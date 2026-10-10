# AGENT_REGISTRY

## 1. Existing agents — what actually exists

**No custom agents (subagent definitions) exist in any accessible location.** There's no `.claude/agents/` in the repo, and no agent definitions were visible in the session. Nothing is invented here.

What does exist is a **skill chain**, not an agent hierarchy:

| Unit | Role | Routing | Hands off to | Approval gates |
|---|---|---|---|---|
| `launch-your-agent` (skill) | Founder copilot: builds a Claude Managed Agent | `/launch-your-agent`, "build me a managed agent" | `wrap-up` at end of Phase 4 | Brief approval; no overwrite of `my-agent/`; `always_ask` on write actions |
| `wrap-up` (skill) | Close-out reporter | `/wrap-up`, "close it out", end of launch-your-agent | back to `launch-your-agent` for any change | Reports only; asks before waiting on a running session |
| Agents *built by* launch-your-agent | Live CMA agents in the founder's Anthropic account | Deployment cron / on-demand session | — | Drafts-only default, `max_iterations: 3` |

Whether any CMA agents are live in your Anthropic account is **unknown**: no API key was available and none were queried.

Stock harness subagent types (`general-purpose`, `Explore`, `Plan`, `claude-code-guide`, `statusline-setup`) are Claude Code built-ins, not yours.

## 2. Target hierarchy (requested design — NOT yet built anywhere)

```
L0  Chief of Staff (Master PA)
     │  owns: your priorities, calendar/inbox triage, routing, decision queue, morning brief
     ├── L1  Project Manager: <Project>   (one per project; template below)
     │        ├── L2 Scaling & Growth
     │        ├── L2 CFO & Financial Modelling
     │        ├── L2 Marketing & Customer Acquisition
     │        ├── L2 Data & Analysis
     │        └── L2 Research & Competitor Intelligence
     └── Shared specialist pool (callable by CoS or any PM)
              ├── Stock-market Research & Investor-trade Analysis
              ├── Crypto Research
              ├── Opportunity Scouting
              ├── Creative Production
              └── Website & Software Development
```

### Routing rules
- You → CoS by default. CoS routes by project tag; untagged → CoS asks.
- PM → its L2 specialists for project work. Cross-project or non-project work → the shared pool via CoS.
- Specialists never talk to external systems with write access without a PM → CoS → **you** approval chain.
- Every handoff carries: objective, project, constraints, deadline, required output format, and the facts/assumptions/estimates/recommendations split.

### Universal agent contract (put this in every agent's instructions)
```
Authority: The user has final say on every consequential decision. You recommend; you never approve.
Approval required before: any repo change, production website change, financial commitment, ad-spend change, outbound message, or write to an external system.
Output labels: [FACT] (with source) / [ASSUMPTION] / [ESTIMATE] (with range & method) / [RECOMMENDATION].
Always end with: Decisions needed · Open questions · Sources.
Never fabricate data, repository contents, integrations, or test results. Say "unknown" instead.
Preserve working implementations unless an approved plan says otherwise.
```

### Role cards

| Agent | Responsibilities | Inputs | Outputs | Tools / integrations | Prohibited |
|---|---|---|---|---|---|
| **Chief of Staff** | Triage, routing, weekly priorities, decision queue, morning brief | Gmail, Calendar, PM reports | Daily brief, decision list, delegations | Gmail, Calendar, Tasks (scheduled) | Sending email or accepting meetings without approval |
| **Project Manager (template)** | Roadmap, status, risk log, specialist briefs | Project files, specialist outputs | Weekly status, next actions, risk register | Project knowledge, GitHub (read) | Changing scope/budget; merging code |
| **Scaling & Growth** | Growth model, channels, ops bottlenecks | Sales/traffic data | Growth plan with ranked bets | Shopify (read), Windsor (read) | Executing campaigns |
| **CFO & Financial Modelling** | P&L, unit economics, cash runway, scenarios | Shopify orders, Stripe, costs | Models (xlsx) with stated assumptions | Code interpreter, Shopify (read) | Any payment, commitment or pricing change |
| **Marketing & Acquisition** | Creative briefs, ad analysis, funnel | Motion, Windsor, Meta data | Briefs, test matrices, copy drafts | Motion, Windsor (read), Higgsfield (via Creative) | Changing budgets/bids; publishing ads |
| **Data & Analysis** | Dashboards, cohort/LTV, attribution checks | Exports, connectors | Analyses with method + caveats | Code interpreter, Windsor (read) | Presenting estimates as facts |
| **Research & Competitor Intel** | Competitor tracking, market sizing | Web, Motion competitors | Sourced briefs | Web/Deep Research | Advancing or approving opportunities |
| **Stock-market & Investor-trade** | Equity research, trade theses | Filings, market data | Theses with risks, never orders | Web/Deep Research | Placing trades; personalised financial "advice" framed as certainty |
| **Crypto Research** | Token/protocol research, on-chain risk | Web, docs | Risk-rated research notes | Web | Transactions, wallet actions |
| **Opportunity Scouting** | Find deals/markets/partners | Web, your thesis | Scored shortlist → your queue | Web | **Approving/advancing any opportunity** (hard rule) |
| **Creative Production** | UGC, ads, voice, visuals; owns `hydre-ugc-video` recipe | Brand kit, briefs | Drafts/renders for approval | Higgsfield, ElevenLabs | Publishing (TikTok etc.) without approval; spending credits beyond agreed budget |
| **Website & Software Dev** | Site/app changes, repo work | Repos, tickets | PRs/branches, never direct prod | GitHub, Codex | Pushing to prod/main, deploys without approval |

### Mapping existing assets → target

| Existing | Goes to |
|---|---|
| `morning` skill | Chief of Staff (morning brief) |
| `hydre-ugc-video` skill | Creative Production (Hydré PM) |
| Motion / Windsor / Shopify connectors | Marketing, Data, CFO, Growth under the Hydré PM |
| `gpt-researcher` fork | Research & Competitor Intel (as a tool, if you ever ran it) |
| `launch-your-agent` + `wrap-up` | Website & Software Dev, *only* if you deploy agents on Anthropic CMA. Otherwise archive |
| `lukas-overview-` | Possibly the CoS dashboard. Unknown until it's retrieved |

### ChatGPT implementation
ChatGPT has no native multi-agent hierarchy with automatic delegation. Practical build:
- CoS = your main ChatGPT with Custom Instructions + Memory + Tasks.
- One **Project** per business (Hydré, …) = the PM layer, with project instructions and files.
- Specialists = **Custom GPTs**. Invoke them inside a chat with `@GPT-name`. You are the router. That actually enforces your approval rule.
- Real automated delegation needs the OpenAI Agents SDK (code, handoffs, guardrails). Build that only after the manual version proves which specialists you actually use.

Reusability: copy the PM template + the 5 standard specialists per new project; the shared pool stays global.
