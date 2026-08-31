# Backend Build Roadmap
### Step-by-step instructions for building the evidence engine end to end — FastAPI stack, hand-written, Claude Code as research assistant and boilerplate generator
### Companion to: evidence_layer_plan.md (architecture), research_flows.md (scenarios), stack_fastapi.md (tooling), decisions.md (rationale)

---

## 0. The Approach in One Paragraph

**You write the application. All of it** — core domain, every connector, every pipeline task, every endpoint — with one deliberate exception: the **BDC Schedule of Investments PDF parser**, which is fully delegated to Claude Code because its difficulty is irreducible document-format chaos with no learning value. Claude Code's role everywhere else is **assistant, not author**: it reads third-party documentation and reports back what you need to know, generates boilerplate and scaffolding for you to fill in, assembles field lists and API parameter references, answers stack questions, and writes the test suites. You make every architectural decision, type every line of business logic, and test everything manually yourself — the test suites exist for regression protection (run them after your changes) and for Claude Code to verify its own scaffolding, not as a substitute for your understanding. The goal is dual: a working evidence engine, and genuine FastAPI expertise earned by building every piece of a production-grade backend by hand.

**Timeline honesty:** hand-writing everything moves this from ~1 month to a realistic **6–8 weeks** of focused work (nights-and-weekends: think in phases, not days). The roadmap below is organized in five phases with exit criteria; the phase gates matter, the day counts are proportions.

---

## 1. How to Use Claude Code (the assistant contract)

Allowed and encouraged — these are accelerants that don't cost you understanding:
1. **Documentation scanning:** "Read the NPPES API docs and give me: base URL, query parameters for org search, response schema, rate limits, and 2 example responses." You integrate from the digest; you never read the raw docs unless the digest fails you.
2. **Boilerplate and scaffolding:** empty router/service/task skeletons, Alembic env setup, Docker Compose, pyproject config, repetitive SQLAlchemy column definitions *after you've designed the schema*.
3. **Field/parameter assembly:** "List every column in the Form 5500 Schedule H bulk file with its meaning" — the tedious inventory work before you design a model.
4. **Test suites:** Claude Code writes and maintains all tests, including the golden-fixture conformance tests. You run them after every change; you don't hand-craft them.
5. **Explaining errors and idioms:** stack traces, SQLAlchemy patterns, Celery configuration, "what's the Pydantic v2 way to do X."

Not allowed — these are where understanding lives:
6. Claude Code does not write business logic, pipeline tasks, connectors (except the BDC parser), endpoints, or the extraction prompt.
7. Claude Code does not make architectural or schema decisions. It can present options with trade-offs when you ask; you decide.
8. Nothing merges that you couldn't re-explain from memory the next morning. That's the working definition of "intimate understanding" — apply it as a self-check at every step.

Write this contract into `CLAUDE.md` on Day 0 so every session starts with the same rules.

---

## 2. Prerequisites (Day 0)

1. Install: Python 3.12, Docker Desktop, `uv` (or poetry). Have Claude Code generate `docker-compose.yml` (Postgres 16, Redis, MinIO for local S3) and `pyproject.toml` — then read both files until every line makes sense; this is your first "scaffold, then understand" rep.
2. Repo skeleton (Claude Code scaffolds the empty tree; you own everything that goes in it):
   ```
   app/
     core/            # domain: contracts.py, models.py, verify.py, score.py, resolve.py
     connectors/      # one module per source — all hand-written except bdc_soi.py
     workers/         # celery app, tasks, beat schedule
     api/             # routers
   tests/             # Claude Code's territory; fixtures/ holds golden files
   docs/              # commit the ten .md project documents here
   CLAUDE.md
   alembic/
   docker-compose.yml
   ```
3. `CLAUDE.md` contents: the assistant contract (§1), the one delegation exception, the fixture rule ("every connector gets 2–3 real fixture files and a conformance test before it's considered done"), the predicate vocabulary, pointers into `/docs`.

---

## 3. Phase 1 — Core Domain (Days 1–9)

The foundation week-and-a-half. Slowest, most educational, entirely yours. Each step names the FastAPI/Python concept it teaches.

**Step 1 — Contracts (Day 1).** Hand-write `app/core/contracts.py`: `RawDocument`, `ExtractedClaim` (with the predicate `str, Enum`: `acquired_by, owned_by, operates_location_of, lends_to, allocates_to, holds_position, renamed_from`), `ResolvedEntity`, `ClaimCardOut`, `EdgeOut`. *Teaches: Pydantic v2 models, enums, validators.* This file is the constitution — every connector emits these types or its output doesn't exist.

