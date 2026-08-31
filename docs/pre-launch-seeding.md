# Pre-Launch Seeding Plan
### What must be loaded, matched, and verified before the app launches — plus the definitive category list
### Companion to: decisions.md §11 (seeding strategy), research_flows.md (scenarios A0/A1/B1), build_roadmap.md (who builds what, when)

---

## 1. What "Seeded for Launch" Means

Every business a user can see at launch is in exactly one of four coverage states, and the UI is honest about which:

| State | Meaning | How it got there |
|---|---|---|
| **Verified chain** | Full ownership chain published, ≥2 independent sources per edge, claim card with receipts | Metro-depth research (A1) or roster + corroborating press/filing |
| **Roster-confirmed** | PE-connected via a sponsor/DSO's own published roster (single authoritative source); shown as `reported` pending second source | National roster crawl (A0) |
| **No PE evidence found (checked {date})** | In the census, matched against all known rosters, nothing found — the honest "likely independent" state | Census × roster join (A0) |
| **Unknown — research on request** | Not yet in the graph; searching triggers on-demand research (A2), results in minutes and published permanently | User demand post-launch |

Launch is credible when Tier-1 categories are dense in states 1–3 and everything else fails gracefully into state 4 — never a blank map, never a fabricated verdict.

---

## 2. Launch Categories — Seeded Before Day One

### 2A. Fully seeded nationally (both layers: PE roster layer + census denominator)

| Category | PE layer source | Census denominator | Notes |
|---|---|---|---|
| **Dental practices** | DSO rosters (~30–50 major DSOs) + sponsor portfolio pages | **NPPES bulk file** (dental taxonomies) | The flagship wedge; richest data on both sides |
| **Physician groups / urgent care** | MSO + ER-staffing-firm rosters (TeamHealth/Envision-class), hospital-system pages | NPPES bulk file (medical org taxonomies) | Includes the ER staffing layer — the "which ER is safe" use case from the research |
| **Dermatology / ophthalmology / optometry** | Specialty rollup rosters | NPPES bulk file | High rollup density, clean taxonomies |
| **ABA / behavior therapy** | Rollup rosters (ACES-class) | NPPES bulk file | Serves the worker due-diligence constituency directly |

### 2B. Seeded nationally, PE layer only (census partial or absent)

| Category | PE layer source | Denominator status |
|---|---|---|
| **Veterinary clinics** | Vet consolidator rosters (~15–25 majors: NVA/VCA/Banfield/TSG-backed groups etc.) | **No NPPES** (human healthcare only) — state veterinary license boards for launch states; national census backfilled state-by-state post-launch |
| **Funeral homes / crematoria** | Consolidator rosters (SCI-class + PE rollups) | No public census file; independents appear via on-demand search |
| **Car washes** | PE rollup brand rosters (heavily consolidated, brands list locations) | Same — roster layer only |
| **HVAC / plumbing / electrical** | Rollup platform rosters (brand-family sites list member companies) | Same — roster layer only |

For 2B categories the honest UI states are: roster-confirmed (PE layer), or unknown-with-on-demand — there is no national "likely independent" claim without a census to back it.

### 2C. Metro-depth showcase (full deep research per entity)

2–3 launch metros where **every** dental + vet practice gets the full connector fan-out (press, SoS, EDGAR, NPPES/board records) on top of the census/roster baseline — producing dense verified chains and the screenshots/share-links that market the launch. Pick metros by: (a) documented rollup density, (b) a state SoS you've built a scraper for, (c) where you live (support and spot-checking are easier).

---

## 3. Available via Manual Search Only (on-demand research at launch)

