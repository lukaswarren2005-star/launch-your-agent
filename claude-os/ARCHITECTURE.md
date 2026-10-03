# Claude OS — Implementation Architecture

Design doc for the operating system. Read this before touching any agent prompt.

---

## 0. The four calls that shape everything

**1. The engine is Claude Code running over one git repo. claude.ai chat Projects are not the engine.**
A claude.ai Project can't call another Project, can't write its own knowledge files, and can't run
specialists in parallel. That rules it out as the place where the hierarchy lives. Claude Code has
what this design needs:

| Need | Claude Code primitive |
|---|---|
| Orchestrator with global visibility | Root `CLAUDE.md` = Master PA |
| Isolated specialists, each with its own context window | Subagents (`.claude/agents/*.md`) |
| Reusable procedures (new project, decision log, reports) | Skills (`.claude/skills/*/SKILL.md`) |
| Shared, persistent, versioned memory | Markdown/CSV files in git |
| Tool access per agent | Subagent `tools:` allowlist + `settings.json` permission rules |
| Recurring reports | Cloud routines (claude.ai/code) that run a skill and commit the result |
| Mobile / anywhere access | claude.ai/code sessions on this same repo |

**2. The hierarchy is three logical levels but two runtime levels.**
In Claude Code a subagent cannot spawn another subagent. So the **Master PA (main session) does all
dispatching**. The **Project PA** is a *context layer* (`projects/<p>/CLAUDE.md` + `STATUS.md`) that the
Master PA loads when it goes into a project, plus a `project-pa` subagent that does the bookkeeping
(status, tasks, decision-log hygiene, project reports). Nothing is lost: what the Project PA "knows"
lives in its files, and the Master PA dispatches the specialists using that knowledge.

```
ROOKAS
  │
  ▼
MASTER PA  (main session · root CLAUDE.md · REGISTRY · ROUTING)
  │  loads project context ──► PROJECT PA LAYER (projects/<p>/CLAUDE.md, STATUS, OBJECTIVES, DECISIONS)
  │  dispatches in parallel ─► SPECIALIST SUBAGENTS (growth, cfo, marketing, data-analyst, research, …)
  │                               │ read: canonical DATA, project memory, own agent memory
  │                               │ read-only connectors: Shopify, Windsor, Motion, EDGAR, web
  │                               ▼
  │                            structured outputs ──► REPORTS/ (the shared bus)
  │  qa-auditor gate (when triggered)
  ▼
SYNTHESIS + DISAGREEMENTS + "DECISION REQUIRED FROM ROOKAS"
  ▼
ROOKAS decides ──► /decide logs it ──► execution (write tools need approval) ──► result
  ▼
RESULT → DATA/ledger + DECISIONS review date + agent memory   (loop closes)
```

**3. You specified ~30 agents. The system ships 16. Every cut is a merge, not a loss.**
An agent should exist when it has a distinct method, distinct data, or a distinct failure mode.
Several of the specified agents are the same agent pointed at a different source:

| Specified | Built as | Why |
|---|---|---|
| Research + Competitor Intelligence | `research` | Same workflow (source→evidence→verification→insight); competitors are one target |
| Financial Analysis | `cfo` | Same numbers, same model; two agents = two versions of the truth |
| Risk Analysis (business) | `cfo` + `qa-auditor` | Business risk is financial risk + reasoning risk |
| Stock Market Researcher + Smart Money | `filings-intel` | Both are SEC filings → position timelines. One timeline database, not two |
| Stocks News + Crypto News/Narrative | `news-intel` (shared) | Same discipline: primary source, dated, materiality |
| Stocks Macro + Crypto Macro/Liquidity | `macro-analyst` (shared) | Same mechanisms; liquidity is a section |
| Stocks Portfolio/Risk + Crypto Risk | `portfolio-risk` (shared) | **Separate risk agents can't see your total exposure.** One book, one risk agent |
| Stocks Technical/Quant + Crypto Market Structure | `technical-quant` (shared) | Price/volume/momentum are asset-agnostic; derivatives structure is a crypto module |
| Crypto Fundamental + Tokenomics | `crypto-fundamental` | Supply math is part of crypto fundamentals |
| On-chain + Whale Intelligence | `onchain-intel` | Whale tracking is on-chain tracking with an attribution standard |
| Stocks/Crypto Data Analyst | `data-analyst` (standard) | Same agent, different ledger |
| Stocks PA / Crypto PA | Project PA layer | Same as every project |