**Step 2 — Database schema (Days 1–2).** Design on paper first (you already have evidence_layer_plan.md §4). Hand-write the SQLAlchemy models: `entities`, `entity_aliases`, `documents`, `claims` (unique index on hash(subject, predicate, object, doc_sha, quote) — idempotency as a constraint, not a convention), `edges`, `review_items`, `ingest_batches/items`, `events` (append-only). Claude Code may generate repetitive column boilerplate *from your written design*; you review every line. Learn the Alembic loop: edit model → `revision --autogenerate` → **read the generated migration** → `upgrade head`. *Teaches: SQLAlchemy 2.0 declarative, relationships, Alembic.*

**Step 3 — FastAPI skeleton + the claims door (Days 2–3).** App factory, `pydantic-settings` config, DB session dependency, health route. Then the single most important small thing in the system: `POST /internal/claims` — the one door through which ALL connector output enters. Validation happens here or nothing gets in. *Teaches: routers, `Depends()`, request/response models, dependency-injected sessions.*

**Step 4 — Document storage (Day 3).** `store_document(raw: RawDocument)`: boto3 put to MinIO/S3, sha256 dedup against `documents`, insert. ~30 lines, all yours. *Teaches: boto3, content-addressed storage.*

**Step 5 — Celery wiring (Day 4).** Celery app on Redis, one toy task, one `chain()`, Flower up. *Teaches: tasks, queues, `delay()` vs `apply_async`, retry config — your `Bus::chain()` translated.*

**Step 6 — `verify_citations` (Days 4–5).** The soul of the product, ~40 lines: whitespace-normalize, substring-search `claim.quote` in stored document text, set verified+offset or auto-reject. Design the edge cases yourself (quote spans a line break; smart quotes vs straight; quote appears twice), then have Claude Code write the test suite around *your* cases plus its own. *Teaches: nothing fancy — and that's the point; the trust mechanism is deliberately boring code you fully own.*

**Step 7 — `extract_claims` (Days 5–6).** Anthropic SDK call. **You write the prompt** — it is product, not plumbing: claims only from provided documents, verbatim quotes mandatory, `no_evidence_found` is a valid answer, ownership-type classification per your taxonomy. Parse the response through Pydantic; drop-and-log failures. *Teaches: the SDK, structured outputs, the validate-at-the-boundary pattern end to end.*

