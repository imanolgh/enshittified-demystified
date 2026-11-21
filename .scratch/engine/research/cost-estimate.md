# Task: Estimate build, seeding and monthly running costs

Ticket: [122-task-estimate-build-and-running-costs](../issues/122-task-estimate-build-and-running-costs.md) · Estimated 2026-11-20 by a background agent · Sources: resolved tickets (cited by name), this project's local Claude Code session transcripts, and vendor pricing pages read on 2026-11-20. No paid API calls were made.

Bottom line: building the product costs about $2,100 to $9,200 in Claude Code usage at Opus 5.5 API list prices, or about $500 to $1,800 in plan fees on a Max or Ultra subscription over the 5 to 9 months the build would take at the pace measured so far. The developer spends about 130 to 370 hours on it. The figure is rough, because no spec exists yet. One seeding pass costs about $1,200 to $9,500: $850 to $7,700 for DeepSeek reads and $360 to $1,760 for Claude list-building and registry research. A typical month at launch costs about $110 to $1,730. Each new prompt or model version adds $850 to $7,700 more, because it re-reads the whole corpus. Most of the spread comes from one ruling: every EDGAR full-text search hit is read whole ("EDGAR full-text search and ownership filings"). That ruling sets most of the seeding cost and most of every version re-read. The planning done so far, measured from the transcripts, came to $746 at Opus 5.5 list prices over 19 active days.

Fetch method note: vendor pages were read with WebFetch on 2026-11-20. Before the first request to each host I read its robots.txt: claude.com, code.claude.com, api-docs.deepseek.com, openrouter.ai, developers.google.com, www.cloudflare.com, developers.cloudflare.com, cloudflare.com (the redirect target of domains.cloudflare.com's robots.txt), www.hetzner.com, www.backblaze.com, www.digitalocean.com, render.com, aws.amazon.com, fly.io, docs.fly.io (the redirect target of fly.io's pricing page) and www.ecb.europa.eu. No disallowed path was fetched. domains.cloudflare.com refused the domain-price page with a plain 403, so I made no further requests to that host. Anthropic's API prices came from its documentation tool. The session transcripts were summed by local scripts in the session scratchpad, without reading them into context.

Sources:
- [ANT-API] Anthropic, Pricing (model, cache, batch and long-context prices): https://platform.claude.com/docs/en/about-claude/pricing, read 2026-11-20
- [ANT-PLANS] Claude plans and pricing: https://claude.com/pricing, read 2026-11-20
- [CC-COSTS] Claude Code, "Manage costs effectively" (enterprise averages, transcript cleanup after 30 days): https://code.claude.com/docs/en/costs, read 2026-11-20
- [DS-PRICE] DeepSeek API, Models and Pricing (peak and off-peak rates, Search API price): https://api-docs.deepseek.com/quick_start/pricing, read 2026-11-20
- [OR-MODEL] OpenRouter, DeepSeek V4.1 Flash 1017 provider prices: https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017, read 2026-11-20
- [OR-FEES] OpenRouter pricing (credit purchase fee): https://openrouter.ai/pricing, read 2026-11-20
- [G-PLACES] Google Maps Platform pricing (Places API SKUs): https://developers.google.com/maps/billing-and-pricing/pricing, read 2026-11-20
- [CF-PAGES-LIM] Cloudflare Pages limits: https://developers.cloudflare.com/pages/platform/limits/, read 2026-11-20
- [CF-PAGES-PRICE] Cloudflare Pages Functions pricing (static asset requests): https://developers.cloudflare.com/pages/functions/pricing/, read 2026-11-20
- [CF-REG] Cloudflare Registrar product page: https://www.cloudflare.com/products/registrar/, read 2026-11-20
- [COM-PRICE] Trade press on Verisign's .com wholesale price from 2026-11-01 (Domain Name Wire, Webhosting.today, Openprovider), found by web search 2026-11-20; the primary Verisign filing was not opened
- [HZ-CLOUD] Hetzner Cloud, Regular Performance plans: https://www.hetzner.com/cloud/regular-performance/, read 2026-11-20
- [B2-PRICE] Backblaze B2 pricing: https://www.backblaze.com/cloud-storage/pricing, read 2026-11-20
- [B2-LOCK] Backblaze B2 Object Lock docs: https://www.backblaze.com/docs/cloud-storage-object-lock, read 2026-11-20
- [DO-DB] DigitalOcean managed databases pricing: https://www.digitalocean.com/pricing/managed-databases, read 2026-11-20
- [DO-DROP] DigitalOcean Droplet pricing: https://www.digitalocean.com/pricing/droplets, read 2026-11-20
- [DO-SPACES] DigitalOcean Spaces pricing: https://www.digitalocean.com/pricing/spaces-object-storage, read 2026-11-20
- [FLY-PRICE] Fly.io pricing: https://docs.fly.io/about/pricing, read 2026-11-20
- [FLY-MPG] Fly.io Managed Postgres plans: https://docs.fly.io/postgres, read 2026-11-20
- [ECB-USD] ECB euro reference rate, USD, 20 November 2026 (1 EUR = 1.0990 USD): https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html, read 2026-11-20

## 1. Prices used

### Anthropic, for Claude Code (build, research, upkeep)

Per million tokens [ANT-API]:

| Model | Input | 5-minute cache write | 1-hour cache write | Cache read | Output |
|---|---|---|---|---|---|
| Claude Opus 5.5 | $4 | $5 | $8 | $0.20 | $20 |
| Claude Sonnet 5.5 | $2 | $2.50 | $4 | $0.10 | $10 |

The Batch API halves input and output prices. It doesn't apply to interactive Claude Code sessions. The prices match what "Extraction execution" recorded on 2026-11-04.

