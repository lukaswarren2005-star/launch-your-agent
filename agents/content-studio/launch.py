#!/usr/bin/env python3
"""Content Studio — resumable launch sequence for Claude Managed Agents.

Usage:  python3 launch.py [step ...]
Steps (default, in order): model skills env memory vault agent session
Later: status · outputs · deploy (only after a run passes the rubric)
Every created ID is appended to IDS.env immediately; re-running skips anything already created.
Needs ANTHROPIC_API_KEY in the shell or in .env (never printed).
"""
import io, json, os, sys, urllib.request, urllib.error, uuid, zipfile, pathlib

HERE = pathlib.Path(__file__).resolve().parent
BASE = "https://api.anthropic.com/v1"
BETA = "managed-agents-2026-04-01"


def load_env(path):
    out = {}
    if path.exists():
        for line in path.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip()
    return out


KEY = os.environ.get("ANTHROPIC_API_KEY") or load_env(HERE / ".env").get("ANTHROPIC_API_KEY", "")
IDS_PATH = HERE / "IDS.env"
IDS = load_env(IDS_PATH)


def save_id(k, v):
    IDS[k] = v
    with IDS_PATH.open("a") as f:
        f.write(f"{k}={v}\n")
    print(f"   saved {k}={v}")


def call(method, path, body=None, extra_headers=None, raw=None, ctype="application/json"):
    headers = {"x-api-key": KEY, "anthropic-version": "2023-06-01", "anthropic-beta": BETA}
    headers.update(extra_headers or {})
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    if data is not None:
        headers["content-type"] = ctype
    req = urllib.request.Request(BASE + path, data=data, method=method, headers=headers)
    print(f"-> {method} {path}")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            txt = r.read().decode()
    except urllib.error.HTTPError as e:
        txt = e.read().decode()
        print(f"   HTTP {e.code}: {txt[:800]}")
        raise SystemExit(1)
    return json.JSONDecoder(strict=False).decode(txt) if txt else {}


def step_model():
    if "MODEL" in IDS:
        return print(f"model: {IDS['MODEL']} (kept)")
    ids = [m["id"] for m in call("GET", "/models?limit=100")["data"]]
    opus = [m for m in ids if "opus" in m]
    print("   available:", ", ".join(ids[:12]))
    save_id("MODEL", opus[0] if opus else ids[0])


def zip_dir(d):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(d.rglob("*")):
            if p.is_file():
                z.write(p, f"{d.name}/{p.relative_to(d)}")
    return buf.getvalue()


def step_skills():
    for d in sorted((HERE / "skills").iterdir()):
        key = "SKILL_" + d.name.upper().replace("-", "_")
        if key in IDS:
            print(f"skill {d.name}: {IDS[key]} (kept)")
            continue
        boundary = uuid.uuid4().hex
        payload = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"files[]\"; filename=\"{d.name}.zip\"\r\n"
                   f"Content-Type: application/zip\r\n\r\n").encode() + zip_dir(d) + f"\r\n--{boundary}--\r\n".encode()
        res = call("POST", "/skills", raw=payload, ctype=f"multipart/form-data; boundary={boundary}",
                   extra_headers={"anthropic-beta": "skills-2025-10-02"})
        save_id(key, res["id"])


def step_env():
    if "ENV_ID" in IDS:
        return print(f"environment: {IDS['ENV_ID']} (kept)")
    save_id("ENV_ID", call("POST", "/environments", json.loads((HERE / "environment.json").read_text()))["id"])


def step_memory():
    if "MEMSTORE_ID" not in IDS:
        save_id("MEMSTORE_ID", call("POST", "/memory_stores", json.loads((HERE / "memory-store.json").read_text()))["id"])
    if IDS.get("MEMORY_SEEDED") == "1":
        return print("memory: already seeded (kept)")
    seed = HERE / "memory-seed"
    for p in sorted(seed.rglob("*.md")):
        call("POST", f"/memory_stores/{IDS['MEMSTORE_ID']}/memories",
             {"path": "/" + str(p.relative_to(seed)), "content": p.read_text()})
    save_id("MEMORY_SEEDED", "1")


