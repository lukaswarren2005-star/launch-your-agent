---
name: experiment
description: Create, launch, or close a pre-registered experiment in a project (hypothesis, variable, baseline, metric, success threshold, duration, cost, result, verdict). Use for "/experiment new", "/experiment close", "test whether…", or when an agent proposes a test.
---
# /experiment

## new
1. Copy `projects/<p>/EXPERIMENTS/_template.md` → `EXP-###-<slug>.md`; add a row to EXPERIMENTS/README.md.
2. Fill the pre-registration. Hard requirements before status can become `running`:
   - Primary metric exists in METRICS.md; **success threshold is a number**.
   - Baseline cites ledger rows.
   - data-analyst has given a minimum sample/duration (dispatch it).
   - If it costs money: cfo has priced it and ROOKAS approved the budget cap (log via `/decide`).
3. Once running, the pre-registration section is locked. Changes = new experiment.

## close
1. Dispatch data-analyst for the readout against the pre-registered metric and threshold only.
   Secondary "wins" found after the fact are labelled exploratory, not success.
2. Verdict: WIN / LOSS / INCONCLUSIVE (insufficient sample is INCONCLUSIVE, not a soft win).
3. Next action; update the register; durable learning → relevant agent memory (e.g. marketing angle results).

Refuse to declare success without a pre-defined threshold. That rule is the whole point of this skill.
