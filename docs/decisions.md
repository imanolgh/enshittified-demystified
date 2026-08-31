# Project Decisions Log
### Decisions and rationale made in conversation that are not captured elsewhere in the document set — read alongside painpoints.md, marketgaps.md, evidence_layer_plan.md, evidence_layer_glossary.md, research_flows.md, and stack_fastapi.md

---

## 1. Backend Stack: FastAPI (Python), not Laravel

**Decision:** Build the entire backend in Python with FastAPI. Laravel was fully evaluated (see `stack_laravel.md`) and rejected for this project.

**Why:** Python is the native language of this workload — scraping (Playwright), PDF and table parsing (pdfplumber/camelot, no Textract dependency), bulk data wrangling (pandas/polars for Form 5500), and LLM tooling. Pydantic gives the cleanest implementation of the core trust mechanism: the LLM's JSON output validates against the Claim schema automatically, rejecting malformed extractions before they touch the database. The project also doubles as an intentional investment in learning FastAPI.

**Accepted costs:** Slower initial velocity while learning the stack (~half speed for the first month), and the review-UI gap — Filament would have provided the human-review panel nearly free; in Python it must be assembled from Starlette-Admin/SQLAdmin or a small Vue panel, and since human review is a load-bearing trust mechanism this is real work, not an afterthought.

**Note:** `evidence_layer_plan.md` has been revised to the FastAPI stack; it retains Laravel equivalents alongside each tool as a reference for a Laravel-fluent reader, plus a Laravel → Python translation cheat sheet in its appendix.

## 2. One Application, Not Two

**Decision:** PE investigation and PC investigation live in one system with one database and one graph — not two separate apps/APIs.

**Why:** The core strategic finding is that PE and PC are one graph: *who owns my dentist → who funds that owner → is my pension holding the paper*. The middle edge (a PE portfolio company borrowing from a BDC that a 401(k) fund holds) is an edge *between* the two sides; two databases would give it nowhere to live. Splitting would also duplicate entity resolution, the claims/verification machinery, and the review panel, and would inevitably drift into two entity IDs for the same firm — the exact identity mess the product exists to fix. The consumer-map → retirement-checker cross-sell also assumes one account and one brand.

**Internally** it is fine to think of "the PE engine" and "the PC engine" as separate ingestion pipelines feeding one system of record. Choosing all-Python made the earlier hybrid (Laravel record + Python sidecar) unnecessary.

## 3. Sources: Public Evidence Only — PitchBook/Preqin/CB Insights Excluded

**Decision:** No commercial private-markets databases in the architecture.

**Why:** (a) Licensing prohibits redistributing or building products on their data (~$25–30k/seat/year, contractually restricted). (b) They are secondary sources — a claim citing PitchBook is unverifiable by ordinary users, which breaks the provenance premise. (c) Coverage misses the long tail (individual local clinics inside a DSO) that is the wedge. The information asymmetry these paywalls create is part of *why* the market gap exists; a public-evidence graph with citable receipts is the thing they structurally cannot become. At most, one internal seat later as a lead-checking aid, never a displayed source.

## 4. Business Categories: Category-Agnostic Pipeline, Tiered Rollout

**Decision:** Users can search any business type; the pipeline does not restrict category. Coverage is sequenced by evidence density.

- **Tier 1 (launch):** dental, veterinary, physician/urgent care, ABA therapy (all get NPPES), funeral homes/crematoria, car washes, HVAC/plumbing/electrical, dermatology/ophthalmology — heavy PE rollup activity, state licensing records, acquisition press coverage.
- **Tier 2:** apartments/property management, daycare chains, pet boarding, med spas, physical therapy.
- **Tier 3:** independent bars, clubs, hair salons, single-location restaurants — low PE density; the honest output is usually "no PE evidence found," framed in the UI as *likely independent*, never as certainty.

**Franchise rule:** ownership is modeled at two levels — **brand ownership** and **location operator** — because a franchised location (e.g., a sandwich shop) is typically owned by a local franchisee even when the brand is PE-owned. Collapsing these would be wrong in exactly the way that destroys trust. National-brand data and local-services data compose in one graph: any search returns both the brand verdict and the operator verdict.

## 5. Paid 401(k)/Pension Analysis: Yes, Informational Only, Subscription-Led

**Decision:** Offer personalized retirement-plan analysis. Public pensions are a lookup against pre-analyzed CAFRs; 401(k)s are resolved via the employer's Form 5500 (or user-entered tickers), with look-through into mutual funds via N-PORT filings. Collective investment trusts (CITs) are reported honestly as opaque.

**Regulatory line:** Reports show evidence, explain mechanisms (gates, PIK, fees), and cite filings — they **never recommend actions**. Recommendation is investment advice and can trigger RIA registration. Wording must stay informational; confirm with a securities attorney before charging for the personalized product.

**Pricing model:** A one-time ~$50 deep-dive is plausible but weak while most plans still show minimal exposure. The primary product is the **monitoring subscription** ($5–8/mo): "your plan is clean today; we watch its filings and alert you when private-markets vehicles appear." The deep-dive is the premium tier for users already known to be exposed. Marginal cost per analysis is near zero because reports compose from already-published edges.

## 6. Map Delivery: Standalone Web App First, Extension Second