If a merged agent starts producing shallow work in one domain, split it then. Splitting on evidence is
cheap; maintaining 30 prompts nobody tests is not.

**4. The binding constraint is data, not agents.**
An agent with no data feed is a confident prompt that makes things up. What's actually wired today:

| Domain | Data available now | Gap |
|---|---|---|
| E-commerce (e.g. HYDRÉ) | **Shopify** (orders, products, analytics), **Windsor.ai** (Meta/Google/TikTok ads, GA4, Klaviyo…), **Motion** (Meta creative analytics) | **Stripe** connector present but unauthorized → authorize in claude.ai connector settings |
| Personal ops | **Gmail**, **Google Calendar** | none |
| Stocks — filings | SEC EDGAR is free and official (`data.sec.gov` JSON, full-text search) via WebFetch | No 13F aggregator; agent builds timelines itself |
| Stocks — prices/fundamentals | Web only | No market-data connector. Price-dependent work (technicals, risk) is weak until one is added |
| Crypto — on-chain | Public APIs via WebFetch (DefiLlama etc.); explorers often need keys | No on-chain data connector. `onchain-intel` is limited to public dashboards/APIs |

So the business stack is ready to work on real numbers now. The investing stacks are ready
structurally but will be research-grade, not data-grade, until a market-data and on-chain source exist.
Every agent is told to say this out loud instead of filling the gap.

---

## 1. What is a Claude Project?

**Not a claude.ai Project. A folder: `projects/<slug>/`.** One per business, venture, or domain
(HYDRÉ, STOCKS, CRYPTO, …). Registered in `_system/REGISTRY.md`. Personal ops are not a project; they
belong to the Master PA (`_system/GLOBAL.md`, `_system/TASKS.md`, Calendar/Gmail connectors).

Optional: one claude.ai Project called "Claude OS — read-only" with `GLOBAL.md` + `REGISTRY.md` uploaded,
for quick mobile thinking. Treat it as a stale snapshot. Anything that writes state happens in Claude Code.

## 2. What is an individual agent?

A **subagent file** in `.claude/agents/`. **Agents are defined once and are project-agnostic.** The
project is passed in at dispatch ("project: hydre"). The agent then reads that project's files. That's
what makes cloning cheap: a new project gets the whole stack without copying 16 prompts.

| Tier | Agents |
|---|---|
| Standard stack (every project) | `project-pa`, `growth`, `cfo`, `marketing`, `data-analyst`, `research` |
| Library modules (on demand) | `copywriter`, `qa-auditor` |
| Markets pack (stocks + crypto share) | `macro-analyst`, `news-intel`, `technical-quant`, `portfolio-risk` |
| Stocks pack | `filings-intel`, `equity-fundamental` |
| Crypto pack | `onchain-intel`, `crypto-fundamental` |

Every agent body follows the Universal Agent Specification (Identity → Failure Modes).

## 3. What is a reusable prompt/template?

| Kind | Where | Used for |
|---|---|---|
| Project skeleton | `_templates/project/` | Copied by `scripts/new-project.sh` |
| Extension packs | `_templates/packs/{stocks,crypto}/` | Extra files layered on at creation |
| Procedures | `.claude/skills/` | `/new-project`, `/decide`, `/experiment`, `/report` |
| Shared protocols | `_system/PROTOCOLS.md` | Output format, evidence labels, disagreement, checkpoints. Agents read it; it isn't copied into 16 prompts |

## 4. What is project knowledge (Level 2)?