**Step 8 — `score_and_publish` (Days 6–7).** Group verified claims; two independent sources (different source_type or domain) → `verified` edge; one → `reported` + review_item; conflict → review only; official-filing source types self-verify (you'll use this in Phase 3). Append an `events` row on every publication. *Teaches: transactional business logic in SQLAlchemy sessions.*

**Step 9 — Entity resolution v1 (Days 7–8).** `resolve_entity`: exact match → rapidfuzz scored match against entities+aliases → create, or → review on ambiguity. Enrichment sources plug in during Phase 2; logic first, sources second. *Teaches: the resolve-or-review pattern; keeping thresholds as settings.*

**Step 10 — First connector: press RSS (Days 8–9).** Hand-write `connectors/press_rss.py`: httpx → parse feed → fetch article → selectolax text → `RawDocument` → store. Wire the full Celery chain `retrieve → extract → verify → publish` and run it on a real DSO acquisition press release. *Teaches: httpx, async patterns, and the complete pipeline in miniature.*

**✅ Phase 1 exit:** one real claim from one real press release, quote-verified, published as a `reported` edge — every line of the path written by you, re-explainable from memory.

---

## 4. Phase 2 — PE Wedge Connectors, By Hand (Days 10–19)

Each connector: Claude Code digests the docs and drafts the fixture files' *shape*; you write the connector; Claude Code writes the conformance tests; you verify manually against a real lookup before calling it done.

**Step 11 — NPPES, both modes (Days 10–11).** Two deliverables from one source, and the order matters:
- **11a — Bulk census load.** NPPES publishes the *entire* NPI registry as a free monthly bulk file — every dentist, physician, and healthcare organization in the country. Hand-write the ETL (a sibling of the Form 5500 pattern you'll build in Phase 3): download → pandas filter to Tier-1 taxonomies (dental, medical org types) → national census entities in Postgres, with org names, addresses, authorized officials, and other-name aliases. This is your seeding backbone: it replaces hundreds of thousands of per-lookup API calls (and the Places bills that would come with them) with one free file.
- **11b — API client for freshness.** Then write the REST client: org-name+state query, used *on-demand* for freshness checks and for resolving user searches that miss the census. Save 3 real responses as fixtures. *Teaches: your bulk-ETL pattern early, plus your REST-client house style — error handling, timeout policy, the shared Redis token-bucket rate limiter you'll reuse everywhere.*

**Step 12 — Google Places (Days 11–12).** Same motion; first paid API — add per-call cost logging from day one. **Usage policy: lazy and on-demand only** — Places canonicalizes user searches and enriches entities as needed; it is never used for bulk seeding (the NPPES census makes that unnecessary, and bulk Places calls would be your largest bill). *Teaches: keyed auth, quota discipline.*

**Step 13 — EDGAR full-text search (Days 12–13).** Free, keyless, JSON. Query sponsor/DSO names; store hits as documents. *Teaches: nothing new technically — which is the sign your house style is working; this one should feel fast.*

**Step 14 — Sponsor portfolio scraper (Days 13–15).** The pattern investment of the phase, and the other half of the top-down seeding strategy: the rollups **publish their own location rosters**, so a few hundred crawled sponsor/DSO sites enumerate the PE-connected layer *nationally* — you never research independents one by one to find the PE side. One static-HTML sponsor first: fetch → extract portfolio names → `RawDocument` + structured hints → **the diff loop** (sha256 vs last crawl; changed → re-extract). Then generalize it yourself into a registry-driven crawler (domain + selector config per site) and add ~10 Tier-1 sponsor/DSO sites, including one JS-heavy site via Playwright. Claude Code assembles the candidate selector configs from page inspection; you approve each. *Teaches: scraping, Playwright, and the diff mechanism that powers Acquisition Alarm.*

**Step 15 — DSO location rosters (Day 16).** Clone of your own scraper pattern for `operates_location_of` evidence. Should feel like an afternoon.

**Step 16 — One state SoS (Days 16–17).** Your launch state only. The messiest scrape of the phase; budget patience, not elegance.

**Step 17 — Wire resolution + the census match (Day 18).** `resolve_entity` now matches against the NPPES census first (free, local), then falls back to Places → NPPES API for misses. Then run the **census match**: DSO-roster locations (Step 14–15) matched against census entities — every match publishes an `operates_location_of` claim; every unmatched census entity carries "no PE evidence found (checked {date})". This one join is what lights up the national healthcare map. Test manually with a dozen tricky names (franchises, "Dental" vs "Dentistry", DBAs).

**Step 18 — First real batch (Days 18–19).** ~200 dental+vet practices, one metro — now drawn *from the census* rather than a hand-built CSV, exercising deep per-entity research (press, SoS, EDGAR) on top of the census/roster baseline. Build the batch outcome report (resolved / verified-chain / reported / no_evidence / review counts). Fix the top failure classes it reveals — this run's job is to find your resolution-threshold and prompt bugs.

**Seeding strategy, stated once (see decisions.md §12):** national coverage is built **top-down** — sponsor/DSO rosters enumerate the PE layer, the NPPES bulk census supplies the denominator, and their join is the launch map. Bottom-up per-entity research is reserved for metro showcase depth (this step), on-demand user searches, and non-healthcare Tier-1 verticals where no census file exists (vets via state license boards + rosters).

**✅ Phase 2 exit:** national healthcare census loaded and matched against rosters (the map lights up nationally), metro batch producing verified ownership chains queryable via `GET /api/entities/{id}/card`, honest `no_evidence_found` majority, and you can describe every connector's quirks from memory.

---

## 5. Phase 3 — PC Side (Days 20–27)

**Step 19 — Form 5500 ETL (Days 20–22).** The second application of the bulk-ETL pattern you built in Step 11a — same motion, different file. Claude Code inventories the EFAST bulk-file columns; you design the mapping and hand-write the pandas/polars pipeline: download → clean (sponsor-name normalization is the real work) → plan entities + `allocates_to` claims with file/row provenance → publish `verified` via the official-filing rule from Step 8. No LLM anywhere in this path — notice that. *Teaches: the pandas→Postgres motion at scale, and the second flavor of claim (structured, self-verifying).*

**Step 20 — EDGAR submissions client + BDC discovery (Day 22).** By-CIK filing fetch in your house REST style; build the ~150-BDC list.

**Step 21 — BDC Schedule of Investments parser (Days 23–25). THE DELEGATED EXCEPTION.** Hand Claude Code: 3 real 10-Ks from different BDCs as fixtures, your `ExtractedClaim` contract, and requirements — parsed rows → `lends_to` claims quoting row text, numeric cross-check (quoted principal == structured value), `no_evidence` on unparseable tables rather than guesses. Your review is output-based: open each filing PDF beside the emitted claims and hand-check 20 rows per fixture; iterate 2–3 rounds on its failures. You own the *acceptance*, not the pdfplumber internals — and that's the deliberate trade recorded in decisions.md.

**Step 22 — Borrower resolution = the graph join (Day 26).** Parser output → `resolve_entity` (no Places; not storefronts). Watch for a borrower matching a DSO/sponsor the PE side knows — the `lends_to` edge that joins the graphs. Verify the full chain: clinic → DSO → sponsor ← lends_to ← BDC fund.

**Step 23 — Graph endpoint (Day 27).** Hand-write the recursive CTE (SQLAlchemy `text()`) behind `GET /api/entities/{id}/graph`: depth-capped edge walk, confidence on every hop, retracted edges excluded. *Teaches: raw-SQL-within-ORM, recursive CTEs — likely new even from Laravel.*

**✅ Phase 3 exit:** employer → plan lineup works; one BDC's loan book lives as edges; at least one cross-layer chain traverses end to end.

---

## 6. Phase 4 — Refresh, Review, Hardening (Days 28–38)

**Step 24 — Celery Beat schedules (Days 28–29).** Encode the cadence tables from research_flows.md: nightly sponsor/DSO diff crawl, 6-hourly press RSS, daily EDGAR polls, weekly stale-`reported` re-verification. New filings → same chains → **diff vs existing edges** → delta events.

**Step 25 — Events → alerts stub (Day 30).** Minimal consumer of the `events` table (log/email yourself). Acquisition Alarm is a UI on this later; plumbing done now.

**Step 26 — Review panel (Days 31–33).** Hand-build it as a small set of FastAPI endpoints + minimal server-rendered pages or a tiny Vue page — consistent with owning your stack, and honestly not much slower than fighting SQLAdmin's customization for the one view that matters: claim beside document text, quote highlighted, approve/edit/reject writing audit rows. *Teaches: the full request→template/SPA loop in your own API.*

**Step 27 — Full metro batch (Days 34–36).** The 2,000-entity run (research_flows.md A1). Watch Flower; tune workers per queue and rate budgets; measure outcome distribution and LLM spend per entity; fix the top 3 failure classes.

**Step 28 — Retraction + changelog (Day 36).** `POST /internal/edges/{id}/retract` → end-date edge, append event, claims untouched; changelog = query over events. Small; it's the credibility story.

**Step 29 — Hardening (Days 37–38).** Idempotency audit (re-run a filing, prove zero duplicates), tenacity on every connector, dead-letter queue, structured logging with batch/entity correlation IDs end to end, full test suite green, Compose deploy documented. Manual test pass: you, a checklist, and every endpoint.

**✅ Phase 4 exit:** the engine runs unattended over one metro's PE wedge + the PC quick wins; you can trace any claim from source URL to published edge and explain every hop.

---

## 7. Phase 5 — Buffer & Depth (Days 39–45, flexible)

Reserved for what the batches revealed, plus the first deferred items if time allows: more sponsor sites in the registry, a second state SoS, CAFR ingestion spike (one pension system, hand-written, to scope the pattern), Meilisearch if fuzzy-in-Postgres is hurting. This buffer is what makes the 6–8 week estimate honest rather than optimistic.

---

## 8. Explicitly Deferred

CAFRs at scale · N-PORT + the paid 401(k) analysis product · on-demand user research (scenario A2) · OpenCorporates · states 2–50 SoS · WARN, licensing boards, GDELT, CourtListener · NAIC · community submissions · all frontend. Every deferral has a slot: deferred connectors follow a house pattern you've already built by hand; deferred products compose over edges that already exist.

---

## 9. The Learning Ledger (FastAPI expertise, mapped)

By exit of each phase you will have hand-built, in production shape: **P1** — Pydantic contracts & settings, SQLAlchemy 2.0 + Alembic, routers & dependency injection, Celery chains, boundary validation, an LLM integration with mechanical verification. **P2** — bulk-file ETL (NPPES census), a house REST-client style with rate limiting, paid-API cost discipline (lazy Places), scraping with diff detection, Playwright, batch orchestration, and the top-down census-join seeding pattern. **P3** — pandas ETL to Postgres, recursive CTEs, cross-domain entity resolution. **P4** — Beat scheduling, event-driven alerts, an admin surface on your own API, idempotency and observability hardening. That ledger *is* "robust backend API in FastAPI, by hand" — keep it updated as a running brag sheet; it doubles as your interview narrative.