**Decision:** The PE consumer product is a mobile-responsive Vue web app on the FastAPI backend, rendering its own map, with deep links out to Google Maps / Apple Maps for directions. A desktop browser extension comes in Phase 2 as a companion, not the product.

**Why:** Google Maps and Apple Maps do not allow third-party plugins inside their apps; the only "inside Google Maps" option is desktop DOM injection into the Google Maps website — fragile, gray-zone, and nonexistent on mobile, where local-business search actually happens. The standalone app gives full control of pins/claim cards/filters, works on every device, and produces shareable URLs. The extension later annotates Google Maps web, Yelp, and business sites, and doubles as Chrome Web Store distribution and screenshot-viral marketing.

**Map rendering:** MapLibre GL with OpenStreetMap-based tiles (MapTiler/Protomaps) rather than Google's Maps JavaScript API, to avoid per-load billing that scales exactly when the product succeeds. Google Places API remains in use server-side for entity resolution only. A PWA (installable web app) covers home-screen presence; a native app only if demand proves it.

## 7. Evidence Layer Is Core Free Product, Not a Premium Add-On

**Decision:** The map does not ship as bare verdicts. Every pin carries a **claim card** — verdict, ownership type, sponsor, acquisition date, and 2–3 primary sources with quotes — as core free product. Progressive disclosure: pin → claim card → full dossier/graph.

**Why:** Even the beloved incumbent brand ledger drew immediate accuracy challenges and "did you use LLMs?" suspicion in its own viral thread. Users will not trust "some random app says my vet is PE-owned"; the receipts *are* the trust mechanism. What remains as the later premium/intelligence layer is depth: full rollup dossiers, connection/money-flow graphs, subscription reports, and eventual graph licensing.

## 8. Anti-Hallucination Architecture (restated as a decision)

**Decision:** The LLM never discovers facts. Deterministic connectors retrieve documents; the LLM extracts claims *from those documents only*, each with a verbatim quote; code mechanically verifies the quote against the stored document and auto-rejects any claim whose quote isn't found. Two independent sources publish an edge as `verified`; one source publishes as `reported` and opens review; conflicts never auto-publish. "No evidence found" is a first-class, published outcome.

## 9. Two-Service Architecture and "Distributed Systems Experience"

**Decision/clarification:** The all-Python choice made the two-service split unnecessary, but the reasoning is recorded: a two-service design would have delivered real experience with idempotency, at-least-once delivery, cross-service contracts, and correlation-ID tracing — but *not* consensus/replication/consistency problems, because state stays centralized in one Postgres by design. Adopt service splits only when justified by tooling fit, never for resume value alone. Idempotency by claim hash and an append-only event log are retained regardless.

## 10. Data & Trust Guardrails (operating rules)

- Immutable S3 archive of every source document (URL, retrieval date, sha256).
- Two-source rule enforced in code, not policy.
- Corrections are public retractions with a changelog — never silent edits.
- Community submissions count as one source; they corroborate but never solo-publish a `verified` edge.
- Scrape etiquette: rate limits, identified user agent, robots.txt, official APIs/bulk data preferred (EDGAR, NPPES, Form 5500, CourtListener are all free and official).
- Confidence is labeled honestly (`verified` / `reported` / `estimated` / `unknown`); the honest unknown state is load-bearing for credibility.

## 11. Seeding Strategy: Top-Down National, Bottom-Up Metro Depth

**Decision:** Launch pre-seeded — an empty map kills trust. But national coverage is built **top-down**, not by researching businesses one at a time:

- **The PE-connected layer** comes from ~300–500 sponsor/DSO/rollup websites, which publish their own location rosters — a few hundred crawled sites enumerate tens of thousands of PE-connected locations nationally, with the roster page as the citation.
- **The census denominator** for healthcare comes from the **NPPES bulk file** — the entire NPI registry as a free monthly download, loaded with the same ETL pattern as Form 5500. Every census entity not matching a roster launches as "no PE evidence found (checked {date})" — the honest likely-independent state, nationally.
- **Vets** (not in NPPES — it covers human healthcare) use state veterinary license boards plus vet-rollup rosters; other Tier-1 verticals (funeral, car wash, HVAC) get top-down roster coverage only, with independents filled on demand.
- **Google Places is lazy/on-demand only** — canonicalizing user searches and enriching entities, never bulk seeding. Used naively for a national census it would be the project's largest bill, exceeding all LLM spend combined.
- **Bottom-up deep research** (full connector fan-out per entity) is reserved for 2–3 showcase metros at launch, on-demand user searches (which permanently grow the graph and act as the crawl-prioritization signal), and review-queue follow-ups.

**Cost consequence:** LLM extraction runs cents per entity (batch pricing, prompt caching, sha256 dedup making re-runs free); realistic launch seeding is a few hundred dollars of LLM spend total. The binding constraints on launch quality are connector coverage and review throughput, not money.

## 12. Learning & Review Plan

Reading order for the document set: `painpoints.md` → `marketgaps.md` → `evidence_layer_glossary.md` (light pass, then reference) → `evidence_layer_plan.md` → `research_flows.md` (trace scenarios A1 and B1 by hand) → `stack_fastapi.md` → `stack_laravel.md` (optional contrast) → this file. Audio/podcast summaries (e.g., NotebookLM) for the conceptual layer; pen-and-paper flow tracing for mechanical precision; then self-written notes reviewed for gaps.
