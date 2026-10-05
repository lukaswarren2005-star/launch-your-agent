#!/usr/bin/env python3
"""Re-run held-back eval cases against a pinned agent version: python3 evals/run_evals.py <agent_version>
Case 1 is unattended (outcome kickoff); cases 2–3 are interactive — this script starts them and prints the
Console link so Lukas can play the founder; verdicts are recorded by hand in evals/results-v<N>.json."""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import launch
ver = int(sys.argv[1]) if len(sys.argv) > 1 else int(launch.IDS["AGENT_VERSION"])
results = {}
for case in sorted(pathlib.Path(__file__).parent.glob("case-*")):
    s = launch.call("POST", "/sessions", {"agent": {"type": "agent", "id": launch.IDS["AGENT_ID"], "version": ver},
        "environment_id": launch.IDS["ENV_ID"], "title": f"eval {case.name} v{ver}", "vault_ids": [launch.IDS["VAULT_ID"]],
        "resources": [{"type": "memory_store", "memory_store_id": launch.IDS["MEMSTORE_ID"], "access": "read_only"}]})
    if case.name.startswith("case-01"):
        launch.call("POST", f"/sessions/{s['id']}/events", json.loads((launch.HERE / "kickoff.json").read_text()))
    results[case.name] = {"session": s["id"], "console": f"https://platform.claude.com/workspaces/default/sessions/{s['id']}", "verdict": None}
    print(case.name, results[case.name]["console"])
out = pathlib.Path(__file__).parent / f"results-v{ver}.json"
out.write_text(json.dumps(results, indent=2)); print("wrote", out)