def step_vault():
    if "VAULT_ID" not in IDS:
        save_id("VAULT_ID", call("POST", "/vaults", {"display_name": "Content Studio", "metadata": {"owner": "lukas"}})["id"])
    if "HIGGSFIELD_CRED_ID" not in IDS:
        print("   !! Higgsfield credential not stored yet — run: python3 higgsfield_auth.py")


def step_agent():
    if "AGENT_ID" in IDS:
        return print(f"agent: {IDS['AGENT_ID']} v{IDS.get('AGENT_VERSION')} (kept)")
    a = json.loads((HERE / "agent.json").read_text())
    a["model"] = IDS["MODEL"]
    a["skills"] = [{"type": "custom", "skill_id": v, "version": "latest"} for k, v in IDS.items() if k.startswith("SKILL_")]
    res = call("POST", "/agents", a)
    save_id("AGENT_ID", res["id"])
    save_id("AGENT_VERSION", str(res["version"]))


def step_session():
    if "HIGGSFIELD_CRED_ID" not in IDS:
        print("   note: no Higgsfield credential yet — fine for the Radar (it never generates), required for production.")
    sess = call("POST", "/sessions", {
        "agent": IDS["AGENT_ID"], "environment_id": IDS["ENV_ID"], "title": "Hydré radar — eval case 1",
        "vault_ids": [IDS["VAULT_ID"]],
        "resources": [{"type": "memory_store", "memory_store_id": IDS["MEMSTORE_ID"], "access": "read_write",
                       "instructions": "Content Studio's memory. Read README.md first; follow the content-studio skill's brain-protocol."}]})
    save_id("SESSION_ID", sess["id"])
    call("POST", f"/sessions/{sess['id']}/events", json.loads((HERE / "kickoff.json").read_text()))
    print(f"   console: https://platform.claude.com/workspaces/default/sessions/{sess['id']}")


def step_deploy():
    if "DEPLOYMENT_ID" in IDS:
        return print(f"deployment: {IDS['DEPLOYMENT_ID']} (kept)")
    txt = (HERE / "deployment.json").read_text()
    for k in ("AGENT_ID", "ENV_ID", "VAULT_ID", "MEMSTORE_ID"):
        txt = txt.replace("$" + k, IDS[k])
    res = call("POST", "/deployments?beta=true", json.loads(txt))
    save_id("DEPLOYMENT_ID", res["id"])
    print("   upcoming runs:", res.get("schedule", {}).get("upcoming_runs_at"))
    print(f"   console: https://platform.claude.com/workspaces/default/deployments/{res['id']}")


def step_status():
    d = call("GET", f"/sessions/{IDS['SESSION_ID']}")
    print("   status:", d.get("status"), "| outcome:", [(e.get("result"), (e.get("explanation") or "")[:300]) for e in d.get("outcome_evaluations", [])])
    print("   usage:", d.get("usage"))


def step_outputs():
    out = HERE / "outputs" / IDS["SESSION_ID"]
    out.mkdir(parents=True, exist_ok=True)
    for f in call("GET", f"/files?scope_id={IDS['SESSION_ID']}", extra_headers={"anthropic-beta": BETA + ",files-api-2025-04-14"})["data"]:
        req = urllib.request.Request(f"{BASE}/files/{f['id']}/content", headers={"x-api-key": KEY, "anthropic-version": "2023-06-01", "anthropic-beta": BETA + ",files-api-2025-04-14"})
        dest = out / f["filename"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(urllib.request.urlopen(req, timeout=120).read())
        print("   saved", dest.relative_to(HERE))


STEPS = {"model": step_model, "skills": step_skills, "env": step_env, "memory": step_memory,
         "vault": step_vault, "agent": step_agent, "session": step_session,
         "status": step_status, "outputs": step_outputs, "deploy": step_deploy}
DEFAULT = ["model", "skills", "env", "memory", "vault", "agent", "session"]

if __name__ == "__main__":
    if not KEY:
        sys.exit("ANTHROPIC_API_KEY not set — export it or put it in my-agent/.env (never paste it in chat).")
    for name in (sys.argv[1:] or DEFAULT):
        print(f"\n== {name}")
        STEPS[name]()
