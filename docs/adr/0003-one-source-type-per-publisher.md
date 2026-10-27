# One source type per publisher's dataset, not per fetch method

Status: accepted (2026-10-26).

`SourceType` names **who published** a document (`nppes`, `form5500`, `sec_filing`, …), never how it was fetched — so there is no `nppes_bulk` vs `nppes_api`. We chose this because `SourceType` decides whether two documents are independent sources (and so whether a fact is verified); if the bulk file and the API were separate values, one CMS record fetched both ways would count as two independent sources and verify itself. The fetch method still matters for pipelines, auditing, and cost, so it is recorded elsewhere: each connector is its own module with its own processing path, and each document's `meta` records the connector and method (`"retrieval": "bulk" | "api"`).

## Rules

- **Official** source types (one is enough to verify a fact; they also rank first for owner kind, ADR 0001) are a fixed list in code, not a separate enum: `nppes, form5500, form_adv, sec_filing, irs_exempt_org, sos, license_board, cafr`. Not official: `company_site, press_release, news`.
- An SEC 8-K press-release exhibit (EX-99) is stored as `press_release`, not `sec_filing` — filing a press release does not make it official, and the same release on a wire must count once.
- A sponsor portfolio page, a rollup roster, and a firm's About page are all `company_site`; the domain keeps them independent of each other.
- Google Places is never a source type: it is identity lookup only, and its terms forbid storing its content (only `place_id`).
- Values join the enum only when a relationship type takes evidence from them (court records and WARN notices are excluded until then).

## Considered options

- **Separate values per fetch method** (suggested by a general-purpose AI review): gives lineage and per-pipeline config in the enum, but both are already covered by connector modules and `meta`, and it opens the self-verification hole above.