Subscription plans that include Claude Code [ANT-PLANS]: Pro $20 a month ($17 a month billed annually); Max $100 a month ("5x Pro usage" per 5 hours and per week); Ultra $200 a month ("10x Pro usage" per week, no 5-hour limit for verified accounts); Team Standard seat $25 a month ($20 annually); Team Premium seat $125 a month ($100 annually, "5x more usage than standard seats"); Enterprise $20 a seat plus usage at API rates. Anthropic states plan limits as multiples of Pro, never as tokens, so no plan can be converted into a token allowance. Claude Code's docs give enterprise averages of about $13 per developer per active day and $150 to $250 a month, with 90% of users under $30 per active day [CC-COSTS].

### DeepSeek and the fallback (extraction, past coverage)

DeepSeek V4.1 Flash (`deepseek-flash`) per million tokens [DS-PRICE]: input cache hit $0.003 off-peak and $0.006 peak; input cache miss $0.15 off-peak and $0.30 peak; output $0.60 off-peak and $1.20 peak. "Off-peak rates are half of the peak rates." Peak hours are 01:00 to 04:00 and 06:00 to 10:00 UTC, Monday to Friday, excluding Chinese public holidays, which is 35 of 168 hours a week (21%). Weekends and Chinese holidays are off-peak. So off-peak discounts apply to the bulk work that "Extraction execution" Q11 holds for off-peak hours. Single new documents that are read at once are billed at peak about 21% of the time, an average of about 1.21 times the off-peak price. The Search API costs $0.75 per 1,000 successful requests, which matches "Task: Test search API coverage of older deals". From 2026-11-18, search and fetch calls made inside model calls are billed as context tokens. That doesn't apply here, because the engine keeps DeepSeek's tools off.

Fallback (DeepSeek 1017 through OpenRouter) [OR-MODEL]: DeepInfra $0.078 to $0.147 input and $0.235 to $0.441 output; inference.net $0.08 and $0.666; CoreWeave $0.30 and $1.20 per million. OpenRouter adds no markup on inference but takes 5.5% when credits are bought [OR-FEES]. The allowed hosts cost about the same as DeepSeek's own API or less, so an outage doesn't raise the price per read.

### Per-document figures, from measured tickets

- Average read: $0.0044 per document off-peak, $45 to $54 per 10,000 ("Extraction execution"), measured on 157 documents: 98 ordinary pages, 13 portfolio pages and about 30 SEC filings, with whole filings in one request.
- Page versus long filing: "Extraction execution" measured DeepSeek through OpenRouter at $0.037 per long filing (over 100,000 Haiku tokens, 14 of the 157) against $0.0056 per other document, a ratio of about 6.6. Applying that ratio to the $0.0044 average gives about $0.003 per page and about $0.019 per long filing (roughly 60,000 to 140,000 DeepSeek tokens) on DeepSeek's own API off-peak. A token check at today's prices agrees: 100,000 input tokens at $0.15 per million is $0.015, plus about 6,000 to 8,000 output tokens at $0.60 per million, which comes to about $0.019 to $0.020.
- A check of the average against today's token prices (2.43 million DeepSeek input tokens and 0.87 million output tokens per run of 157 documents, research/extraction-model-comparison.md) gives $0.005 to $0.0057 per document, 15 to 30% above the measured $0.0044. The measured figure is used throughout. Treat page costs as about ±30%.
- Large portfolio pages cost more: Leonard Green's page cost about $0.03 off-peak (50,800 output tokens; research/extraction-model-comparison.md).

### Hosting, storage, website and domain

- Hetzner Cloud [HZ-CLOUD], excluding VAT, converted at 1.0990 USD per EUR [ECB-USD]: CPX42 (8 vCPU, 16 GB, 320 GB NVMe, 20 TB traffic) €59.49 in Helsinki; CPX32 (4 vCPU, 8 GB) €30.49 in Helsinki; in the US (Ashburn or Hillsboro), CPX31 (4 vCPU, 8 GB, 160 GB) €62.99 and CPX41 (8 vCPU, 16 GB, 240 GB) €120.99. When the page was read, the plan buttons said "This product is currently unavailable", so availability is a risk. The page shows no backup price.
- DigitalOcean [DO-DB, DO-DROP, DO-SPACES]: managed PostgreSQL 4 GiB / 2 vCPU / 60 to 120 GiB $60.90; 8 GiB / 4 vCPU / 140 to 280 GiB $122.10; extra storage $0.215 per GiB. Valkey (Redis-compatible) 1 GiB $15, 2 GiB $30. Basic Droplets 8 GiB / 4 vCPU $48, 16 GiB / 8 vCPU $96. Spaces costs $5 for 250 GiB, but the page doesn't say whether it supports Object Lock. The PostgreSQL version and standby-node prices aren't listed.
- Fly.io [FLY-PRICE, FLY-MPG]: Managed Postgres Starter (shared-2x, 2 GB) $72, Launch (performance-2x, 8 GB) $282, with high availability and backups included, Postgres 16 or 17, storage $0.28 per GB. Machines: shared-cpu-2x 2 GB $13.39, performance-2x 4 GB $66. Upstash Redis and Tigris prices aren't listed.
- Backblaze B2 [B2-PRICE, B2-LOCK]: $6.95 per TB a month, free egress up to 3 times what is stored, Object Lock through the S3-compatible API in governance and compliance modes "at no extra cost".
- Cloudflare Pages Free [CF-PAGES-LIM, CF-PAGES-PRICE]: "requests to static assets are free and unlimited"; 500 builds a month (the roughly 90 scheduled builds a month from "Website stack and hosting" fit, as that ticket remembered); 20,000 files per site; 25 MiB per file.
- Domain: Cloudflare Registrar charges cost price with no markup [CF-REG] but publishes no price list. Its domain search refused the request (403). Trade press reports Verisign's .com wholesale price at about $10.97 from 2026-11-01, plus the $0.20 ICANN fee, so about $11.17 a year [COM-PRICE].
- Google Places [G-PLACES]: Text Search Essentials (IDs only) is free and unlimited; Place Details Pro $17 per 1,000 after 5,000 free a month; Text Search Pro $32 per 1,000 after 5,000 free.

