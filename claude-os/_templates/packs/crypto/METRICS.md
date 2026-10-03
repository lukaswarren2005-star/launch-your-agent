# METRICS — {{NAME}}
| metric | definition | canonical source | owner |
|---|---|---|---|
| position_weight | position market value / total book value (stocks + crypto + cash) | PORTFOLIO files + timestamped prices | portfolio-risk |
| unrealized_pnl | (price − avg cost) × qty | PORTFOLIO + price | data-analyst |
| book_drawdown | peak-to-trough of total book value | ledger history | portfolio-risk |
| price | last price, with source + timestamp; no market-data feed yet, so web-sourced and possibly stale | [FILL when connected] | data-analyst |
