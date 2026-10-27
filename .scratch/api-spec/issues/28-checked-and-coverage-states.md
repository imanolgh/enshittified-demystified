# What "checked" means and coverage states

Type: grilling
Status: open
Blocked by: 27  (Category precedence and storage)
Map: [api-spec](../map.md)

## Question

What has to have happened for a business to show "No PE evidence found (checked {date})", what state does a not-yet-researched entity have, and how do the pre-launch coverage states map onto categories and confidence?

## Context

- **"Checked"**: GLOSSARY:35–37 (checked against every known ownership source) vs research_flows.md:17 and build_roadmap.md:101 (assigned after the roster join alone) vs evidence_layer_plan.md:195 (from an extraction no-evidence result) vs pre-launch-seeding.md:92 (W7 checks only against rosters). The source set varies by vertical and state; does a failed or robots-blocked connector still count as checked?
- **Where checked dates / no-evidence outcomes / unparseable filings are stored** — no table or column (GLOSSARY:35–37; ADR 0001:16; ADR 0002:16; research_flows.md:17,90,114; monetizationideas.md:75).
- **Not-yet-checked state**: BusinessCategory (ADR 0001:20) has no value for an entity that exists but hasn't been researched (SoI borrowers, unmatched roster locations, A2 in flight).
- **Coverage states vs categories**: pre-launch-seeding.md:9–16 says every business is in exactly one of four coverage states, "Verified chain" = ≥2 sources per edge — omitting sources_disagree, owner_type_not_confirmed, non-PE categories, "couldn't confirm which business" (ADR 0002:14), and ignoring that one official filing self-verifies (CLAUDE.md:26).
- **"Likely independent"**: ADR 0001:16 reserves "independent" for Certified Independent; decisions.md:36,84, pre-launch-seeding.md:15, research_flows.md:79 still frame no-evidence as "likely independent"; marketgaps.md:24 has "Verified independent".
- **Confidence vocabulary**: edges `verified|reported|estimated` (evidence_layer_plan.md:116); decisions.md:77 adds `unknown`; evidence_layer_plan.md:261 "honest unknown state"; categories only verified|reported (ADR 0001:14); GLOSSARY has neither `estimated` nor `unknown`; registry uses `documented|reported|inferred`. No in-scope rule produces `estimated` (evidence_layer_plan.md:251) — keep in enum but never emit?
- Launch gate replacing W8 (pre-launch-seeding.md:94) has no number — owned by "Testing and acceptance bars".
