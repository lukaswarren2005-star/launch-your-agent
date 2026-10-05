#!/usr/bin/env python3
"""One-time Higgsfield MCP sign-in → Claude Managed Agents vault credential (mcp_oauth, auto-refresh).

  python3 higgsfield_auth.py start            # prints a sign-in link; open it, approve, copy the URL you land on
  python3 higgsfield_auth.py finish '<URL>'   # exchanges the code and stores the token in the vault

The landing page (localhost) won't load — that's expected; just copy the full URL from the address bar.
The code in that URL is single-use, expires in minutes, and is useless without the PKCE verifier kept
in .higgsfield_oauth.json (chmod 600, gitignored). Tokens are never printed.
Needs network access to mcp.higgsfield.ai and Higgsfield's auth server, plus VAULT_ID in IDS.env.
"""
import base64, datetime, hashlib, json, os, secrets, sys, pathlib, urllib.parse, urllib.request, urllib.error

HERE = pathlib.Path(__file__).resolve().parent
MCP_URL = "https://mcp.higgsfield.ai/mcp"
REDIRECT = "http://localhost:8765/callback"
STATE_FILE = HERE / ".higgsfield_oauth.json"
sys.path.insert(0, str(HERE))
import launch  # reuses key loading, IDS.env and the API caller


def get_json(url, data=None, form=False):
    headers = {"accept": "application/json"}
    body = None
    if data is not None:
        body = urllib.parse.urlencode(data).encode() if form else json.dumps(data).encode()
        headers["content-type"] = "application/x-www-form-urlencoded" if form else "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method="POST" if body else "GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} from {url}: {e.read().decode()[:400]}")


def discover():
    origin = "https://mcp.higgsfield.ai"
    prm = None
    for u in (f"{origin}/.well-known/oauth-protected-resource/mcp", f"{origin}/.well-known/oauth-protected-resource"):
        try:
            prm = get_json(u)
            break
        except SystemExit:
            continue
    as_url = (prm or {}).get("authorization_servers", [origin])[0].rstrip("/")
    for u in (f"{as_url}/.well-known/oauth-authorization-server", f"{as_url}/.well-known/openid-configuration"):
        try:
            return get_json(u)
        except SystemExit:
            continue
    sys.exit("Could not discover Higgsfield's OAuth metadata.")


def start():
    meta = discover()
    reg = get_json(meta["registration_endpoint"], {
        "client_name": "Content Studio (Claude Managed Agent)", "redirect_uris": [REDIRECT],
        "grant_types": ["authorization_code", "refresh_token"], "response_types": ["code"],
        "token_endpoint_auth_method": "none"})
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_urlsafe(16)
    STATE_FILE.write_text(json.dumps({"meta": meta, "client": reg, "verifier": verifier, "state": state}))
    os.chmod(STATE_FILE, 0o600)
    params = {"response_type": "code", "client_id": reg["client_id"], "redirect_uri": REDIRECT,
              "code_challenge": challenge, "code_challenge_method": "S256", "state": state, "resource": MCP_URL}
    if meta.get("scopes_supported"):
        params["scope"] = " ".join(meta["scopes_supported"])
    print("Open this link, sign in to Higgsfield and approve:\n")
    print(meta["authorization_endpoint"] + "?" + urllib.parse.urlencode(params))


def finish(landing_url):
    st = json.loads(STATE_FILE.read_text())
    q = urllib.parse.parse_qs(urllib.parse.urlparse(landing_url).query)
    if q.get("state", [""])[0] != st["state"]:
        sys.exit("State mismatch — run `start` again.")
    meta, client = st["meta"], st["client"]
    form = {"grant_type": "authorization_code", "code": q["code"][0], "redirect_uri": REDIRECT,
            "client_id": client["client_id"], "code_verifier": st["verifier"], "resource": MCP_URL}
    tok = get_json(meta["token_endpoint"], form, form=True)
    expires = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=int(tok.get("expires_in", 3600)))
    auth = {"type": "mcp_oauth", "mcp_server_url": MCP_URL, "access_token": tok["access_token"],
            "expires_at": expires.strftime("%Y-%m-%dT%H:%M:%SZ")}
    if tok.get("refresh_token"):
        auth["refresh"] = {"token_endpoint": meta["token_endpoint"], "client_id": client["client_id"],
                           "refresh_token": tok["refresh_token"], "token_endpoint_auth": {"type": "none"}}
        if tok.get("scope"):
            auth["refresh"]["scope"] = tok["scope"]
    res = launch.call("POST", f"/vaults/{launch.IDS['VAULT_ID']}/credentials",
                      {"display_name": "Higgsfield MCP", "auth": auth})
    launch.save_id("HIGGSFIELD_CRED_ID", res["id"])
    STATE_FILE.unlink()
    print("Stored. Refresh token:", "yes — renews itself" if tok.get("refresh_token") else "NO — will need re-auth when it expires")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("start", "finish"):
        sys.exit(__doc__)
    start() if sys.argv[1] == "start" else finish(sys.argv[2])