`projects/<p>/`: `PROJECT_CONTEXT.md` (business model, customers, strategy), `OBJECTIVES.md`,
`STATUS.md` (live state: priorities, blockers, next actions, outstanding decisions), `DECISIONS.md`,
`METRICS.md` (definitions), `DATA/ledger.csv` (canonical numbers), `EXPERIMENTS/`, `RESEARCH/`,
`COMPETITORS/`, `FINANCIALS/`, `MARKETING/`, `SOPs/`, `REPORTS/`, `LOGS/`.

## 5. What is global knowledge (Level 1)?

`_system/GLOBAL.md`: goals, principles, operating style, operating rules. Imported into every Master PA
session via root `CLAUDE.md`. Kept short on purpose, because everything there is paid for in every session.
`_system/REGISTRY.md` (projects), `ROUTING.md`, `PROTOCOLS.md`, `CONNECTORS.md`, `TASKS.md`.

## 6. How do agents share information?

**Files are the bus. Agents never talk to each other directly.** That's a Claude Code constraint, and
it's also the right design, because every handoff becomes inspectable and versioned.

1. **Canonical facts**: `DATA/ledger.csv`. Only `data-analyst` writes it. Everyone else reads it.
   Agents may *pull* live connector data for analysis, but a number that disagrees with the ledger gets
   flagged, not used silently.
2. **Definitions**: `METRICS.md`. Most agent "disagreements" about CAC or ROAS are really two
   definitions. Lock the definition once and reference it.
3. **Findings**: each dispatch writes `REPORTS/YYYY-MM-DD-<topic>-<agent>.md` in the standard output
   format. The Master PA passes paths (not paraphrases) to downstream agents.
4. **Decisions**: `DECISIONS.md`, appended by `/decide`.

## 7. How does the Master PA route?

`_system/ROUTING.md` holds the intent→agents table and the protocol:

1. **Classify**: which project(s)? which intent? Is it consequential (money, commitments, external writes)?
2. **Load the minimum context**: the project's `STATUS.md` and `CLAUDE.md`, not the whole folder.
3. **Pick 1–4 agents** from the table. If one agent is enough, use one. Everyone-by-default is banned.
4. **Dispatch in parallel** with a brief: project slug, the question, relevant file paths, the deadline
   or horizon, and what decision this informs.
5. **Sequential handoff** only when B needs A's output (e.g. data-analyst diagnoses, then cfo prices it).
6. **QA gate** (`qa-auditor`) when the output carries a recommendation involving money/positions, cites
   numbers not in the ledger, or agents conflict.
7. **Synthesize**: answer, disagreements (never averaged away), and `DECISION REQUIRED FROM ROOKAS`.
8. **Close the loop**: update STATUS via `project-pa`, log the decision with `/decide`, promote memory.

## 8. How does memory work?

| Level | Lives in | Loaded | Written by |
|---|---|---|---|
| L1 Global | `_system/GLOBAL.md` | Every session (imported) | ROOKAS, Master PA on explicit instruction |
| L2 Project | `projects/<p>/*` | When the project is in scope (STATUS first, rest on demand) | project-pa, data-analyst (ledger), `/decide`, `/experiment` |
| L3 Agent | Method → agent file (library). Project-specific findings → `projects/<p>/AGENTS/<agent>.md` | By that agent only, at start of dispatch | That agent (append-only, dated, ≤ ~150 lines, prune oldest) |
| L4 Session | The conversation | Now | Nobody. Dies with the session unless promoted |

**Promotion rule** (end of every substantive task): fact → ledger, decision → DECISIONS, durable
specialist learning → agent memory, project state change → STATUS. Everything else is discarded on purpose.

## 9. How are tools/connectors assigned?

Decision rights are enforced by **tools, not prompts**. A prompt that says "don't spend money" is a request;
a missing write tool is a guarantee.

- **Subagents get read paths only.** Writes to external systems (ad budgets, Shopify products, discounts,
  inventory, sending email, calendar invites) are set to `ask` in `.claude/settings.json`, which means a
  human click every time, and *blocked* in unattended routine runs.
