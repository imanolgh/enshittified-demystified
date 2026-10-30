# Operational identity, budgets and guardrail values

Type: grilling
Status: open
Map: [api-spec](../map.md)

## Question

What is the product's public identity for crawling, what are the budget caps and guardrail values, and where do operational alerts go?

## Context

- **Identified user agent** (CLAUDE.md:52; SEC requires contact): product public name, URL, contact email — none decided; repo and package names differ.
- **Rate limiting**: per-registrable-domain Redis token bucket, default rate/burst, per-domain overrides (SEC), Lua script or the `limits` library (evidence_layer_plan.md:284), shared by httpx and Playwright.
- **robots.txt**: parser (protego), cache TTL, UA token, crawl-delay; RFC 9309 (4xx → allow, 5xx → disallow); applies to Playwright; does it apply to official bulk downloads; how a blocked page affects "checked".
- **Budgets**: a per-batch spend cap for launch-state deep batches (ruled necessary in "Launch states and metros": a full NY run could be ~$1k of extraction, a rough estimate); Places and Anthropic daily caps and behavior when hit (connector-dev SKILL:17 "hard budget guard from settings").
- **Settings inventory/values**: fuzzy thresholds, BDC failure rate, 5% malformed rate, 18 months, graph depth, per-domain rates, model ids, effort (many owned by their own tickets — this one owns the inventory and the ops values).
- **Cost logging** (CLAUDE.md:54): `api_costs` table — provider, SKU, tokens incl. cache, batch discount, $ from a price table, entity attribution via custom_id.
- **Logging/observability**: JSON logs, correlation ids through Celery headers (build_roadmap.md:159); error tracking and metrics (only Flower is named).
- **Operational alert destination** (ADR 0002:16 names none): email via SMTP (default)?