Any business type is searchable from day one — the search box is not category-restricted. Categories below launch with **no pre-seeded layer**; a search triggers Scenario A2 (priority-queue research, minutes, published permanently, honest `no_evidence_found` when that's the answer):

- Restaurants, bars, cafes, clubs (note: franchise handling per decisions.md §4 — brand verdict + operator verdict shown separately)
- Hair salons, barbershops, nail salons, med spas
- Gyms, fitness studios, bowling alleys, movie theaters, entertainment venues
- Daycares and early education
- Pet boarding/grooming, physical therapy, chiropractic
- Apartments / property management (Tier-2; county-records connector post-launch — searches meanwhile resolve manager names against sponsor portfolios)
- Supermarkets, pharmacies, retail storefronts
- Everything else — the category list is open by design; user demand is the crawl-prioritization signal for what gets seeded next

**Not at launch:** national consumer **brands** (the Worse on Purpose competition) — deliberately post-MVP per monetizationideas.md §5; the graph supports it, the launch scope excludes it.

---

## 4. PC Side at Launch

| Surface | Seeded? | Source |
|---|---|---|
| Employer → 401(k) plan lineup lookup + **free headline exposure number** | ✅ Yes | Form 5500/EFAST bulk load (Scenario B1a) — effectively every private-sector plan |
| BDC loan books as `lends_to` edges (incl. the PE↔PC cross-links where borrowers resolve) | ✅ Yes | ~150 BDC latest 10-K/10-Qs parsed (B1b) |
| Public pension lookup (CAFR allocations) | 🔜 Fast-follow, not launch | Top-100 CAFRs; roadmap Phase 5+. UI at launch: "public pension coverage coming — get notified" |
| Paid deep-dive analysis / monitor | 🔜 Post-launch | Composes over the above once monetization ships |

---

## 5. Seeding Workstreams (the actual to-do list)

**W1 — Sponsor & rollup registry curation (the big manual task).** Assemble the master list of ~300–500 sponsor/DSO/consolidator/rollup-brand domains across all §2 categories, each with: domain, roster/portfolio URL, category, static-vs-JS flag, candidate selectors. This is *research*, not code — Claude Code accelerates it (finding rollups per category from trade press and portfolio pages; drafting selector configs), you approve every entry. Expect this to consume more calendar time than any connector. Quality here = coverage at launch.

**W2 — NPPES bulk census load.** Roadmap Step 11a. Download, filter to the taxonomies in §2A, load. One-time + monthly refresh job.

**W3 — National roster crawl + census match.** Scenario A0 in full: crawl every W1 registry entry, publish roster claims, run the census join, publish the "no PE evidence found" denominator for §2A categories.

**W4 — Vet license boards (launch states).** Scraper per launch state's veterinary board → vet census for those states; national backfill post-launch.

**W5 — Metro deep batches.** Scenario A1 across the 2–3 showcase metros; work the review queue to zero on conflicts before launch.

**W6 — PC bulk loads.** Form 5500 (B1a) + 150-BDC parse (B1b) + borrower resolution pass (the graph join).

**W7 — QA & honesty pass.** Hand-spot-check 50 random entities per coverage state against their sources; verify every "no evidence" entity really matched against the full roster set; confirm checked-dates render; confirm A2 on-demand works end to end for an unseeded category.

**W8 — Review-queue drain.** Launch gate: single-source and conflict queues at a size you can actually work weekly, not a backlog measured in thousands.

---

## 6. Cost & Effort Envelope

| Item | Estimate |
|---|---|
| LLM extraction (rosters + metro batches + BDC parse, batch pricing, cached prompts) | **Low hundreds of dollars, one-time**; re-runs free via sha256 dedup |
| NPPES, Form 5500, EDGAR, license-board data | $0 (free/official) |
| Google Places | Near-$0 at seeding (lazy-only policy, decisions.md §11); scales with user searches post-launch |
| Compute/storage (workers, Postgres, S3-compatible) | Tens of dollars/month at this scale |
| **The real costs** | W1 registry curation time, W5/W8 review-queue time, and connector maintenance — human hours, not API bills |

---

## 7. Launch Readiness Checklist

- [ ] W1 registry ≥ target counts per §2 category (dental ≥30 DSOs, vet ≥15 consolidators, etc.)
- [ ] NPPES census loaded + monthly refresh scheduled
- [ ] Census × roster join published; §2A categories show all three seeded states correctly
- [ ] 2–3 metros at showcase depth; review queue drained for them
- [ ] Form 5500 lookup returns lineups for arbitrary employer names; headline exposure number renders
- [ ] ≥1 full cross-layer chain (clinic → DSO → sponsor ← BDC) live and traversable
- [ ] On-demand search (A2) works for an unseeded category, honest states included
- [ ] Every claim card resolves to stored source documents; retraction/changelog path tested
- [ ] Beat schedules running: roster diffs, press polls, EDGAR polls — launch data doesn't rot
- [ ] Spot-check pass (W7) signed off by you personally
