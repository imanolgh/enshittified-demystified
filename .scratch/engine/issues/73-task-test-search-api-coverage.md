# Task: Test search API coverage of older deals

Type: task
Status: resolved
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

## Comments

**2026-11-19, Claude: claimed; DeepSeek half run, Mojeek and Brave waiting on keys.**

- **DeepSeek terms.** The public [Open Platform Terms of Service](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html) (released 2026-04-22, effective 2026-04-29) say nothing about search results. They define "Output" as content the model generates from Input, and §4.2 assigns the rights in Outputs to the customer for "a wide range of use cases, including … derivative product development". The search guide is silent on storage too. Whether results may be stored or shown stays open. The developer chose to run the test anyway (2026-11-19), because it stores nothing from the results.
- **Search also returns page text.** `need_content: true` on the Search API returns the page content, which would get around the bot rules just as Fetch does. The test sent `need_content: false`.
- **Method.** 13 deals from the category audits, 2015 to 2024, each with a known primary URL. Four queries per deal, 20 results each:
  - B: `"<brand>"`
  - B+acq: `"<brand>" acquisition`
  - O+B: `"<owner>" "<brand>"`
  - O+B dated: the O+B query with `after:` / `before:` set from 60 days before the deal to 120 days after.

  Each response was reduced in memory to: the rank of the known URL, and the rank and domain of results on a sponsor, company, adviser or wire domain, with yes/no flags (title names the brand / the owner; path holds the brand / looks like a news page). No titles, snippets or result URLs were kept. 52 queries, under $0.05.
- **DeepSeek hit table.** K = rank of the known primary URL (K- = not in the top 20). P = first other probable primary page: its title names both brand and owner, or it is a news page with the brand in its path on a sponsor or adviser site (wire pages need both names in the title). P pages are inferred from flags and were not opened.

| Deal | B | B+acq | O+B | O+B dated |
|---|---|---|---|---|
| Aspen Dental 2015 (Leonard Green) | K- | K- | K10, P6 american-securities | K8 (10 results) |
| Jefferson Dental 2017 (Kirkland) | K- | K2, P5 businesswire | K2 | K1, P3 brentwood |
| Dr. Scholl's 2019 (Yellow Wood) | K- | P1 yellowwood | P1 yellowwood | K17, P3 bayer |
| Lap of Love 2020 (Cortec) | K- | K4 | K4 | K1 (5 results) |
| Natrol 2020 (natrol.com) | K- | K6 | K3 | K-, P5 businesswire |
| Tidal Wave Auto Spa 2020 (Golden Gate) | K- | K- | P17 businesswire | P1 businesswire |
| Dental365 2021 (Kirkland) | K- | K9 | K5 | K1 |
| Bond Vet 2021 (PR Newswire) | K- | K- | P13 warburgpincus | P1 warburgpincus |
| Super Star Car Wash 2021 (TSG) | K- | K2 | K4 | K1 |
| El Car Wash 2022 (elcarwash.com) | K- | K- | K17 | K1, P2 warburgpincus |
| Mattress Warehouse 2022 (company page) | K- | K- | K9 | K1 |
| GoodVets 2023 (General Atlantic) | K- | K- | P8 generalatlantic | — (19 results, none primary) |
| MB2 Dental 2024 (Charlesbank) | K- | K- | P11 warburgpincus | P6 warburgpincus |

- **Totals.** Known URL in the top 20 on some query: 9/13 (8/13 in the top 10). Known URL or a probable primary page: 13/13. By query:
  - B: known 0/13, either 0/13
  - B+acq: known 5/13, either 6/13
  - O+B: known 8/13, either 13/13
  - O+B dated: known 8/13, either 12/13
- **Readings:**
  - The index reaches 2015: Aspen Dental's March 2015 release comes back.
  - The brand name alone returns the brand's own site, not the deal.
  - Naming the owner finds a primary page for every deal. Without the owner (brand plus "acquisition"), it finds one for about half.
  - The date window moves the known page to rank 1 in 6 of its 8 hits. It loses pages whose `date` is wrong: Natrol's 2020 release is dated 2022-06-28, outside the window.
  - The other eight known hits carry a `date` of 16:00 UTC, which is midnight China time. Read that way, six match the audit's release date to the day. Super Star is one day after its signing date. Lap of Love's date is a week before its 2020-01-24 closing; its release date isn't in the audit.
- **Next:** the same run on Mojeek (plus an unquoted O+B query) and Brave (`freshness` range for the dated query) once `MOJEEK_API_KEY` and `BRAVE_API_KEY` are in `.env`.

## Answer

Done 2026-11-19, DeepSeek Search only. Hit table, method and readings are in the 2026-11-19 comment above. Spend: under $0.05.

- **Developer decisions (2026-11-19):**
  - **DeepSeek Search is the only web search API.** Every AI integration stays with one vendor, unless another is far cheaper. It isn't: per 1,000 requests, DeepSeek charges $0.75 for up to 50 results, Mojeek £2 for 10 (£3 with storage rights), and Brave $5 for 20 (storage only on a plan with no published price). A launch run of 1,496 queries comes to $1.12 on DeepSeek, £2.99 to £4.49 on Mojeek and $7.48 on Brave before its $5 monthly credit. Mojeek and Brave were not tested, and step 1's accounts aren't needed.
  - **DeepSeek's results may be kept and shown.** The [Open Platform Terms of Service](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html) (effective 2026-04-29) and the search docs don't ban it, and the developer rules that is enough.
- **Coverage:** the index reaches 2015.
  - Owner plus brand (`"<owner>" "<brand>"`) found the known primary page for 8 of 13 deals from 2015 to 2024, and the known page or a probable primary page for all 13.
  - Brand plus "acquisition", the only query possible when the owner is unknown, found 5 known pages and 6 primary pages.
  - The brand alone found none; it returns the brand's own site.
  - An `after:` / `before:` window put the known page at rank 1 in 6 of its 8 hits, but drops pages DeepSeek misdates (Natrol's 2020 release is dated 2022).
- **What follows from existing rules:** the engine's own crawler fetches every result URL. Fetch stays out, and Search is always called with `need_content: false`, because page text from DeepSeek would get around the bot rules. `snippet` and `summary` are DeepSeek's words and never evidence.

Handed on to "Retrieval fan-out, tracked entities and refresh cadence":
- Search works for confirming or dating a lead we already have (an owner named in a BDC filing, on a portfolio page or in a Form ADV fund), and finds the deal for only about half the brands when the owner is unknown. Whether search is the route to a brand's past coverage, and which queries it runs, stays that ticket's decision.
- With DeepSeek as the only vendor, there's no fallback search when its API is down. How partial failures are handled is already that ticket's question.
- Queries send brand and owner names to a service whose data is stored in China (low sensitivity, noted before).
