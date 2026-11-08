# Operational identity, budgets and guardrail values

Type: grilling
Status: open
Map: [engine](../map.md)

## Question

What is the product's public identity for crawling, what are the budget caps and guardrail values, and where do operational alerts go?

## Context

- **Identified user agent** (CLAUDE.md:52; SEC requires contact): product public name, URL, contact email — none decided; repo and package names differ.
- **Rate limiting**: per-registrable-domain Redis token bucket, default rate/burst, per-domain overrides (SEC), Lua script or the `limits` library (evidence_layer_plan.md:284), shared by httpx and Playwright.
- **robots.txt**: parser (protego), cache TTL, UA token, crawl-delay; RFC 9309 (4xx → allow, 5xx → disallow); applies to Playwright; does it apply to official bulk downloads; how a blocked page affects "checked".
- **Budgets**: the per-batch spend cap mechanism (ruled necessary for launch-state deep batches in local-businesses "Launch states and metros"); Places and Anthropic daily caps and behavior when hit (connector-dev SKILL:17 "hard budget guard from settings"). The NY cap value and the NYC-area county list moved to local-businesses "Launch-state run budget and the NYC-area counties" on 2026-11-04.
- **Spend figures for setting the caps** (added 2026-11-04; derivation, prices and assumptions in "Extraction execution"): one chains-and-brands seeding pass ≈ $120 on Sonnet 5.5 batch or $240 on Opus 5.5 batch for ~1,000 brands (an unsettled count); monthly refresh of 1,000–3,000 new documents ≈ $20–60 (Sonnet) or $40–120 (Opus) in batch; an on-demand lookup of an unknown brand (~6 documents, synchronous) ≈ $0.24 (Sonnet) or $0.48 (Opus), the only cost that grows with traffic, so 1,000 such lookups a month ≈ $240–480. Google Places is likely $0 for version 1 (no map; brand lookup doesn't need it).
- **Settings inventory/values**: fuzzy thresholds, BDC failure rate, 5% malformed rate, 18 months, graph depth, per-domain rates, model ids, effort (many owned by their own tickets — this one owns the inventory and the ops values).
- **Cost logging** (CLAUDE.md:54): `api_costs` table — provider, SKU, tokens incl. cache, batch discount, $ from a price table, entity attribution via custom_id.
- **Logging/observability**: JSON logs, correlation ids through Celery headers (build_roadmap.md:159); error tracking and metrics (only Flower is named).
- **Operational alert destination** (ADR 0002:16 names none): email via SMTP (default)?
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): the on-demand lookup cost (~$0.24–0.48 per unknown brand) no longer exists; search itself is the only traffic-driven cost, plus Places only if the demand log uses it (IDs-only Text Search is free). A batch stopped by the spend cap gets status `halted`. The `api_costs` and operational-alerts tables, their columns and retention are this ticket's; money columns are `numeric` with a currency.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): code producers raise alerts in three cases: a failed shape check (the run stops before writing), each per-record failure (naming producer, version and document), and a run stopped by the failure threshold. How alerts reach the developer is this ticket's.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): an identity record whose strong identifier sits on an entity of a different type raises an operational alert (no merge).
- **From "ExtractedClaim and the extraction result envelope"** (2026-11-06): dropped LLM items (unknown label, name not in the document, bad date, failing `value`) are logged; the alert threshold for them is this ticket's, starting from the docs' "flag the batch above 5%".
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): every real text change on a crawled page triggers a whole-document LLM re-read; the spend guardrails should account for it.
- **From "Category storage and recompute"** (2026-11-07; tables `entity_categories` and `entity_pe_owner_periods` in evidence_layer_plan.md §4): values needed: the chunk size for recompute fan-out, and the alert raised when the nightly drift check finds any difference between stored and recomputed categories.
- **From "Press and EDGAR full-text connectors"** (2026-11-08; scrape etiquette in CLAUDE.md; press-connector note in evidence_layer_plan.md): the bot needs the project's own name in its user agent (no contact detail), the same name in Playwright, no proxies or CAPTCHA services, and a per-site stop when a site asks; a cap on documents fetched per brand per run is also needed.
