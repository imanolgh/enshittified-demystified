# Testing and acceptance bars

Type: grilling
Status: open
Blocked by: 02  (Docs governance and definition of done)
Map: [engine](../map.md)

## Question

How is the build verified when no human hand-checks it: prompt golden tests, acceptance thresholds per component, and the launch gate?

## Context

- **Prompt golden-fixture tests** (CLAUDE.md:7): LLM output varies and costs money — offline replay of recorded responses + a frozen live eval set with precision/recall pass bars run on demand?
- **Acceptance bars**: Steps 18 and 27 measure outcome distributions without pass thresholds — quote-pass rate, resolution precision on a labeled set, BDC row accuracy. An agent can't judge "good enough" alone.
- **Launch gate** replacing W8 (pre-launch-seeding.md:94): share of `reported` and `sources_disagree` — no number.
- **Definition of done shape is settled** ("Docs governance and definition of done", CLAUDE.md working rules): fixtures + recorded live lookup + automatic BDC XBRL cross-check + developer commit. This ticket sets the numbers: what the live lookup must show to pass, the XBRL match threshold, fixture counts per source kind.
- Labeled resolution set: commit the "dozen tricky names" (build_roadmap.md:101) as a fixture.
- Harness defaults: Celery eager + one real-worker chord test; respx for httpx; local static server for Playwright; MinIO; bulk fixtures as real-row slices; property tests for chains/categories; per-test transaction rollback; Postgres test DB (no SQLite — conformance-tests SKILL).
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): golden-fixture tests fail when a producer's output changes until its `producer_version` is bumped (conformance-tests skill updated). The per-run failure threshold for code producers is a numeric bar for the spec.
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): a launch bar for owner-kind coverage: the share of owners whose descriptions mapped to a kind (the number is this ticket's).
- **From "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended; tables `document_reads` and `source_runs` in evidence_layer_plan.md §4): every brand on a launch category list must be checked (every required source finished) before launch; the numeric gate replacing W8 is this ticket's.
- **From "Press and EDGAR full-text connectors"** (2026-11-08; scrape etiquette in CLAUDE.md; press-connector note in evidence_layer_plan.md): chains task "Legal review before launch" is a launch gate. The press connector build must also measure how often an issuer posts its own copy of a wire release, on the launch brands' releases, as evidence for that review.
- **From "Rosters, portfolio pages and the registry"** (2026-11-12; cases in the conformance-tests skill): registry crawler fixtures are real saved pages in `tests/fixtures/registry/` (Roark's hidden former section, TSG's hidden modals, Leonard Green's text status, Golden Gate's paged listing and a detail page, a challenge page).
- **From "Extraction execution"** (2026-11-15): a weekly golden-document check runs the live model on a fixed set and alerts when answers drift (thresholds in "Operational identity, budgets and guardrail values"); the prompt's golden fixtures; the eval harness used for model selection is at `~/.local/share/extraction-eval/` (157 clean-text documents with known facts, scorers `score_clean.py` and `compare_routes.py`, blind precision samplers).
- **From "Extraction prompt rules"** (2026-11-15; check recorded in that ticket's Answer): every prompt or model version passes the approval check before the developer commits it: two full runs on the 157 clean-text documents plus the targeted documents, with bars set against the last approved version (known facts down at most 3 per run, quotes at least 98%, at most 1 lost answer in 314, no claim breaking a prompt rule in the targeted documents, blind precision at least 37 of 40 with at most 1 wrong). Each extraction error found in production adds its document to the targeted set. The harness is at `~/.local/share/extraction-eval/`; how the check and the golden fixtures become pytest suites is this ticket's.
- **From "Task: Draft prompt p9 and run the approval check"** (2026-11-15; results in research/extraction-model-comparison.md "Prompt p9 approval check"): the version check's targeted documents are `data/targeted.json` (5 new pages) plus the in-set documents behind each rule (`data/p9probe.json`, 27 documents), with a rule checker (`scripts/check_rules.py`) and a known-fact sorter (`scripts/fact_diff.py`) in the harness at `~/.local/share/extraction-eval/`. Lessons for the bars: the strict known-facts metric undercounts (it misses relationships found through a different or shorter quote, and counts facts the prompt rules now exclude), so a version's gap needs sorting by hand or a relationship-level match; single runs swing (Roark's page read fully in 6 of 10 reads; one filing can push quotes under 98%), so bars judged on one run trip on noise.
- **From "Form ADV and IRS exempt-org ingestion"** (2026-11-15): fixtures needed: real rows from both SEC monthly adviser files (registered and exempt), real archive rows (Schedule D 7.B.(1) and the adviser base table), and one real IAPD Form ADV PDF with several funds.
