# Rosters, portfolio pages and the registry

Type: grilling
Status: open
Blocked by: 15, 17  (Predicate semantics; Claim producers and the claims door)
Map: [engine](../map.md)

## Question

How are the sponsor/rollup registry, portfolio pages and DSO/rollup location rosters stored, crawled, diffed and turned into documents and claims?

## Context

- **Registry storage & schema**: DB table, YAML in repo, or settings? Two entry formats disagree: registry-research SKILL (kind, roster URL, confidence `documented|reported|inferred`) vs build_roadmap.md:95 `{domain, roster_url, selectors, js_required}`. Per-entry developer approval (registry-research SKILL:8,32; pre-launch-seeding.md:80) — kept? The registry is never evidence (GLOSSARY:95–97), so manual `kind` labels are fine under ADR 0002 — confirm; registry `kind` must never set owner kind.
- **Crawler config schema**: selector grammar, pagination / "load more", per-state sub-pages, sitemaps, static-vs-JS flag; Playwright capture.
- **Store-locator JSON APIs**: allowed? (see "Claim producers…").
- **Diff granularity**: page-sha gate, then item-set diff (default).
- **What one document is** for a roster (whole roster page — default) given RawDocument's one-unit-per-citation rule.
- **Unmatched roster locations**: create entities? **Removals**: what does a vanished location mean (see "Edge lifecycle…")?
- **"Exited/former portfolio" sections** → formerly PE-owned?
- **Registry targets** beyond dental/vet (pre-launch-seeding.md:112 "dental ≥30, vet ≥15, etc.").
- The "sponsor registry crawl index" (research_flows.md:43) is never defined (default: Postgres full-text over stored portfolio/roster text).
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): crawl state is assigned here (it had no owner); the registry and crawl-state tables, their columns and retention are this ticket's.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): settled there: portfolio pages go to the LLM; `selector` producers only read long uniform lists (store locators, location rosters); store-locator JSON endpoints are allowed when robots.txt permits them and they feed the public locator page; a JSON record is one document. Still this ticket's: the selector config schema, its revision number (which is the selector's `producer_version`), the selector shape check (expected fields, roughly the usual item count, run before anything is written), and whether an HTML roster page is one document or one per item (the item's text must appear in the page's text either way).
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): a roster or store-locator item yields an `operated_by` claim (location → the company that runs it) when the page states the operator, and `location_brands` rows from the brand names in its identity record. Portfolio pages yield `owned_by`.
- **From chains-and-brands "Brand and chain model"** (2026-11-06): launch needs the registry and sponsor portfolio pages only. Store-locator selectors are for the store-map follow-up (stores without operators). DSO and rollup location rosters are parked with local businesses.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): in the store-map follow-up, a store missing from its brand's locator sets the location's `status = closed` (the diff rule is this ticket's with "Edge lifecycle").
- **From "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended; tables `document_reads` and `source_runs` in evidence_layer_plan.md §4): the registry's `documented|reported|inferred` vocabulary stays inside the registry and never reaches a card (the registry is a crawl list, never evidence). Sponsor pages are a shared source: a pass counts when every page on the list was fetched and read, and a page that keeps failing leaves the list only by a code change after the operator report flags it.
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): a sponsor page's versions are its document rows per extracted text; an unchanged page costs nothing, and a changed page is re-read whole. A store-locator response is a parent and each store record a recurring child (endpoint plus store id).
