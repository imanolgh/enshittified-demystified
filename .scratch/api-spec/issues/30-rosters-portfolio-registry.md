# Rosters, portfolio pages and the registry

Type: grilling
Status: open
Blocked by: 15, 17  (Predicate semantics; Claim producers and the claims door)
Map: [api-spec](../map.md)

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
