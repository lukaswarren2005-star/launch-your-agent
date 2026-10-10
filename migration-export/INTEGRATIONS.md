# INTEGRATIONS

These were connected to Claude in this session (MCP servers, surfaced by name and tool list only). **No credentials, tokens or config files were read or exported.** Each one needs fresh OAuth on the ChatGPT side.

| Integration | What it does in your stack (from its tool list) | Write powers (approval needed under your rules) | ChatGPT route |
|---|---|---|---|
| **Shopify** | Products, collections, orders, customers, inventory, ShopifyQL analytics, discounts, GraphQL | Create/update products, inventory, discounts, mutations | ChatGPT Shopify app/connector if offered in your region; else a Custom GPT Action against the Admin API (OAuth app) |
| **Higgsfield AI** | Image/video/audio generation, UGC/ads studio, AI influencer, voice, websites, TikTok publish | Generation spends credits; TikTok publish; website deploy | Check whether a Higgsfield ChatGPT app exists. If not, it's manual use in Higgsfield. **Blocks a direct port of `hydre-ugc-video`.** |
| **ElevenLabs** | Voice/speech, image/video flows, conversational agents | Generation spends credits; agent/phone config | Check the ChatGPT app directory, else Actions via the ElevenLabs API |
| **Motion Creative Analytics** | Meta ad creative performance, competitor creatives | Feedback only | Check the app directory, else export reports manually |
| **Windsor.ai** | 350+ data connectors (Meta/Google/TikTok Ads, GA4, Klaviyo, Shopify, Stripe…) **read AND write** | Campaigns, budgets, bids, Klaviyo flows, Amazon listings | Windsor offers an MCP server; ChatGPT supports remote MCP connectors in developer mode. Verify current availability |
| **Gmail** | Search, read, draft, send, label | Send, forward, trash | Built-in ChatGPT Gmail connector |
| **Google Calendar** | Events CRUD, suggest time | Create/update/delete events | Built-in ChatGPT Calendar connector |
| **GitHub** | Repos, PRs, issues, Actions | Push, merge, create repos | Built-in ChatGPT GitHub connector (read) / Codex (write) |
| **Anthropic API** (launch-your-agent only) | Claude Managed Agents | Creates billable agents/sessions/deployments | No ChatGPT equivalent. Stays with Anthropic |

## Setup steps (ChatGPT)
1. ChatGPT → Settings → Apps & Connectors → connect Gmail, Google Calendar, GitHub.
2. For each remaining service, search the app directory first. If it's missing and the service publishes a remote MCP endpoint, add it as a custom connector (developer mode). If it has neither, use a Custom GPT Action with an OpenAPI spec + OAuth.
3. **Gate every write-capable integration.** Your rule: explicit approval before material changes to external systems or money. Windsor.ai (ad budgets) and Shopify (prices/inventory/discounts) are the highest-risk.
4. Revoke the Claude-side grants once ChatGPT is proven: Claude → Settings → Connectors.

## Not observed
- No hooks, MCP config files or custom slash commands of yours were found in this repo.
- The harness's own `~/.claude` hooks (stop-hook scripts) are Anthropic cloud infrastructure, not your config. They were not exported.
