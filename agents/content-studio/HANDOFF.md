# Handoff: launch Content Studio

Staged on 2026-10-04, not launched yet. A new Claude Code session on branch `content-studio-agent` should:

1. Check `ANTHROPIC_API_KEY` is set in the environment (`echo ${ANTHROPIC_API_KEY:+set}`). Never print it or ask for it in chat.
2. `cd agents/content-studio && python3 launch.py model skills env memory vault` and fix any API shape errors against the live docs (skills upload is the least-tested step).
3. If `mcp.higgsfield.ai` is reachable: `python3 higgsfield_auth.py start` → founder opens the link → `python3 higgsfield_auth.py finish '<landing URL>'`.
4. `python3 launch.py agent session` → eval case 1 (Hydré Radar). Poll with `python3 launch.py status`, fetch with `python3 launch.py outputs`, grade against `outcome.md`.
5. Once it passes: `python3 launch.py deploy` (Mon 07:00 Australia/Brisbane), then a manual run (see LAUNCH.md), then `/wrap-up`.

IDs accumulate in `IDS.env`. Commit it after launch so later sessions can resume. `.env` is never committed.
