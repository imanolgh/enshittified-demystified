# Refresh schedule and next-check date

Type: grilling
Status: open
Blocked by: 37, 118  (Retrieval fan-out, tracked entities and refresh cadence; Past coverage through DeepSeek Search)
Map: [engine](../map.md)

## Question

How often does each recurring job run, how much faster do a pending deal's sources run, and what next-check date does each brand's card show?

## Context

- Split off "Retrieval fan-out, tracked entities and refresh cadence" on 2026-11-20 (round 1 Q0). That ticket decides which sources run for which tracked entities; this one decides how often.
- **Already set elsewhere:** Form ADV monthly files, monthly (ticket 34); BDC submissions JSON, daily; BDC universe and data-set comparison, monthly (ticket 36); last-confirmed sweep, daily (ticket 26); full category recompute, nightly (ticket 68); news-sitemap backfill, daily (ticket 32). A firm's IAPD PDF is re-read when its Latest ADV Filing Date changes (ticket 34).
- **Intervals this ticket sets:**
  - **Registry pass** (every required portfolio, about and newsroom page, detail and paged pages, new releases). A 100-page firm at a 10-second crawl delay takes about 17 minutes. Shared source: a newly listed brand counts as checked only after a pass that finished after it was added, so this interval sets how soon a new brand can be checked (ticket 28).
  - **Wire subject feeds:** polled faster than each turns over its 20 items (ticket 32; about hourly today).
  - **EDGAR full-text search:** a first run since 2001, then only filings since the last run (ticket 70).
  - **13D and 13G** re-reads per public company (ticket 70).
  - **DeepSeek Search** re-runs (ticket 118).
  - **Pending deals** (ticket 26): while today falls inside a pending edge's `expected_close_from`/`expected_close_to`, plus a lead time before and a grace period after, the brand's own sources run faster than normal. The lead time, grace period and faster pace are this ticket's.
  - **Receipt link check:** a periodic check that stored releases' links still work, for the dead-link note (ticket 30).
  - **Beat jobs without a cadence:** retries of ambiguous resolutions (ticket 19); the events consumer (ticket 29). The batch poller is gone (no batch tables, ticket 22).
- **Failed runs** (ticket 37 Q4): a failed run is retried daily for up to 7 days, then only at its normal interval.
- **From chains "What would change this"** (2026-11-18): brand cards show "Next check due {Mon YYYY}", so the schedule must give each brand a next check date the card can read. With shared passes running nightly or weekly, which run that date refers to is this ticket's.
- **Freshness:** how long a completed check stays fresh is chains "Brand-level checked: required sources and freshness"; the intervals here must fit inside it.