## 2. Measured planning sessions

Local Claude Code transcripts for this project: 13 main session files (one with no model calls) and 70 subagent transcripts in the sessions' folders. They hold 9,343 model calls from 2026-10-17 to 2026-11-21 UTC (2026-11-20 local), over 19 active days. Every call ran on `claude-opus-5-5`, apart from a few thousand tokens on Haiku 5.5. Claude Code deletes session files older than 30 days by default [CC-COSTS], so planning before mid-October (the project's docs go back to 2026-08-31) isn't measured. The figures below are a floor.

Planning totals, excluding the session that ran this estimate:

| | Tokens | At Opus 5.5 list price |
|---|---|---|
| Input (uncached) | 19,456 | $0.08 |
| Output (thinking included) | 9,415,740 | $188.31 |
| Cache writes (5-minute 18,689,262; 1-hour 10,888,696) | 29,577,958 | $180.56 |
| Cache reads | 1,882,954,779 | $376.59 |
| Total | 1.92 billion | $745.54 |

This session added $11.42 by the time it was summed. At Sonnet 5.5 prices the planning would have cost about half, $373.

Largest sessions, subagents included, at Opus 5.5 list price:

| Session | Dates (UTC) | Subagents | Cost | Contains |
|---|---|---|---|---|
| 4ec801bb | 2026-11-05 to 11-08 | 15 | $214 | the full category audit (chains 66: 10 workers, $120) and grilling |
| 02bcbe8a | 2026-11-17 to 11-19 | 11 | $157 | the product-industry, screen and follow-up audits (chains 91, 92, 93: 11 workers, $104) |
| 203f5672 | 2026-11-15 to 11-17 | 15 | $136 | research workers and grilling |
| 99c9d4d8 | 2026-11-11 to 11-14 | 7 | $82 | research workers and grilling |
| 41ac58d7 | 2026-11-05 | 5 | $47 | research workers |

Two unit figures come out of this:

- One active planning day averaged about 100 million tokens processed: about 0.5 million output, 1.6 million cache writes and 99 million cache reads. That cost $39 at Opus 5.5 list price, $15 in the main conversations and $24 in subagents. The day is above the enterprise 90th percentile in [CC-COSTS], because of the research workers.
- Research tickets record "harness" token counts, the total the agent tool reports. Matching worker transcripts to tickets gives the dollar value of those counts: chains 66, 3,419,427 tokens, $119.63 ($35 per million); chains 91 and 92, about 2.31 million, $66.10 ($29 per million); chains 93, 1,371,017, $37.85 ($28 per million). So $28 to $35 per million harness tokens at Opus 5.5 list prices. By that rate chains 82 (about 2.72 million) cost about $76 to $95.

## 3. Build

Claude writes all of the code from the spec (CLAUDE.md role contract), so the build is Claude Code usage plus the developer's hours. No spec exists, so the parts below follow the docs as they stand. Each part is sized in active build days, and each day has the same token mix as a measured planning day (about 100 million tokens, about 0.5 million of them output). A build day is priced at $25 (lighter, mostly main-conversation work) to $60 (heavy subagent use for tests, fixtures and live lookups) at Opus 5.5 list prices, around the measured $39. The days include the definition of done in CLAUDE.md: 2 or 3 real fixture files per connector, one live lookup recorded in the ticket, and for BDC parsing an automatic cross-check against the SEC's BDC data set.

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| Planning to date (sunk, measured) | $746 | $746 | Transcript sum, 2026-10-17 to 2026-11-20, at Opus 5.5 list price | Section 2; [ANT-API] |
| Remaining decisions and the wayfinder spec | $250 | $1,200 | 24 open tickets (engine 19, 23, 29, 38, 40, 41, 42, 43, 44, 45, 46, 63, 69, 74, 106, 118, 119; chains 61, 62, 72, 94, 105, 109, 117) plus the spec: 10 to 20 active days × $25 to $60 | ticket list; Section 2 |
| Foundation: app factory, config, logging, Docker images for api, workers, beat, flower and Playwright, CI, missing dependencies | $50 | $240 | 2 to 4 days | "Hosting, storage and deployment" context; CLAUDE.md layout |
| Schema and migrations: 27 tables in §4 plus `api_costs`, events, alerts, demand log and report submissions; CHECK constraints from StrEnums with a drift test | $100 | $420 | 4 to 7 days | `docs/evidence_layer_plan.md` §4 |
| Contracts, the claims door, claim identity, document storage and fetch log, `verify_citations` | $150 | $600 | 6 to 10 days | "Claim producers and the claims door", "Claim identity", "Document storage, fetch log and last-confirmed", "ExtractedClaim and the extraction result envelope", "Citation verification rules" (open) |
| Resolution, scoring, edges and categories: entity resolution, source independence, conflict and succession, edge lifecycle, category precedence and recompute with the nightly drift check, events, funds and firms, the PE-firm test | $250 | $1,080 | 10 to 18 days | engine 19, 24 to 29, 65, 68, 120 |
| Extraction: DeepSeek client, windows, retries, fallback and `api_incidents`, `extraction_requests`, cost rows, golden fixtures and the weekly check | $100 | $480 | 4 to 8 days | "Extraction execution", "Extraction prompt rules" |
| Shared fetcher: robots.txt per host including redirect targets, per-domain token buckets, Playwright request routing, `site_access`, the challenge retry | $100 | $420 | 4 to 7 days | "Rosters, portfolio pages and the registry"; "Operational identity" context (proposed fetcher) |
| Registry crawler and selector producers: registry sync, paging, detail pages, status-only selectors, gap report | $150 | $600 | 6 to 10 days | "Rosters, portfolio pages and the registry"; "Selector producers" (open) |
| EDGAR full-text search, the 13D/13G parser, press feeds | $150 | $600 | 6 to 10 days | "EDGAR full-text search and ownership filings"; "Press and EDGAR full-text connectors" |
| Form ADV monthly files, FOIA archive, IAPD PDF parser, IRS exempt-org | $75 | $360 | 3 to 6 days | "Form ADV and IRS exempt-org ingestion" |
| BDC discovery, Schedule of Investments parser, cross-check against the SEC BDC data set | $200 | $900 | 8 to 15 days, the hardest connector by the docs (hidden identifiers, joint-venture schedules) | "BDC discovery and Schedule of Investments parsing"; research/bdc-filing-facts.md |
| DeepSeek Search connector | $50 | $180 | 2 to 3 days | "Past coverage through DeepSeek Search" (open) |
| Celery chains and Beat schedules | $75 | $360 | 3 to 6 days | "Celery topology" (open); "Refresh schedule" (open) |
| Read API, operator surface, search and demand log, report form, graph endpoint | $150 | $600 | 6 to 10 days | engine 39, 40, 41, 69; chains 59 |
| Website: Astro pages, share cards with satori, OpenAPI types, how-this-works page | $150 | $720 | 6 to 12 days | chains "Website stack and hosting", "Website pages and shareable cards" |
| Operations: deploy, backups and a restore drill, alerts, monitoring | $75 | $360 | 3 to 6 days | "Hosting, storage and deployment" and "Operational identity" (both open) |
| Model test spend during the build (golden runs, prompt checks, live lookups) | $10 | $50 | Earlier test spend: about $24 on OpenRouter and $1.40 on DeepSeek in "Extraction execution", $2.27 for the p9 check | "Extraction execution"; research/extraction-model-comparison.md |
| Build total at Opus 5.5 API list prices, excluding the sunk planning | $2,085 | $9,170 | 83 to 152 active days (10 to 20 remaining planning, 73 to 132 build) | sum of the rows above |
| The same at Sonnet 5.5 prices | about $1,050 | about $4,600 | Sonnet 5.5's prices are half of Opus 5.5's in every column | [ANT-API] |
| On a Max plan ($100 a month) | $500 | $900 | 83 to 152 active days at the measured pace (19 active days in 35 calendar days, about 3.8 a week) is 22 to 40 weeks, about 5 to 9 months. Plan fees only; add the $10 to $50 model test spend. | [ANT-PLANS]; Section 2 |
| On an Ultra plan ($200 a month) | $1,000 | $1,800 | The same months × $200, plan fees only | [ANT-PLANS] |
| Developer hours | 130 h | 370 h | Remaining grilling and spec review 25 to 60 h; reviewing and committing build work 1 to 1.5 h per active build day, 73 to 198 h; approving registry entries by commit, 1,450 to 1,950 entries at 1 to 2.5 minutes, 24 to 81 h; operating the seeding pass (alerts, operator report) 10 to 30 h | CLAUDE.md definition of done; "Rosters, portfolio pages and the registry" (developer commits each entry) |

