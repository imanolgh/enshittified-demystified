# What "checked" means and coverage states

Type: grilling
Status: resolved
Blocked by: 27  (Category precedence and public companies)
Map: [engine](../map.md)

## Question

What has to have happened for a business to show "No PE evidence found (checked {date})", what state does a not-yet-researched entity have, and how do the pre-launch coverage states map onto categories and confidence?

## Context

- **"Checked"**: GLOSSARY:35–37 (checked against every known ownership source) vs research_flows.md:17 and build_roadmap.md:101 (assigned after the roster join alone) vs evidence_layer_plan.md:195 (from an extraction no-evidence result) vs pre-launch-seeding.md:92 (W7 checks only against rosters). The source set varies by vertical and state; does a failed or robots-blocked connector still count as checked?
- **Where checked dates / no-evidence outcomes / unparseable filings are stored** — no table or column (GLOSSARY:35–37; ADR 0001:16; ADR 0002:16; research_flows.md:17,90,114; monetizationideas.md:75).
- **Not-yet-checked state**: BusinessCategory (ADR 0001:20) has no value for an entity that exists but hasn't been researched (SoI borrowers, unmatched roster locations, A2 in flight).
- **Coverage states vs categories**: pre-launch-seeding.md:9–16 says every business is in exactly one of four coverage states, "Verified chain" = ≥2 sources per edge — omitting sources_disagree, owner_type_not_confirmed, non-PE categories, "couldn't confirm which business" (ADR 0002:14), and ignoring that one official filing self-verifies (CLAUDE.md:26).
- **"Likely independent"**: ADR 0001:16 reserves "independent" for Certified Independent; decisions.md:36,84, pre-launch-seeding.md:15, research_flows.md:79 still frame no-evidence as "likely independent"; marketgaps.md:24 has "Verified independent".
- **Confidence vocabulary**: edges `verified|reported|estimated` (evidence_layer_plan.md:116); decisions.md:77 adds `unknown`; evidence_layer_plan.md:261 "honest unknown state"; categories only verified|reported (ADR 0001:14); GLOSSARY has neither `estimated` nor `unknown`; registry uses `documented|reported|inferred`. No in-scope rule produces `estimated` (evidence_layer_plan.md:251) — keep in enum but never emit?
- **Brand level** (added 2026-11-04): what "checked" means for a brand and a category is the product side, in chains-and-brands "Category brand lists and brand-level checked".
- Launch gate replacing W8 (pre-launch-seeding.md:94) has no number — owned by "Testing and acceptance bars".
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): the "A2 in flight" state and the "Unknown, research on request" coverage state (pre-launch-seeding.md:18) are gone. An entity that is in the data but not yet checked still needs a state: searches for it are logged as demand ("Search and the demand log").
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): "nothing found" arrives through the door call; where it is stored is this ticket's.
- **From "ExtractedClaim and the extraction result envelope"** (2026-11-06): `no_evidence_found` is a per-document outcome derived by code: a document the producer read, in a response that finished, that no claim cites. Unreadable documents (unparseable filings, failed responses) never get it, and a document cited only by dropped items gets no outcome. Where the outcome is stored, how it turns into "checked", and what a document whose claims were all rejected counts as are this ticket's.
- **From "Category precedence and public companies"** (2026-11-07; ADR 0001 amended): `no_pe_evidence_found` is the floor of the precedence, for a brand where no owner was found. A brand, company or location can carry a category, but launch computes brands only, so companies and locations have no category state at launch. What must have happened for the floor to show is this ticket's.

## Comments

### Round 1 (2026-11-07)