- Agents that need connectors inherit tools (connector tool names differ between cloud and local
  installs, so hard-coding them breaks portability). The permission layer is what enforces safety.
- Agents that should never touch connectors (`qa-auditor`, `research`, the markets agents) get an explicit
  `tools:` allowlist: Read, Grep, Glob, WebSearch, WebFetch, plus Write/Edit only where they own a file.
- Map of connector → agent → read/write: `_system/CONNECTORS.md`.

## 10. How are new projects cloned?

`/new-project <slug> [--pack stocks|crypto|markets]`:
1. `scripts/new-project.sh` deterministically copies `_templates/project/` (+ pack), substitutes the
   slug/name/date, and appends a row to `REGISTRY.md`. It refuses to overwrite an existing project.
2. The skill then runs a short onboarding interview (business model, customers, current numbers, top
   3 objectives, known data sources) and fills `PROJECT_CONTEXT.md`, `OBJECTIVES.md`, `METRICS.md`.
3. It asks which connectors hold this project's data and records them in the project `CLAUDE.md`.
4. It writes an initial `STATUS.md`. The project is now routable.

No agent prompts are copied. The stack exists the moment the folder does.

## 11. How do Stocks and Crypto extend the standard?

A **pack** adds files and enables agents. It never forks the base structure.

| | Stocks pack | Crypto pack |
|---|---|---|
| Extra files | `WATCHLIST.md`, `PORTFOLIO.md` (canonical holdings), `FILINGS/position-timelines.md`, `THESES/` | `WATCHLIST.md`, `PORTFOLIO.md`, `ONCHAIN/address-book.md` (attribution tiers), `ONCHAIN/unlocks.md`, `THESES/` |
| Agents enabled | filings-intel, equity-fundamental + markets pack | onchain-intel, crypto-fundamental + markets pack |
| Standard agents kept | data-analyst, research, project-pa, qa-auditor | same |
| Standard agents dropped | growth, marketing, cfo (no business P&L to run) | same |

`portfolio-risk` reads **both** PORTFOLIO files, so exposure, correlation and drawdown are computed on
the whole book.

## 12. How do QA and verification work?

- **Built in**: every agent labels claims FACT / INFERENCE / HYPOTHESIS / UNKNOWN (data work uses
  KNOWN / PROBABLE / UNCERTAIN / UNKNOWN), with source and date per fact.
- **Gate**: `qa-auditor` runs when the routing protocol triggers it (§7.6). It gets the output paths
  and the ledger, re-checks the 3–5 load-bearing claims against primary sources, and returns
  PASS / PASS-WITH-FIXES / FAIL with specific defects. FAIL goes back to the originating agent once;
  a second FAIL reaches ROOKAS as an open uncertainty, not a hidden one.
- **Numbers**: any figure in a synthesis must trace to the ledger or a cited source. Untraceable numbers
  are a QA FAIL.
- **Decisions**: `/decide` sets a review date. `/report` surfaces decisions past their review date, so
  outcomes get compared against expectations. That's how the system learns.

---

## Build order (what to do, in order)

1. **Fill `_system/GLOBAL.md`** (goals, priorities, rules). 15 minutes, and it's the highest-leverage
   file in the system.
2. **`/new-project hydre`** with real numbers. Seed `DATA/ledger.csv` from Shopify + Windsor.
   Run one real question end to end ("why is CAC up?"). Fix the prompts on what breaks.
3. **Authorize Stripe** in claude.ai connector settings if HYDRÉ takes payments there.
4. **`/new-project stocks --pack stocks`**. Start `filings-intel` on 3–5 investors you actually follow.
5. **`/new-project crypto --pack crypto`** last. It has the weakest data access.
6. **One weekly routine per active project.** No daily reports until a weekly one has changed a
   decision at least once.
7. **v2**: move always-on monitors (filings, news) to Claude Managed Agents scheduled deployments
   (see `../cma-primitives.md`) once their prompts are stable.

Building the investing stacks before the business stack has run one real question means building the
fun part before the part that pays.
