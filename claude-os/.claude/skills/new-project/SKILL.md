---
name: new-project
description: Create a new project in the Claude OS — instantiate the standard structure and agent stack (optionally the stocks or crypto pack), run a short onboarding interview, and register it with the Master PA. Use when ROOKAS says "create a new project", "new business", "/new-project".
---
# /new-project

Goal: NEW PROJECT → STANDARD AGENT STACK → PROJECT CONTEXT → READY TO OPERATE.

## 1. Scaffold (deterministic)
Get slug, display name, and pack (none / stocks / crypto) from the request; ask only if missing.
```bash
scripts/new-project.sh <slug> --name "<Name>" [--pack stocks|crypto]
```
The script refuses to overwrite. It copies the template, applies the pack, and appends to REGISTRY.md.
Agents are NOT copied: the library in `.claude/agents/` serves every project.

## 2. Onboarding interview (one cluster per turn, AskUserQuestion for enumerable choices)
Business projects:
1. What it sells, to whom, how it makes money (price, rough margin).
2. Current numbers ROOKAS knows offhand (revenue/month, orders, ad spend, CAC). Mark them `ROOKAS-stated`;
   the data-analyst replaces them with sourced figures.
3. Top 1–3 objectives with a measurable target and deadline.
4. Where the data lives (Shopify / Windsor / Stripe / Motion / sheets / other). Check `_system/CONNECTORS.md`;
   flag any source that isn't connected.
5. Main competitors (names only; research fills detail later).
6. Constraints agents must respect (claims/compliance, brand rules, currency, timezone).

Markets projects: base currency, risk limits (max position %, max drawdown) → GLOBAL.md if missing,
current holdings (or "ROOKAS will paste an export"), watchlist, tracked investors/wallets.

Anything ROOKAS doesn't know stays `UNKNOWN`. Never fill with plausible guesses.

## 3. Write
PROJECT_CONTEXT.md, OBJECTIVES.md, METRICS.md (set canonical sources), CLAUDE.md data-sources table,
initial STATUS.md (health + reason, first 3 next actions). Set REGISTRY status → `active`.

## 4. First data pull (if a connector exists)
Dispatch `data-analyst` to seed `DATA/ledger.csv` with the last 90 days of the core metrics in METRICS.md
and report reconciliation gaps.

## 5. Close
Report in ≤8 lines: what was created, what's UNKNOWN, which data sources are missing, and the one
question worth running first.
