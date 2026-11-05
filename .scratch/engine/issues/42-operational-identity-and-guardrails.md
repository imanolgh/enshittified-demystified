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
