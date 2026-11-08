# Category brand lists and brand-level "checked"

Type: grilling
Status: open
Blocked by: 54, 64, engine/28  (Product categories: vocabulary and assignment; USPTO trademark data: adopt as a source?; What "checked" means and coverage states)
Map: [chains-and-brands](../map.md)

## Question

How is a category's brand list chosen and kept current, what has to have happened for a brand to count as checked, and what does the category page promise about coverage?

## Context

- Pivot proposal, **not decided**: "Every major brand in this category is checked" replaces launch states as the coverage promise.
- The brand list needs a public, repeatable source (rankings by sales, units or revenue); the pilot audit records which sources worked.
- Engine "What 'checked' means and coverage states" fixes the engine meaning; this is the brand and category level: which sources must have run (SEC, sponsor portfolio pages, press, Form ADV, USPTO if adopted), and how long a check stays fresh.
- `no_evidence_found` is publishable (CLAUDE.md): "No PE evidence found (checked {date})", never "Not PE-owned" (GLOSSARY).
- **From "Brand and chain model"** (2026-11-06): a category's list holds consumer-facing brand names only. Groups of brands (Luxottica Retail, Inspire Brands, Xponential Fitness) are companies and never list entries; a brand and a same-named company are two rows. Brands whose stores another company runs under license (BJ's Optical) count like any brand. A share counted "by parent company" (audit §9 question 1) would count companies, which exist as rows.
- **From engine "Entity lifecycle"** (2026-11-06): a discontinued brand leaves the launch lists; nothing sets `status = closed` on brands at launch.
- **From "Research: Full category audit (ten remaining candidates)"** (2026-11-07; findings in research/category-audit-full.md): each category file lists its brands with cited owners, a separate list of rollups that aren't brands (dental, vet), and owner-not-found rows (from 1 in car washes and vet to 13 in pet stores). Several rankings are composites, and 2026 deals make public rankings stale; findings §7 lists the open counting questions.
- **From engine "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended): the engine side is settled. A brand is checked when every source on its required list has finished a run (finding nothing counts); its checked date is the oldest run's; a failed or robots-blocked source leaves it unchecked. Shared sources (sponsor pages, press feeds, Form ADV, BDC Schedules) count through their latest complete pass after the brand was added. A check is judged against the list in force when it ran. Before a check completes, a brand shows only PE-owned or PE minority stake, else "not yet checked". Which sources make up the brand list, and how long a check stays fresh, are this ticket's.
- **From engine "Press and EDGAR full-text connectors"** (2026-11-08): press as a required source for a brand means the wire feeds going forward (releases stored from issuers' own sites) plus the historical route, which "Retrieval fan-out, tracked entities and refresh cadence" decides after "Research: Web search APIs for finding a brand's past coverage".
