---
name: decide
description: Log a decision to a project's DECISIONS.md, or review decisions whose review date has passed (compare expected vs actual outcome, record lessons). Use when ROOKAS makes a significant decision, says "log this decision", "/decide", or "/decide review".
---
# /decide

## Log (`/decide [project] <decision>`)
1. Identify the project; if ambiguous, ask.
2. Pull context from the conversation and the REPORTS that informed it. Next ID = last `D-###` + 1.
3. Append using the template in DECISIONS.md. Required: context, options considered (≥2, incl. "do nothing"),
   evidence (paths/ledger rows), assumptions, decision, **measurable expected outcome**, risks, owner, review date.
4. If expected outcome isn't measurable, ask ROOKAS for a number before logging. A decision you can't
   grade later teaches nothing.
5. Default review date: 30 days for tactical decisions, 90 for strategic. Ask if unclear.
6. Add a TASKS.md entry for the review. Dispatch project-pa to reflect it in STATUS.

## Review (`/decide review [project|all]`)
1. Find decisions with review date ≤ today and no Actual outcome.
2. For each: dispatch data-analyst for the actual metric vs expected.
3. Append under the entry: `UPDATE YYYY-MM-DD`, actual outcome, verdict (as expected / better / worse / unclear),
   lessons (what assumption was wrong or right).
4. Durable lessons → the relevant agent's memory file and, if universal, propose an addition to GLOBAL.md (ROOKAS approves).

Never edit an original entry. Append only.
