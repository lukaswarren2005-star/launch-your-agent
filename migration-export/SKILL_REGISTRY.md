# SKILL_REGISTRY

Legend: **Exported** = original files preserved unmodified · **Identified** = name and description known, content not exported · **Stock** = Anthropic-provided, not yours; don't migrate, ChatGPT has its own equivalent.

## A. Custom / repo skills — EXPORTED

### A1. `launch-your-agent` (v0.3.0) — author: Anthropic (upstream), license Apache-2.0
- **Path:** `.claude/skills/launch-your-agent/` (SKILL.md + references/: interview.md, cma-api.md, examples-bank.md, mock-connectors.md, overview-template.html, overview.css, build-sheet.example.json)
- **Original description (verbatim):** "Help a technical founder build whatever they want on Claude Managed Agents — an internal worker, a piece of their product, a customer-facing agent. Find out what they want to build, scope a v0, launch it in their account, grade it, iterate, and (if it should run on a clock) put it on a scheduled deployment, with everything bigger laid out as v1/v2. Use when a founder says "launch my agent", "/launch-your-agent", "build me a managed agent", or wants to build something on CMA. Keywords: managed agents, CMA, founder, launch, scheduled deployment, outcome rubric."
- **Trigger/routing:** `/launch-your-agent` or the phrases above.
- **Inputs:** founder interview answers; `ANTHROPIC_API_KEY` (shell env or `my-agent/.env`) from the launch step; optional `ant` CLI.
- **Outputs:** `./my-agent/` folder: build-sheet.json, agent.json/.yaml, environment.json, outcome.md, first_prompt.txt, kickoff.json, deployment.json, evals/, agent-overview.html + overview.css, NEXT-DIRECTIONS.md, LAUNCH.md, IDS.env, .env, .gitignore. Live CMA objects in the founder's Anthropic account (agent, environment, session, deployment, optionally vault and memory store).
- **Phases:** 1 Interview → plan (no key) · 2 Stage then launch · 3 Grade, iterate, eval · 4 Scheduled deployment (only if recurring) → hands off to `wrap-up`.
- **Tools required:** Bash (curl/python3), file Write/Edit, AskUserQuestion, background tasks, browser open.
- **Approval requirements:** brief approved via AskUserQuestion before files are emitted; never overwrite an existing `my-agent/` without asking; write-actions to external systems only with an `always_ask` gate; drafts-first by default.
- **Prohibited:** API key in chat or transcript (if it happens → rotate); literal dates in deployment kickoffs; listing built-in tools individually in agent.json; invented specifics about the founder's problem; unverified timings; cost notes unless asked.
- **Eval criteria:** Outcome rubric (3–6 binary criteria, `max_iterations: 3`); golden set = the founder's past cases (case 1 is the build input, the rest held back); re-run evals before promoting a new agent version.
- **Fallback ladder:** live docs → Console UI → archetype config → local Claude Code workflow.
- **ChatGPT compatibility: LOW as an executable skill.** It drives Anthropic's Managed Agents API and the Claude Code harness (AskUserQuestion, background tasks, Bash). In ChatGPT it can only serve as a *reference/coaching document*. Equivalent target platform: OpenAI Agents SDK / Responses API, which is a rewrite, not a port. **Recommendation:** don't migrate. Keep using it in Claude Code if you still build on CMA; otherwise archive it.

### A2. `wrap-up` (v0.2.0) — author: Anthropic (upstream)
- **Path:** `.claude/skills/wrap-up/SKILL.md`
- **Description (verbatim):** "Close out (or revisit) a Claude Managed Agent build — refresh the overview page, recap every primitive the founder now owns, show the run log and live status, suggest 1–2 tailored next upgrades, and sweep hygiene (sessions archived, key only in .env, no literal dates in deployment kickoffs). Use when the founder says "/wrap-up", "wrap up", "close it out", "where do things stand with my agent", or at the end of a /launch-your-agent build."
- **Dependencies:** `./my-agent/` from launch-your-agent; reads `../launch-your-agent/references/` (**hard dependency on the sibling directory layout**); API key optional (describe-only without it).
- **Handoff:** invoked by launch-your-agent Phase 4. It reports and suggests only; changes go back through launch-your-agent.
- **Prohibited:** cost notes unless asked; re-litigating design decisions.
- **ChatGPT compatibility: LOW.** Same reasons as A1.

## B. Your custom claude.ai skills — IDENTIFIED, NOT EXPORTED

| Skill | Description (as shown to this session) | Why not exported | Priority |
|---|---|---|---|
| `hydre-ugc-video` | "Make a realistic AI UGC talking-head video ad for Hydré in Higgsfield, using the approved staged recipe (avatar, outfit, background, product, colour, then video)." | claude.ai synced-skill files couldn't be read (access blocked) | **HIGHEST**: this is your real business IP |
| `morning` | "Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only when the user explicitly asks to run, see, or set up their morning brief, or if they invoke /morning by name." | same | High |
| `import-memory` | "Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data." | same | Low: it's Claude-direction only; probably irrelevant after you move |

Retrieval: GAPS.md §2. ChatGPT mapping, once retrieved:
- `hydre-ugc-video` → a Custom GPT with the recipe as instructions, plus the Higgsfield connector if ChatGPT supports it (verify). Otherwise the GPT produces staged prompts and you run them in Higgsfield manually.
- `morning` → ChatGPT Tasks (scheduled) + Gmail/Calendar connectors.

## C. Stock Anthropic skills available in the session — NOT YOURS, do not migrate

`session-start-hook`, `dataviz`, `artifact-design`, `artifact-diagramming`, `artifact-capabilities`, `update-config`, `keybindings-help`, `code-review`, `simplify`, `fewer-permission-prompts`, `loop`, `claude-api`, `run`, `plugin-authoring`, `init`, `security-review`, `built-in-browser`, `chrome-browser`, `computer-use`, `deep-research`, `docs`, `docx`, `google-workspace`, `pdf`, `pptx`, `skill-creator`, `xlsx`. ChatGPT equivalents are built in (Deep Research, Canvas, file generation, Agent mode).
