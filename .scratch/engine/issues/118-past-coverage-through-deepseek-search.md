# Past coverage through DeepSeek Search

Type: grilling
Status: open
Blocked by: 37  (Retrieval fan-out, tracked entities and refresh cadence)
Map: [engine](../map.md)

## Question

How does DeepSeek Search find a brand's past coverage: which queries run for which tracked entities, which results get fetched and read, how results on wire sites are handled, and when the searches re-run?

## Context

- Split off "Retrieval fan-out, tracked entities and refresh cadence" on 2026-11-20 (round 1 Q0). That ticket decided (Q5) that **DeepSeek Search is added alongside EDGAR full-text search** as the route to a brand's past coverage: EDGAR covers deals that touch a public filer; DeepSeek covers private deals, adviser (law-firm) releases and second sources.
- **From "Task: Test search API coverage of older deals"** (2026-11-19; hit table in that ticket): over 13 private deals from 2015 to 2024, `"<owner>" "<brand>"` found a primary page for all 13 (the known page for 8); `"<brand>" acquisition` for 6; the brand alone for none. An `after:` / `before:` window put the known page at rank 1 in 6 of its 8 hits but drops pages DeepSeek misdates (Natrol's 2020 release is dated 2022). DeepSeek Search is the only web search API (developer, one vendor for every AI integration), and its results may be kept and shown.
- **The same 13 deals on EDGAR full-text search** (2026-11-20, ticket 37 Q5): no deal document for any of them. Brand-name hits are lenders' schedules, landlords' tenant lists, mortgage-pool prospectuses and licensees; owner-plus-brand found two possible second sources after ticket 70's exclusions (Franchise Group's 2023 merger proxy for Mattress Warehouse; a director's bio in Alignment Healthcare's proxy for Bond Vet).
- **Fixed by earlier rules:**
  - the engine's own crawler fetches every result URL under the bot rules, and Search is always called with `need_content: false`;
  - `snippet` and `summary` are DeepSeek's words, never evidence, and Fetch is out;
  - a fetched page's source type comes from its publisher, never the fetch method (ADR 0003);
  - a release on a wire site can't be a source: wire pages are discovery only, and the release is stored from the issuer's own site, an SEC exhibit or an adviser's page ("Press and EDGAR full-text connectors"). Bond Vet's only known primary page is on PR Newswire.
- **Cost, two parts.** Queries are cheap: about 1,100 brands × 3 queries ≈ $2.50 a run at $0.75 per 1,000, and `count` up to 50 costs the same. Reading is the expensive part: if every one of 20 results per query is fetched and read at about $0.0018, a run costs up to about $120. Which results are worth fetching (title or URL naming the brand, primary domains, rank cut-off) is this ticket's.
- **Which entities search runs for:** from ticket 37's routing table, every tracked brand. Whether owner-plus-brand queries run for each owner on a brand's chain, and how search treats owners above the first private equity owner, follow from ticket 37's round 2.
- **Open:** queries per entity; `count`; date windows and when to drop them; result filtering before fetch; wire-site results; re-run cadence (once at seeding, when a new owner appears, periodically); what counts as a completed run for "checked" (chains "Brand-level checked: required sources and freshness").
