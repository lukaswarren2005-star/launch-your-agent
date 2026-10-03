---
name: report
description: Produce a daily, weekly, or monthly report for one project or the whole system (Master PA brief). Includes only information that could change a decision. Use for "/report weekly hydre", "/report daily all", "weekly review", "monthly strategic review". Also the entry point for scheduled routines.
---
# /report <daily|weekly|monthly> <project|all>

**Rule zero: a report exists to change decisions.** If a section has nothing decision-relevant, write
"No material change" in one line. A short report is a good report.

## daily (all): Master PA brief, ≤15 lines
Today's calendar (Google Calendar) · tasks due ≤ today (TASKS.md) · decisions waiting on ROOKAS (all
STATUS files) · decisions past review date · HIGH-materiality news on holdings (news-intel, only if markets
projects are active) · new blockers.

## weekly (per project)
1. data-analyst: refresh ledger for the week; KPI table this week vs last vs 4-week avg, anomalies labelled.
2. In parallel only as relevant: cfo (cash, margin), marketing (funnel/creative), research (competitor
   changes), or for markets packs: portfolio-risk + news-intel + filings-intel (new filings).
3. project-pa: update STATUS; list experiments needing action, decisions due.
4. Synthesize: KPIs · what changed and why (labelled) · risks · **decisions required** · next week's 3 priorities.
5. Save to `REPORTS/YYYY-MM-DD-weekly.md`.

## monthly (per project or all)
Strategic review: financial performance vs objectives, growth, competitive landscape shifts, experiments
concluded (wins/losses), decisions reviewed (`/decide review`), lessons, proposed priority changes for
ROOKAS to approve. QA-audit the report before delivering.

## Unattended (routine) runs
When run by a scheduled routine: never call write tools (they'll block anyway), commit only REPORTS/ and
STATUS changes, and put anything needing action under DECISION REQUIRED FROM ROOKAS at the top.
