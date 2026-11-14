# Task: Test search API coverage of older deals

Type: task
Status: open
Blocked by: 71  (Research: Web search APIs for finding a brand's past coverage)
Map: [engine](../map.md)

## Question

Do the usable web search APIs (Mojeek, Brave, DeepSeek Search) find the primary pages for ownership changes from 2015 to 2024, so "Retrieval fan-out, tracked entities and refresh cadence" can decide whether a search API is the route to a brand's past coverage?

## Context

- Created 2026-11-08 at the developer's request, after "Research: Web search APIs for finding a brand's past coverage" found that no vendor documents how far back its index reaches, and that testing it needs an account.
- Usable candidates from that research: Mojeek (£2 per 1,000 with a 1-hour cache, £3 with indefinite storage; AI and commercial use allowed; exact-phrase search not documented) and Brave ($5 per 1,000 with a $5 monthly credit; transient storage only without a storage-rights plan). Exa and Perplexity have unclear storage terms; Google and Bing are out.
- **DeepSeek Search added as a candidate** (developer, 2026-11-13; facts from https://api-docs.deepseek.com/guides/search, https://api-docs.deepseek.com/api/search/ and https://api-docs.deepseek.com/api/fetch):
  - `POST https://api.deepseek.com/v1/tools/search`: $0.75 per 1,000 successful requests (empty results, failures and timeouts are not billed; `count` up to 50 doesn't change the price); no free allowance documented; 100 requests a second per account.
  - Operators: `site:` and `-site:`, exact phrases in quotes, `-` exclusions, `lang:`, and `after:` / `before:` with a year or full date, which suits searching for a 2020 to 2022 deal. No statement on how far back the index goes.
  - Results carry `title`, `url`, `date` (null when unknown), an `authority` score and a `rerank_score`. `snippet` and `summary` are DeepSeek-written text, not the page's words: never evidence. Only the URL matters; the engine fetches the page itself.
  - **Fetch is out.** DeepSeek's Fetch API (`/v1/tools/fetch`, same price, returns Markdown) names no user agent and says nothing about robots.txt, so using it would sidestep the bot rules (own name, robots.txt path by path, stop when asked). The engine's own crawler fetches every result page.
  - **Terms on keeping results: unknown.** The public docs say nothing about storing results, building a database from them, or showing them; platform.deepseek.com (where the terms probably sit) answered 403 to an unauthenticated fetch. This is the question that ruled out Google and limited Brave, so it decides whether DeepSeek Search can be the route.
  - Queries would be brand and owner names sent to a service whose data is stored in China ("Research: Candidate extraction models and hosts"); low sensitivity, but noted.
- Known older deals from the chains audits, with their primary pages:
  - Dental365: The Jordan Company through The Resolute Fund V, July 2021 (Kirkland & Ellis release; dental audit DN17).
  - Lap of Love: Cortec Group Fund VI, closed 2020-01-24 (Cortec Group release; veterinary audit).
  - El Car Wash: Warburg Pincus from affiliates of Wafra, August 2022 (El Car Wash press page; car-wash audit).
  - Further cases may be drawn from `research/category-audit/*.md` rows dated 2015 to 2024.

## Steps

HITL for the account, then AFK:
1. **Developer:** open a free API key for Mojeek and for Brave (free tier or credit; no paid plan), and put the keys where Claude can read them for this test only (for example a local `.env` entry, never committed). For DeepSeek, the key from "Task: Compare extraction models on audit documents" covers it (search costs fractions of a cent here); while logged in to platform.deepseek.com, find what its terms say about storing and displaying search results, and paste or link that text into this ticket.
2. **Claude:** run a few queries per case (brand name; brand name plus "acquired" or "acquisition"; owner name plus brand name), with exact-phrase quoting where supported (and DeepSeek's `after:` / `before:` around the deal date), staying inside the free tiers and each API's terms (results held only as long as the terms allow).
3. **Claude:** record, per API and case, whether the primary page (issuer release, sponsor page, adviser page) appears in the first 10 or 20 results, and note result counts, date filters tried and any exact-phrase behaviour.

## How to resolve

Claude appends `## Answer` with the hit table and a short summary, then adds a context line to "Retrieval fan-out, tracked entities and refresh cadence". No search results are stored beyond what the terms allow; keys are never committed. No branches, commits or pushes.
