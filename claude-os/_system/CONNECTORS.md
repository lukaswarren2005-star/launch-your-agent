# CONNECTOR MAP
Read = agents may use freely. Write = `ask` in `.claude/settings.json` → ROOKAS approves every call.

| Connector | Status | Read access → agents | Write (approval required) |
|---|---|---|---|
| Shopify | connected | data-analyst, cfo, marketing, growth (orders, products, analytics, inventory) | products, collections, discounts, inventory, GraphQL mutations |
| Windsor.ai | connected | data-analyst, marketing, cfo (Meta/Google/TikTok ads, GA4, Klaviyo, Search Console) | `execute_action` (budgets, bids, ads, audiences, Klaviyo flows) |
| Motion Creative Analytics | connected (Meta only) | marketing, copywriter, research (competitor creative) | none (feedback only) |
| Stripe | **needs authorization** in claude.ai connector settings | cfo, data-analyst once authorized | anything that moves money: never automated |
| Gmail | connected | Master PA, project-pa | send, reply, forward, trash |
| Google Calendar | connected | Master PA, project-pa | create/update/delete/respond |
| SEC EDGAR (WebFetch) | public | filings-intel, equity-fundamental, news-intel | n/a |
| Public crypto APIs (WebFetch: DefiLlama etc.) | public | onchain-intel, crypto-fundamental | n/a |
| Market price data | **missing** | — | — |
| On-chain data provider | **missing** | — | — |

## Gaps worth closing (in order)
1. **Stripe auth**: if a project takes payments there, the CFO is guessing without it.
2. **Market data source** (prices, volume, fundamentals). Until then technical-quant and portfolio-risk run
   on web-sourced, possibly stale prices and must label them so.
3. **On-chain provider**: until then onchain-intel can only use public dashboards/APIs.

## Adding a connector
Add it in claude.ai connector settings (or `claude mcp add` locally), add a row here, add its write tools
to `permissions.ask` in `.claude/settings.json` **before** first use, and list it in the relevant project's
`CLAUDE.md` under Data Sources.
