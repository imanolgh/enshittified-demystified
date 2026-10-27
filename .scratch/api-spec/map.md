# Map: API spec

Label: wayfinder:map · Tracker: local markdown (`docs/agents/issue-tracker.md`) · Charted 2026-10-26

## Destination

`.scratch/api-spec/spec.md`: a build spec for the evidence engine — build_roadmap.md Phases 1–5 plus on-demand research (A2), launch-state vet license boards, Form ADV and IRS exempt-org ingestion, and the employer→plan lookup with the free headline exposure number — complete enough that Claude can build it end to end without asking a design question, with `docs/`, `GLOSSARY.md` and the ADRs consistent with it and with each other.

## Notes

- **Domain**: ownership-transparency evidence engine (FastAPI, Celery, Postgres, S3). Read `CLAUDE.md`, `GLOSSARY.md` and `docs/adr/` first; use glossary vocabulary in every ticket and answer.
- **Authorship** (decisions.md §13): the developer decides, Claude builds. Grilling tickets are HITL — never answer the developer's side.
- **Skills**: grilling tickets → `grilling` + `domain-modeling`. Extraction tickets → also `claude-api`. Stack API specifics (FastAPI, Pydantic v2, SQLAlchemy 2.0, Alembic, Celery) → Context7 (CLAUDE.md documentation rules).
- **Resolving a ticket** = `## Answer` in the ticket **plus** recording the decision where it belongs: the doc it changes, `GLOSSARY.md`, or an ADR (only when hard to reverse, surprising, and a real trade-off). Fix the doc remnants the ticket's context lists. **No application code** until the map is done.
- **Research tickets**: findings go to `.scratch/api-spec/research/<slug>.md`, every claim cited to a primary source. No branches, commits or pushes — git commits are the developer's alone.
- **Ticket context** was captured from two inventories (open items/contradictions, and spec-coverage gaps) run 2026-10-26; line numbers may drift as docs change — search by phrase if a reference misses.
- **Decided before the map existed** (recorded in docs, not tickets): ADR 0002's four automation rules (ambiguous match, Jev rule, BDC cross-check, W7 = system QA); claim status `pending|accepted|rejected|retracted` + `rejection_reason`; ingest item `result` + `candidates`; `review_items` dropped (evidence_layer_plan.md §4); the BDC parser is the only source of SoI `lends_to` claims (build_roadmap.md Step 21); authorship overhaul (decisions.md §13).

## Decisions so far

- [RawDocument shape](issues/01-rawdocument-shape.md): one document per citable row; `url` required; storage computes sha256; `content: bytes` never crosses Celery; bulk row = header + row bytes; PDF raw_text written once; free-dict meta; frozen.
- [Research: Form 5500 bulk data contents](issues/05-research-form-5500.md): **no per-plan fund lineups in bulk data** (line 4i schedule is a per-filing attachment, no bulk/API); large plans give asset-class $ totals + Schedule D pooled vehicles (CCT/PSA/MTIA/103-12) by EIN; small plans totals only; plan key EIN+PN; no DOL sponsor index (buildable); amendments replace filings with new ACK_ID.
- [Research: Press-release and news feed sources](issues/10-research-press-feeds.md): PR Newswire + GlobeNewswire public RSS (20 summary items/feed, M&A and Dentistry feeds exist); Business Wire and ACCESS block `/rss` in robots; **Google News RSS is blocked** (robots, ToS, personal-use-only notice); wire terms ban scraping/database storage (legal call for the developer); wire datelines survive republication — a syndication signal.
- [Research: Google Places terms, pricing and a free geocoder](issues/09-research-places-geocoder.md): ADR 0003 holds — only `place_id` may persist (lat/lng ≤30 days; no names/addresses/phones); Text Search (New) with name/address is $0.032/call (IDs-only is free), not $0.017; Places coords can't feed a non-Google map; US Census Geocoder is free/public-domain but approximate and weak on commercial addresses; Nominatim is ODbL and rate-limited.
- [Research: NPPES bulk file and API](issues/06-research-nppes.md): monthly ~1.1 GB zip (10.8 GB CSV, 330 cols, V2 only) + weekly incrementals + XLSX deactivations; DBAs only in `othername_pfile`, extra sites only in `pl_pfile`; solo practices may exist only as Type 1 sole proprietors; ~half of dental orgs use individual-section taxonomy codes (org-code filter misses most); API capped at 1,200 results/query and throttled — bulk must use the file; CMS download page was down 2026-10-26; NUCC taxonomy descriptions need a commercial license; authorized-official clusters hint at DSO footprints.
- [Research: EDGAR access, BDC identification and SoI formats](issues/08-research-edgar-bdc.md): BDC filings are **HTML, not PDF**; Schedules of Investments are **Inline-XBRL tagged per holding since 2022/23**, and SEC DERA publishes a monthly BDC dataset (`soi.tsv`, ~122k holdings, 165 BDCs) — borrower names mostly buried in free-text identifiers; HTML parsing still needed pre-2022 and for JV exhibits; BDCs found by `814-` file number (no SIC), ~171–187 not ~150; SEC UA + 10 req/s; full-text search JSON is undocumented.
- [Research: Form ADV and IRS exempt-org bulk data](issues/07-research-form-adv-irs.md): monthly SEC adviser files give `Any PE Funds` per adviser (ADR 0001's `pe_firm` test, current to 2026-10); fund-level rows (name, `805-` id, `Fund Type` = "Private Equity Fund", fund→adviser link) only in the historical archive through 2024 — post-2025 funds only in per-adviser IAPD PDFs; PE/VC split matches the form; absence from ADV ≠ not PE (family offices, state advisers missing); IRS EO BMF gives exempt status by EIN, not ownership (only Form 990 Schedule R names controlled entities).

## Not yet specified

- **Structure and build order of the spec itself** — how spec.md is organized (by component? by build phase?) and the order Claude builds in; clearer once the domain-model and pipeline tickets close.
- **Seeding runbooks** — the code entrypoints (CLI) and order for registry → NPPES → roster crawl → census match → vet boards → metro batches → 5500 → BDCs → borrower resolution, and the re-extraction backfill; specifiable once the connector tickets close.

## Out of scope

- **Launch backend** — accounts, follows, billing, digest, retirement brief, deep-dive, founding-member beta: a separate body of decisions; candidate next map (scope ruling 2026-10-26).
- **Alerts to users** — need accounts. Events, the public changelog and operational alerts to the developer stay in scope.
- **Jev (Step 27b)** — vendor unconfirmed, experimental; a later effort with real engine data (scope ruling 2026-10-26).
- **CAFR ingestion**, including the Phase 5 one-system spike — pensions are a fast-follow (pre-launch-seeding.md §4).
- **BDC LLM-fallback revisit** — happens after the build, with failure-rate data.
- **Frontend**, and everything in build_roadmap.md §8 "Explicitly Deferred".
