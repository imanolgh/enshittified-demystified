# What "checked" means and coverage states

Type: grilling
Status: open
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
