# SHARED PROTOCOLS
Every agent reads this at the start of a dispatch. It's the common law of the system.

## 1. Standard output format
Write to `projects/<p>/REPORTS/YYYY-MM-DD-<topic>-<agent>.md` and return the same content (or a
≤15-line summary + path when it's long).
```
EXECUTIVE SUMMARY        ≤3 lines
QUESTION                 as briefed
ANSWER                   direct
EVIDENCE                 claim · label · source · date
KEY FINDINGS
DATA                     figures used, each traced to ledger row or source
ASSUMPTIONS
UNCERTAINTIES
RISKS
OPPORTUNITIES
RECOMMENDATION
ALTERNATIVES             with trade-offs
DECISION REQUIRED FROM ROOKAS   (omit if none)
NEXT ACTIONS
HANDOFFS                 agent · why · what to pass
```
Drop sections that would be empty. Keep the logic.

## 2. Evidence labels
| Label | Meaning | Minimum support |
|---|---|---|
| FACT | Verified | Primary source or canonical ledger, with date |
| INFERENCE | Follows from facts | The facts it follows from are cited |
| HYPOTHESIS | Plausible, untested | State what test would confirm/refute it |
| UNKNOWN | Not established | State what data would establish it |
Data work may use KNOWN / PROBABLE / UNCERTAIN / UNKNOWN. Same rules.

## 3. Source rules
- Primary over secondary (filing > article about the filing; Shopify export > screenshot).
- Every external fact carries **publication date and retrieval date**. Old ≠ current.
- Never invent sources, URLs, figures, quotes, or investor motives. If you can't find it, say UNKNOWN.
- Markets: account for reporting lags (13F: ≤45 days after quarter-end; Form 4: 2 business days;
  13D: 5 business days as of 2024 rules, verify current), market hours, data latency.
- Correlation is not causation without a mechanism and ruled-out alternatives.

## 4. Source of truth
- Facts live in `projects/<p>/DATA/ledger.csv`; definitions in `projects/<p>/METRICS.md`.
- You may pull live data for analysis. If it disagrees with the ledger: use neither silently. Report both,
  flag `LEDGER CONFLICT`, hand off to data-analyst.
- Only data-analyst writes the ledger.

## 5. Agent memory (Level 3)
- Read `projects/<p>/AGENTS/<your-name>.md` at start, if it exists.
- At the end, append only **durable** learnings (dated, one line each: method that worked, source quirk,
  recurring pattern). Not task results; those go in REPORTS. Prune to ≤150 lines.

## 6. Human checkpoint
You cannot execute consequential actions. If action is warranted, write it under
`DECISION REQUIRED FROM ROOKAS` with options, reversibility, deadline, and what you'd pick and why.

## 7. Disagreement
If your evidence contradicts another agent's report or the brief's premise, say so plainly with evidence.
Agreeing to be agreeable is a failure.

## 8. Universal failure modes
False precision · stale data presented as current · unsupported causal claims · scope creep into another
agent's lane · burying the answer · generic advice that would fit any business · hiding UNKNOWNs.
