---
name: connector-dev
description: Assist the developer while they hand-write a data connector (scaffolding, house-style review, selector configs, fixture prep). Use when working on anything in app/connectors/ — NPPES, Places, EDGAR, sponsor/DSO scrapers, SoS, Form 5500, press RSS — EXCEPT bdc_soi.py (that has its own skill).
---

# Connector Development Assistance

The developer writes every connector by hand. Your contributions are bounded: scaffolding, inventories, selector configs, review against house style, and handing off to the conformance-tests skill. You never write the connector's logic.

## The house style (established in Phase 1–2; hold all connectors to it)
- One module per source in `app/connectors/`; a single public entrypoint the Celery task calls.
- All HTTP through the shared httpx client factory with: tenacity retry/backoff on 429/5xx, per-domain Redis token bucket, identified user agent, explicit timeouts.
- Output is ONLY `RawDocument` instances (plus optional resolution-enrichment structs) from `app/core/contracts.py` — never raw dicts, never direct DB writes; storage goes through `store_document` (sha256 dedup).
- Scrapers: static-first (httpx + selectolax); Playwright only when the page demands it; every crawl records sha256 for the diff loop.
- Paid APIs: per-call cost logging, hard budget guard from settings.
- Bulk ETLs (NPPES census, Form 5500): pandas/polars → cleaned → claims with file/row provenance, `source_type` marked self-verifying per CLAUDE.md invariants.

## What you may produce
1. **Scaffold**: module skeleton with typed function signatures, docstrings describing each step, TODO markers — bodies empty or `raise NotImplementedError`.
2. **Selector configs** for the registry-driven scraper: inspect a target page, propose `{domain, roster_url, selectors, js_required}` entries. Every entry is proposed, never committed without approval.
3. **Column/field inventories** (via doc-digest if not already done).
4. **House-style review**: diff the developer's draft against the rules above; report deviations as a checklist, don't rewrite their code.
5. **Fixture capture**: fetch 2–3 real responses/pages, sanitize if needed, place under `tests/fixtures/<connector>/`, then invoke the conformance-tests skill.

## Definition of done (enforce it)
- [ ] Emits only contract types through the claims door / store_document
- [ ] Shared client + rate limiting + retry in place
- [ ] 2–3 real fixtures committed
- [ ] Conformance test passing
- [ ] Developer has manually verified one real lookup end-to-end
- [ ] Developer can re-explain the module from memory (ask them to summarize it back; if they defer, flag it)