- **What a check is** (Q1): each product names a required source list per entity type (for a chains brand: "Category brand lists and brand-level checked"). An entity is checked when every required source has finished a run for it; a run that searched and found nothing counts as finished; a source that failed after retries or was blocked by robots.txt leaves the entity unchecked, and an operator report lists it. The checked date is the date of the oldest required run.
- **What a check gates** (Q2): PE-owned and PE minority stake (and a dispute where one reading is PE) can show as soon as their evidence publishes. Every other result (non-PE categories, "owner type not confirmed", `no_pe_evidence_found`) needs a completed check; before it, the brand reads **"not yet checked"**, a new category value, with any owner already found shown in the chain (Workout Anytime would read founder-owned from its own about page alone, though press reports Pugh's 2025 majority purchase). At launch every listed brand must be checked (the bar: "Testing and acceptance bars").
- **Outcomes and storage** (Q3): a `document_reads` table, one row per document per producer version (document, producer, `producer_version`, outcome `cited|no_evidence_found|unreadable|claims_rejected`, read date), and a `source_runs` table, one row per entity per required source (entity, source, started, finished, outcome `completed|failed|blocked`). A run is `completed` only when every document it found reads `cited` or `no_evidence_found`; an unreadable document or one whose claims were all rejected keeps it incomplete until a parser fix, prompt fix or re-run clears it. How the checked date reaches the category: "Category storage and recompute".
- **Coverage states** (Q4): the four states in `pre-launch-seeding.md` belong to the parked local plan; the engine has only categories, confidence and checks. The mapping goes to the local-businesses map's "Not yet specified".
- **"Likely independent"** (Q5): removed from research_flows.md and marketgaps.md; decisions.md §4 and pre-launch-seeding.md get a one-line note citing ADR 0001.
- **Confidence values** (Q6): `estimated` dropped from edge confidence (the retirement map can add it back); `unknown` is not a confidence value (the honest unknowns are "owner type not confirmed", "not yet checked" and the floor); the registry's `documented|reported|inferred` stays inside the registry and never reaches a card ("Rosters, portfolio pages and the registry").

### Round 2 (2026-11-07)

- **Shared sources** (Q7): per-brand sources (an SEC full-text search for the name, the brand's own site) run per brand; shared sources (registry sponsor pages, press feeds, Form ADV files, BDC Schedules) count through their latest complete pass, complete when every item on the list was fetched and read. An incomplete pass leaves the previous complete pass in force, so checked dates stop advancing rather than vanishing; an item that keeps failing leaves the list only by a code change (a registry edit after the operator report flags it). A shared pass counts for a brand only if it completed after the brand was added, so a new brand's first check waits for each shared source's next pass (cadence: "Retrieval fan-out, tracked entities and refresh cadence").
- **Changing the required list** (Q8): a check is judged against the list in force when it ran; adding a source (USPTO, if adopted) doesn't turn checked brands back to "not yet checked"; each brand's next check includes it.
- **Producer versions** (Q9): a new version leaves earlier `document_reads` standing, and the next re-check uses it. Withdrawing a buggy version also withdraws its document reads; every run that relied on them stops counting, and affected brands fall back to their previous complete check, or to "not yet checked", until the re-run finishes (mechanics: "Edge lifecycle").

## Answer

Resolved 2026-11-07 in a grilling session (two rounds, recorded under Comments).

- **A check:** each product names a required source list per entity type. An entity is checked when every required source has finished a run for it (finding nothing counts); a failed or robots-blocked source leaves it unchecked and on the operator report. The checked date is the oldest required run's date.
- **What a check gates** (ADR 0001 amended): PE-owned and PE minority stake show as soon as their evidence publishes; every other result, including `no_pe_evidence_found`, needs a completed check. Before it the brand reads `not_yet_checked`, a new category value. Every launch brand must be checked.
- **Storage:** `document_reads` (one row per document per producer version; outcome `cited|no_evidence_found|unreadable|claims_rejected`) and `source_runs` (one row per entity per required source; `completed|failed|blocked`). A run completes only when every document it found reads `cited` or `no_evidence_found`.
- **Shared sources** (sponsor pages, press feeds, Form ADV, BDC Schedules) count through their latest complete pass, completed after the brand was added; an incomplete pass leaves the previous one in force; a failing item leaves the list only by a code change.
- **Changes:** a check is judged against the source list in force when it ran. A new producer version leaves earlier reads standing; a withdrawn version withdraws its reads, and affected brands fall back to their previous complete check or to "not yet checked".
- **Cleanup:** the engine has no coverage states (the four in pre-launch-seeding.md go to the local-businesses map); "likely independent" removed from live docs; edge confidence drops `estimated`; `unknown` is not a confidence value; the registry's vocabulary stays inside the registry.
- Docs: ADR 0001 amended; glossary "No PE evidence found", new "Checked" and "Not yet checked"; evidence_layer_plan.md §4; CLAUDE.md; research_flows.md, marketgaps.md, decisions.md and pre-launch-seeding.md notes. No new ADR.

Handed on:
- chains "Category brand lists and brand-level checked": the required source list for brands, freshness.
- "Category storage and recompute": the checked date and `not_yet_checked` on stored categories.
- "Retrieval fan-out, tracked entities and refresh cadence": per-brand runs, shared-pass cadence.
- "Edge lifecycle": withdrawing a version's reads.
- "Extraction execution" and "Citation verification rules": writing read outcomes, `claims_rejected`.
- "Document storage, fetch log and last-confirmed": failed and blocked fetches.
- "Rosters, portfolio pages and the registry": registry vocabulary, removing a failing page.
- "Testing and acceptance bars": every launch brand checked.
- "API conventions, internal auth and operator surface": the unchecked and failing-source report.
- "Claim card and graph output shapes", chains "Card wording and the how-this-works page": the "not yet checked" state and wording.
- "Search and the demand log": searches for unchecked brands.
