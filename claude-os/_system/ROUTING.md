# ROUTING
The Master PA picks the **fewest** agents that cover the question. Default ceiling: 4 per round.

## Intent → agents
| Intent (examples) | Agents (parallel unless →) | QA? |
|---|---|---|
| "Why did CAC / revenue / CVR move?" | data-analyst → marketing + cfo | if a spend change is recommended |
| "Should we increase ad spend?" | marketing + data-analyst + cfo | yes |
| "Find a new product / market" | research + marketing + cfo | yes |
| "How do we grow 2x/5x/10x?" | growth + cfo (+ research if a market question) | yes |
| "What are competitors doing?" | research | no |
| "Price change?" | cfo + marketing + data-analyst | yes |
| "Write ads / landing page / email" | copywriter (+ marketing for angle if none exists) | no |
| "Did experiment X work?" | data-analyst | if it'll be scaled |
| "Project status / what's blocked?" | project-pa | no |
| "Weekly report" | `/report weekly <p>` | no |
| "What's [investor] doing / buying?" | filings-intel | no |
| "Analyse [ticker]" | equity-fundamental + technical-quant + news-intel (+ filings-intel if ownership matters) | yes |
| "Find investment opportunities" | filings-intel + equity-fundamental + macro-analyst → portfolio-risk | yes |
| "What's happening with the portfolio?" | portfolio-risk + news-intel (+ macro-analyst on regime shifts) | no |
| "Analyse [token]" | crypto-fundamental + onchain-intel + technical-quant + news-intel | yes |
| "Whale / wallet activity on X" | onchain-intel | no |
| "Should I buy/sell/size X?" | relevant analysts → portfolio-risk | **always** |
| "What's on today?" | Master PA directly (Calendar + TASKS + STATUS) | no |

Not in the table: reason from agent descriptions, state your routing choice in one line, and proceed.

## Protocol
1. Brief every agent with: `project`, question, decision informed, file paths, horizon, "follow `_system/PROTOCOLS.md`".
2. Parallel by default. Sequential (→) only when the downstream agent needs the upstream output; pass the
   **report path**, not your paraphrase.
3. A subagent can't call another subagent. If an agent's HANDOFFS section names a next agent and that
   handoff is warranted, **you** dispatch it.
4. If an agent returns UNKNOWN on something load-bearing, don't paper over it. Either dispatch a
   targeted follow-up or put it in KEY UNCERTAINTIES.

## QA triggers (dispatch `qa-auditor`)
- Recommendation involves money, positions, pricing, or external commitments.
- Any number in the synthesis not traceable to `DATA/ledger.csv` or a cited primary source.
- Agents disagree on a fact (not an interpretation).
- Research-heavy output that will be reused (thesis, competitor map, position timelines).
QA verdict FAIL → back to the originating agent once → second FAIL goes to ROOKAS as an open uncertainty.

## Conflict handling
Present the disagreement, the evidence on each side, the assumptions, the missing information, and the
cheapest evidence that would resolve it. Do not pick a winner unless the evidence clearly does.
