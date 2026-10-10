# GLOBAL_MEMORY — portable preferences and context

Provenance labels: **[EXPLICIT]** you wrote it as an instruction · **[SYSTEM-VISIBLE]** account/environment fact visible to this session · **[INFERRED]** deduced from artifacts (verify before relying on it) · **[HISTORICAL]** a past decision recorded in files · **[STALE?]** possibly outdated.

## 1. Explicit user instructions [EXPLICIT]

Verbatim from your claude.ai personal preferences:

> Direct and brutal. Be my mentor and remember we are building businesses.

Mandatory operating constraints you stated in the migration request (2026-10-10). Keep them as high-priority system rules:

1. The user retains final authority over consequential decisions.
2. Research agents must not autonomously approve or advance opportunities.
3. Require explicit approval before material changes to repositories, production websites, financial commitments or external systems.
4. Preserve functioning implementations unless an approved migration plan establishes a reason to change them.
5. Distinguish facts, assumptions, estimates and recommendations.
6. Track sources, uncertainty, decisions and unresolved questions.
7. Never fabricate repository contents, research findings, integrations or test results.

Paste-ready ChatGPT Custom Instructions:

```
How I want you to respond: Direct and brutal. Act as my mentor. We are building businesses.
Rules: I have final authority on consequential decisions. Never approve or advance opportunities on your own. Ask for explicit approval before any material change to repos, live websites, money, or external systems. Don't break working things without an approved plan. Label facts vs assumptions vs estimates vs recommendations. Cite sources, flag uncertainty, track open questions. Never fabricate repo contents, research, integrations or test results.
```

## 2. Account and environment facts [SYSTEM-VISIBLE]

- GitHub account: `lukaswarren2005-star` (5 repos, see PROJECT_REGISTRY.md).
- Primary email on the Claude account: on file. Deliberately not repeated here; add it yourself if wanted.
- Connected integrations in Claude: ElevenLabs, Gmail, Google Calendar, Motion Creative Analytics, Shopify, Windsor.ai, GitHub, Higgsfield AI (see INTEGRATIONS.md).
- Custom claude.ai skills on the account: `hydre-ugc-video`, `morning`, `import-memory` (plus Anthropic stock skills).

## 3. Inferred context [INFERRED — verify]

- You run a brand/product called **Hydré**. Evidence: private repo `HYDRE` (most recently pushed: 2026-10-09), skill `hydre-ugc-video` ("Make a realistic AI UGC talking-head video ad for Hydré in Higgsfield, using the approved staged recipe (avatar, outfit, background, product, colour, then video)"), and open PR "Add Hydré clean source images for first video build".
- It's likely e-commerce with paid social. Evidence: Shopify, Motion (Meta ad creative analytics) and Windsor.ai (ads/analytics) are connected; Higgsfield and ElevenLabs are for creative/video/voice.
- You have a morning-brief routine (`morning` skill).
- You've explored Claude Managed Agents (forked `launch-your-agent`) and research agents (forked `gpt-researcher`).
- You have a personal dashboard/overview repo (`lukas-overview-`). Purpose unknown; content was not accessible.

## 4. Claude memory / persistent context

- **No Claude memory files were exported.** None are reachable from this container. claude.ai chat memory and Project knowledge are stored server-side. See GAPS.md for how to export them.
- The `launch-your-agent` CLAUDE.md is **Anthropic's project file, not your memory**. It's recorded in DECISION_LOG.md as that project's history only.

## 5. Stale or contradictory items [STALE?]

- CLAUDE.md says "Repo map (state as of 2026-06-15)". That's 4 months old and written by the upstream authors.
- CLAUDE.md says the skills are "Also installed at `~/.claude/skills/launch-your-agent/`". **False in this environment**: that path doesn't exist in this container. It describes the upstream author's machine.
- CLAUDE.md references `CLAUDE.local.md` (test logs, follow-ups). It isn't present in the repo (it's untracked by design), so it can't be exported.
- `cma-primitives.md` has a heading "Design implications for the 60-minute skill". This contradicts CLAUDE.md's rule "no clock/'hour' framing". It's an upstream inconsistency; left unchanged.