Whether the build fits within a plan's limits can't be computed, because Anthropic publishes the limits only as multiples of Pro. The measured planning ran at about $640 of API-equivalent usage per 30 days. If that work stayed within the developer's current plan, a build at the same daily intensity should too. The plan's `/usage` bars during planning are the only real check.

How rough this is: the build figure is the least certain of the three. It rests on two assumptions that nothing has measured: how many active days each part takes, and that a build day costs about what a planning day did. Either could be off by a factor of two in either direction. The 73-to-132-day total also counts parts whose designs are still open (resolution, citation rules, Celery, API conventions, testing). Section 8 lists what would sharpen it.

## 4. One seeding pass

Brands: 37 launch industries at 30 brands per list where 30 exist, about 1,100 brands ("Launch industries", amended; "Brand-level checked"). The extra batch of PE-owned brands outside the launch industries ("Category brand lists and checked") has never been counted. I assume 50 to 150 brands, from the out-of-scope clusters in chains research/pe-consumer-scan.md (packaged food 40, beverages 16, casinos and others). That makes 1,150 to 1,250 brands. Under "Retrieval fan-out, tracked entities and refresh cadence", full-text search also runs for every tracked company. I assume 0.6 to 1.0 tracked companies per brand (700 to 1,250) and 1.2 to 1.5 names per entity (brand, company, aliases), which gives 2,200 to 3,750 distinct queries. Bulk work runs off-peak ("Extraction execution" Q11). If it ran at peak, every DeepSeek line would double.

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| EDGAR full-text search, first run since 2001, every hit read whole | $600 | $5,625 | 2,200 to 3,750 queries × 40 to 80 hits on average (cap 100) × 70 to 75% unique after overlap between names = 60,000 to 225,000 filings. Each filing costs $0.010 (low: BDC filings dropped by filer before reading, as ticket 70 leaves them to the BDC parser, so half the hits are short exhibits, 8-Ks and 10-Qs) to $0.025 (high: most hits are long, including landlords' 10-Ks and mortgage-pool prospectuses read in several windows). | "EDGAR full-text search and ownership filings"; "Retrieval fan-out" (hit counts: Aspen Dental 2,095, Natrol 1,543, MB2 Dental 1,408; Lap of Love 0); per-filing cost from Section 1 |
| DeepSeek Search queries | $3 | $5 | 3,450 queries (3 per brand, ticket 118's figure) to 6,250 (5 per brand, adding owner-plus-brand queries) at $0.75 per 1,000 | "Past coverage through DeepSeek Search" (open); [DS-PRICE] |
| DeepSeek Search results fetched and read | $52 | $550 | 5 results kept per query after filtering (low) to all 20 (ticket 118's upper case), at $0.003 to $0.0044 per page. Ticket 118's own $120 used the older $0.0018 per page. | ticket 118 (open); "Extraction execution" |
| Newsroom first crawls (whole archives) | $135 | $660 | 45,000 releases (ticket 30's rough size: 150 entries × 300 releases) to 150,000 (500 newsrooms × 300, since each listed brand's own newsroom is also an entry), at $0.003 to $0.0044 | "Rosters, portfolio pages and the registry"; "Operational identity" context |
| Portfolio, about and detail pages (registry pass) | $30 | $154 | 10,000 to 35,000 pages (150 to 300 firms with detail pages, about 100 for a large firm, plus about pages), at $0.003 to $0.0044. Large portfolio pages cost up to about $0.03 each but are few. | ticket 30; "Refresh schedule" context (a 100-page firm) |
| Brand websites (about and product pages) | $7 | $33 | 1,150 to 1,250 brands × 2 to 6 pages, at $0.003 to $0.0044. Rests on chains 94 adding the brand's own site as a required source. | "Licensed names in v1" request on "Brand-level checked" (open) |
| BDC 10-K Item 1 reads | $2 | $5 | About 187 10-Ks a year × 3 to 4 years of the one-time load = 560 to 750 sections, at $0.003 to $0.006 | "BDC discovery and Schedule of Investments parsing" |
| Code parsers: Form ADV monthly files and FOIA archive, IAPD PDFs, about 2,400 BDC Schedules, 13D and 13G | $0 | $0 | No LLM; fetching is free and runs within the SEC's 10 requests a second | tickets 34, 36, 70 |
| Retries, the daily `unreadable` sweep, portfolio-page re-reads | $25 | $703 | 3 to 10% on top of the reading rows above | "Extraction execution" Q5 and Q13 |
| DeepSeek subtotal | $854 | $7,735 | | |
| List-building (ranking-only workers) | $34 | $56 | 1.2 to 1.6 million harness tokens × $28 to $35 per million | "Category brand lists and checked"; Section 2 |
| Registry research (Claude writes the YAML entries) | $325 | $1,700 | 1,450 to 1,950 entries (each listed brand plus 300 to 700 owners with a portfolio page, newsroom or about page) × 8,000 to 25,000 harness tokens each × $28 to $35 per million. No ticket has measured this. | ticket 30 (launch target); Section 2 |
| Seeding total | $1,213 | $9,491 | | |

The two Claude rows can run on a subscription instead, inside its plan fee. The pass needs no extra host. At the SEC's 10 requests a second, 225,000 filings take hours to fetch. DeepSeek allows 2,500 concurrent requests [DS-PRICE], and at a 13-second median answer ("Extraction execution") 50 parallel reads clear 225,000 documents in under a day. Newsroom crawls at 10-second crawl delays run in parallel across domains and take a day or two.

One contingency stays outside the total. Engine 106 "Task: Draft prompt p10" is open. If p10 or any later version ships after the seeding pass, the whole corpus is re-read for another $850 to $7,700 ("Extraction execution" Q7). Seeding after the prompt is final avoids paying that twice.

## 5. A typical month at launch

| Item | Low | High | How it was derived | Source |
|---|---|---|---|---|
| New EDGAR filings for tracked names | $11 | $227 | 2,200 to 3,750 names × 0.5 to 2 new hits a month = 1,100 to 7,500 filings × $0.010 to $0.025, times up to 1.21 if refreshes run at once instead of off-peak. Cadence open. | ticket 70; "Refresh schedule" (open); [DS-PRICE] |
| New newsroom releases | $1 | $27 | 150 to 500 newsrooms × 3 to 10 releases a month, at $0.003 to $0.0044, times up to 1.21 | ticket 30 |
| Wire-feed matches stored from the issuer's site | $1 | $5 | 200 to 1,000 releases a month at page prices. Unmeasured. | "Press and EDGAR full-text connectors" |
| Present-tense pages whose text changed since the last pass | $3 | $339 | 12,300 to 42,500 pages (registry plus brand sites) × 4 to 30 passes a month × 2 to 5% changing per pass = 984 to 63,750 re-reads, at $0.003 to $0.0044, times up to 1.21. Pass cadence is open and the change rate is unmeasured. | "Document storage, fetch log and last-confirmed" (only a text change triggers a read); "Refresh schedule" (open) |
| DeepSeek Search re-runs | $1 | $185 | Low: runs only when a new owner appears. High: a full quarterly re-run of the seeding search rows ($555 a quarter). | ticket 118 (open) |
| New brands added to the lists | $6 | $247 | 10 to 50 brands a month × each brand's own first run ($0.57 to $4.94: EDGAR plus search, from Section 4 divided by brand count). The rate is unset. | "Category brand lists and checked" (lists only grow) |
| Weekly golden-document check | $0 | $3 | 20 to 157 documents × 4.3 weeks × $0.0044 | "Extraction execution" |
| Search help from DeepSeek | $0 | $36 | Low: string matching or a local embedding model. High: DeepSeek reads each query, at about $0.00036 per query at peak prices (about 600 input and 150 output tokens), for 100,000 searches. Traffic is unknown. | "Search and the demand log" (open); [DS-PRICE] |
| OpenRouter fallback during outages | $0 | $5 | Outages only; the allowed hosts cost no more than DeepSeek; 5.5% fee on credits | "Extraction prompt rules"; [OR-MODEL]; [OR-FEES] |
| Google Places | $0 | $0 | Not used for brands in v1. IDs-only Text Search is free and unlimited if the demand log ever uses it. | "Operational identity" context; [G-PLACES] |
| Model and API subtotal | $23 | $1,074 | | |
| Hosting: API, workers with Playwright, Beat, Postgres 16, Redis | $65 | $450 | Low: Hetzner, one CPX42 in Helsinki (€59.49), self-managed compose. Middle: DigitalOcean, $124 to $248 (managed PostgreSQL 4 to 8 GiB, Valkey 1 to 2 GiB, one 8 to 16 GiB Droplet). High: Fly.io, Managed Postgres Launch $282 plus 80 GB storage $22, two performance-2x machines $132 and one shared-cpu-2x $13, without Redis, whose price isn't listed. Hetzner in the US with two boxes (CPX41 plus CPX31) is $202. | "Hosting, storage and deployment" (open); [HZ-CLOUD], [DO-DB], [DO-DROP], [FLY-MPG], [FLY-PRICE], [ECB-USD] |
| Object storage with Object Lock, plus database backups | $1 | $5 | 0.1 to 0.7 TB on Backblaze B2 at $6.95 per TB: raw documents (EDGAR files, about 0.5 to 1.5 MB each), raw extraction responses kept for good, and Postgres dumps | "Document storage, fetch log and last-confirmed"; "Extraction execution" Q8; [B2-PRICE], [B2-LOCK] |
| Cloudflare Pages | $0 | $0 | Static requests free and unlimited; about 90 builds a month against 500; about 2,500 to 6,000 files against 20,000 | "Website stack and hosting"; [CF-PAGES-LIM], [CF-PAGES-PRICE] |
| Domain | $1 | $1 | About $11.17 a year for .com at cost | "Site name and domain" (open); [CF-REG], [COM-PRICE] |
| Monitoring, error tracking, CI | $0 | $0 | Flower, JSON logs and email alerts on the host. A paid error tracker and CI minutes weren't priced. | "Operational identity" (open) |
| Claude Code upkeep (connector fixes when sources change shape, operator batches, registry gaps) | $20 | $200 | A Pro to Ultra plan fee. At API prices, 3 to 12 active days a month × $25 to $60 would be $75 to $720. | [ANT-PLANS]; Section 2 |
| Monthly total, excluding version re-reads | $110 | $1,730 | | |
| Each new prompt or model version | $850 | $7,700 | Re-reads every document older versions read, about the size of the seeding pass's DeepSeek subtotal, growing with the corpus. A silent weight change behind `deepseek-flash` is not a new version and costs nothing. | "Extraction execution" Q6 and Q7 |

## 6. The stale figures this replaces

"Operational identity, budgets and guardrail values" (2026-11-04) budgeted about $120 to $240 per seeding pass of about 1,000 brands and $20 to $120 a month, on Claude batch pricing at about six documents per brand. DeepSeek is cheaper per document ($0.0044 against $0.02 to $0.04 on Sonnet or Opus in batch). Even so, the new figures are higher, for three reasons decided after 2026-11-04: every full-text search hit is read whole, up to 100 hits per name, for brands and companies alike; newsroom archives are read in full on the first crawl (45,000 or more reads); and a new version re-reads everything.

## 7. Assumptions and open dependencies

Figures that rest on open tickets, so the estimate can be re-run when each settles:

- Chains 94 "Brand-level checked: required sources and freshness": the brand-website row (seeding $7 to $33), whether owners' sources are on a brand's required list, and therefore how many company names full-text search must finish before a brand counts as checked.
- Engine 119 "Refresh schedule and next-check date": every monthly cadence. That covers registry passes (4 to 30 a month assumed), EDGAR refreshes, DeepSeek Search re-runs and the pending-deal pace. It moves the changed-pages row ($3 to $339), the EDGAR row ($11 to $227) and the search row ($1 to $185).
- Engine 43 "Hosting, storage and deployment": the hosting row ($65 to $450), the storage row, backups and monitoring.
- Chains 117 "Site name and domain": the domain row, about $11 a year for .com. Other extensions cost more.
- Also open, and they move the numbers: engine 118 "Past coverage through DeepSeek Search" (results fetched per query and re-run cadence: seeding $52 to $550); engine 42 "Operational identity" (whether to budget full-text search noise or reopen the read-everything ruling, the newsroom first-crawl cap, the hop cap); engine 106 (p10's timing against the seeding pass); engine 40 (search method); chains 105 (USPTO access, assumed free).

Assumptions no ticket has measured:

- The extra batch of brands outside launch industries (50 to 150), tracked companies per brand (0.6 to 1.0) and names per entity (1.2 to 1.5).
- Average full-text search hits per query (40 to 80), overlap between names, and the size mix of hit documents. These three set the largest single row.
- Newsroom count (150 to 500) and archive depth (300 releases each, ticket 30's rough figure).
- How often present-tense pages change their extracted text between passes (2 to 5%). Pages with news widgets or dates in their text would be re-read on every pass.
- Registry research tokens per entry (8,000 to 25,000).
- New brands per month (10 to 50) and search traffic (up to 100,000 searches a month).
- Build days per part, and that a build day costs what a planning day did.
- The EUR to USD rate (ECB, 2026-11-20) for Hetzner; VAT is excluded throughout.

Vendor pages that couldn't be read or didn't give the figure:

- Cloudflare's domain search (domains.cloudflare.com) refused the request with a 403, so I stopped using that host. The .com price comes from trade press.
- AWS RDS pricing loads its figures by script, so nothing could be read. Render's pricing page gave no figures in its text. Both were dropped as hosting options.
- Not stated on the pages read: Hetzner backup pricing, DigitalOcean standby-node prices and whether Spaces supports Object Lock (B2 is paired with every option instead), Fly's Upstash Redis and Tigris prices, and Cloudflare's Workers Paid price.
- DeepSeek's page doesn't say whether thinking tokens are billed as output. The measured per-document cost already includes them.

## 8. What would sharpen each estimate

- Build: the wayfinder spec, with its parts list and acceptance bars. Then time one connector end to end (Form ADV is small and self-contained) and sum its transcript tokens with the same script. That replaces the assumed $25 to $60 per day and the days per part with a measured unit. The developer's `/usage` bars during that build show whether the current plan holds.
- Seeding: a free count-only dry run of EDGAR full-text search for all 2,200 to 3,750 names (hit totals and the form and filer mix, no reads), plus token sizes for a sample of about 100 hits. That fixes the largest row. Also a registry-research pilot of about 20 entries with its harness tokens recorded, newsroom archive sizes from the first registry entries, and the extra-batch brand count.
- Monthly: decide engine 119's cadences, then measure the text-change rate over two consecutive registry passes on the first registry entries. Ticket 118's fetch filter fixes the search rows, and ticket 43's choice fixes hosting. Search traffic and new brands per month can only be measured after launch, from the demand log.

## 9. Revised for "Cost cuts before revenue" (2026-11-21)

Engine "Cost cuts before revenue" (ticket 124) changed several rules this estimate assumed. This section re-prices the seeding and monthly tables under the new rules, then sets out the research behind each cut and what it gives up. The build section doesn't change: on the developer's $100 Max plan the build is plan months, not API dollars.

The new rules, in short:

- EDGAR full-text search: a hit is read whole only when the brand's own company or one of its tracked owners filed it; every other hit is read as windows of about 8,000 characters around each mention of the name, plus the cover page. 10-Qs from the brand's company or owners are read only when filed after the latest 10-K.
- Newsrooms: every release is still read.
- A new prompt or model version reads new documents only; re-reads are an operator choice; seeding waits for p10.
- No timers before revenue: every recurring job is a step of one operator command, the pass.
- The engine runs on the developer's machine; the static site goes to Cloudflare Pages (free); search is built into the site; the report form is a small free Cloudflare function.

### One seeding pass, revised

Prices: own-side whole reads at $0.003 to $0.005 for an 8-K and $0.019 to $0.030 for a long filing; windowed reads at $0.003 (short filings, no saving) to $0.0073 (long filings), from measurement 2 below; pages at $0.00136 (measured on releases) to $0.003; releases at $0.00136.

| Item | Before | Revised | How it was derived |
|---|---|---|---|
| EDGAR full-text search | $600 to $5,625 | $290 to $1,970 | The same 60,000 to 225,000 hits. Leaving out BDC filers, 38% come from the brand's company or owners, read whole; dropping their older 10-Qs (about 18% of them) leaves 31% of hits read whole, averaging $0.0095 to $0.0136 (about two thirds short 8-Ks, a third long filings). The other 62% are read as windows at $0.003 to $0.0073 |
| DeepSeek Search queries | $3 to $5 | $3 to $5 | Unchanged |
| DeepSeek Search results read | $52 to $550 | $23 to $375 | 17,250 to 125,000 results at $0.00136 to $0.003. How many results a query keeps is still open ("Past coverage through DeepSeek Search") |
| Newsroom first crawls | $135 to $660 | $61 to $204 | 45,000 to 150,000 releases at the measured $0.00136 |
| Portfolio, about and detail pages | $30 to $154 | $14 to $105 | 10,000 to 35,000 pages at $0.00136 to $0.003 |
| Brand websites | $7 to $33 | $3 to $23 | 2,300 to 7,500 pages at $0.00136 to $0.003 |
| BDC 10-K Item 1 reads | $2 to $5 | $2 to $5 | Unchanged |
| Retries | $25 to $703 | $12 to $269 | 3 to 10% |
| DeepSeek subtotal | $854 to $7,735 | $410 to $2,960 | |
| List-building and registry research | plan time | plan time | Inside the Max plan |

This replaces the rough "$400 to $3,700" given when ticket 124 was decided; that figure counted the windows but not the 10-Q rule or the measured page price.

### Between passes and per pass, revised

| Item | Before (a typical month) | Revised |
|---|---|---|
| Hosting | $65 to $450 | $0: the engine runs on the developer's machine |
| Website on Cloudflare Pages | $0 | $0: the chains site's 2,500 to 6,000 files fit the free plan |
| Report function | n/a | $0 on Cloudflare's free tier (limits to be checked in "Hosting, storage and deployment") |
| Domain | $1 | $1 |
| Backups (Backblaze B2) | $1 to $5 | $0 to $1 |
| Claude Code upkeep | $20 to $200 | inside the Max plan |
| A month with no pass | $110 to $1,730 | about $1 to $2 |
| A "new deals" pass, when run | n/a | about $2 to $25: wire feeds, new newsroom releases and new deal-type EDGAR filings for tracked names |
| A full routine pass, per month since the last one | n/a | about $7 to $120: every new EDGAR filing (windowed where third party), new releases and changed pages |
| A prompt or model version | $850 to $7,700 | $0 unless a re-read is chosen; a full re-read would cost about the revised DeepSeek subtotal, $410 to $2,960 |

### The research behind the cuts

Four measurements, all on 2026-11-20 and 2026-11-21, with $1.37 of DeepSeek in total:

1. Where SEC filings state ownership (`.scratch/engine/research/edgar-quote-distance.md`, code only). In 33 SEC filings from the extraction tests, all filed by the brand's company, its owner or as deal filings, DeepSeek's whole reads found 677 facts. 84% of quotes contain the subject's name and 98% sit within about 2,000 tokens of it. The 12 far facts (2%, in 5 filings) are all a company describing its own controlling owner as "we" or "our Principal Stockholder" (Petco: "We are currently indirectly controlled by certain funds (the "CVC Funds")"; Mister Car Wash: "LGP has more than 50% of the voting power"; Chewy; Unilever on TMICC).
2. Windows on third-party filings (`.scratch/engine/research/edgar-third-party-windows.md`, $1.13). 10 brands, 2,274 full-text hits: 664 from the brand's company or an owner, 566 deal-type, 532 third party, 512 BDC. 44 third-party filings were read by hand and by DeepSeek, whole and as windows. 7 of 44 (16%) state an owner of the brand and 3 (7%) an investor in its company (KKR and Ontario Teachers' for Heartland Dental in a mortgage-pool prospectus, Align's stake in Heartland's holding company, Sentinel as MB2 Dental's former owner); none of 14 landlord or 3 lender filings does. Every statement sits within 391 characters of a brand mention. Windowed reads missed no brand fact a whole read found (0 of 44); whole reads found 13 brand facts and windowed reads 19, a gap about the size of two reads of the same text. Cost per read $0.0200 whole against $0.0057 windowed; long filings $0.030 against $0.0073. 299 of the 566 deal-type hits came from landlords, REITs and mortgage trusts.
3. Older 10-Qs (`.scratch/engine/research/ten-q-deals-missing-from-ten-k.md`, code plus reading). In two test pairs (Chewy, Tractor Supply), a 10-Q's only new ownership facts were the quarter's acquisitions (Modern Animal, VIP Petcare). Across 22 consumer companies, 734 10-Qs and 261 10-Ks from 2015 to 2026, about 420 real deals were named in 10-Qs, and the next 10-K named all but one (about 0.2%): Driven Brands' Clearwater Car Wash, about $24 million, folded into "All Other Car Wash", with no 8-K or press release naming it. No brand bought and sold within a year went missing (Hershey's Tyrrells is in the 10-K). Smucker and Clorox restate deals only in the 10-K's Exhibit 13 or 99.1.
4. Newsroom first-crawl filter (`.scratch/engine/research/newsroom-filter-test.md`, $0.24). 176 releases from Blackstone, TSG Consumer, Serta Simmons Bedding, Pharmavite and Ocean State Job Lot, plus 171 known releases from the research. 37 of the 97 fact-yielding releases state ownership only in the closing About paragraph. The best filters skipped 6% to 25% of releases while losing 3% to 12% of ownership pairs. A release cost $0.00136.

### What each cut gives up, and how much it matters

**1. Third-party EDGAR filings read as windows** (Q1).

- Evidence: measurements 1 and 2. A company's own filings stay whole reads because that's where the 2% of far facts sit.
- What could be missed:
  - An ownership statement in a third-party filing far from every mention of the name. None was found in 44 filings, but only 9 of them held any brand fact, so the sample bounds the miss rate only loosely: up to about 7% of third-party filings, or about a third of the fact-bearing ones, at 95% confidence.
  - Facts about other companies named in those filings. Whole reads returned 631 such facts against 290 for windows, mostly the filer's own structure (a landlord's subsidiaries). A company the engine tracks has its own searches and its own filings read whole; the loss is incidental facts about companies nobody tracks.
  - Statements that use a name the engine doesn't know (an abbreviation such as "TMICC" or a defined term). Windows only open around names the engine searches for.
- How much it matters: low. Third-party filings rarely state who owns a brand (7% name an investor), and those facts usually also appear on the owner's portfolio page or in a release. Their extra value is as an official source that verifies a fact alone, and windows kept every such statement in the test.

**2. 10-Qs older than the filer's latest 10-K skipped** (Q7).

- Evidence: measurement 3.
- What could be missed: a deal named only in an old 10-Q (about 1 in 420, mostly small purchases folded into a larger line in the 10-K); a quarter-level date where the 10-K gives only the year (10-Ks usually give the date). 10-Qs filed since the latest 10-K are still read, so recent deals are kept.
- How much it matters: very low for brand ownership. The one miss in the sample was a roll-up's purchase of a few sites, not a brand changing hands.

**3. No automatic re-read when the prompt or model changes** (Q4).

- Evidence: the cost alone. A full re-read costs about as much as the seeding pass's DeepSeek reads.
- What could be missed: improvements a new prompt version brings (a fixed false claim, a newly caught fact) reach only new documents until the developer chooses a re-read. Facts from two approved versions sit side by side. A document that produced no facts under the old version is never looked at again unless a broad re-read runs.
- How much it matters: low to moderate. Every version passes the same approval check before it ships (known facts, exact quotes, blind precision, no rule breaks; "Extraction prompt rules"), so older facts met the bar of their day. A known kind of error can be fixed with a targeted re-read of the documents that produced it. Seeding waits for p10 so the first pass uses the newest approved prompt.

**4. No timers before revenue: one operator pass** (Q5, Q9).

- Evidence: none needed; it's a choice about when money is spent.
- What could be missed: freshness. Between passes nothing updates:
  - a sale or exit isn't reflected, so a card can show a former owner as current until the next pass, and a new PE purchase doesn't appear;
  - the deal feed shows nothing new;
  - pending deals don't close in the data;
  - failed reads wait for the next pass, so a brand can stay "not yet checked" longer;
  - the drift check and the golden check (a silent model change) run only at pass time.
- How much it matters: moderate, and it grows with the gap between passes. Cards show "checked {date}", so readers can see the age; after 18 months without confirmation a hop shows "No source has shown this since…". The cheap "new deals" pass (wire feeds, new releases, new deal-type EDGAR filings, roughly $2 to $25) is the mitigation; run regularly, it keeps sales and purchases current.

**5. The engine on the developer's machine, static search, a free report function** (Q6).

- Evidence: none needed; it's a choice about hosting.
- What could be missed:
  - search quality: matching on names, owners and industry words only, with no meaning-based ranking;
  - the demand log (searches that found nothing), unless the small Cloudflare function records them;
  - updates when the machine is off or fails. The website itself stays up, since it's static on Cloudflare.
- How much it matters: low for v1, since people look brands up by name. The operational risk of one machine is real; backups (Backblaze B2 with Object Lock) cover the data. Fetching from a home connection is not a loss: research found 90 of 93 PE firm sites readable from a home IP ("Rosters, portfolio pages and the registry").

**6. SEC headers from the first request** (Q8). No data trade-off. If the SEC still refuses, the engine stops SEC requests instead of retrying, and EDGAR facts wait until it's resolved.

**Considered and rejected: a newsroom first-crawl filter** (Q3). Measurement 4 showed every filter that skipped a meaningful share of releases lost 3% to 12% of ownership pairs, mostly facts in About paragraphs, people and charity releases, and deals worded "sell", "purchased" or "invests". At $0.00136 a release, the best filter would have saved about $15 to $50. Every release is still read.
