# Launch states and metros

Type: grilling
Status: resolved
Map: [api-spec](../map.md)

## Question

Which state(s) does the engine cover at launch (SoS scraper, vet license boards), and which 2–3 showcase metros get full-depth research?

## Context

- **One state or several?** build_roadmap.md:99 ("your launch state only"), :167 (second SoS "if time allows"), :173 (states 2–50 deferred) vs pre-launch-seeding.md:46 (2–3 metros, each needing an SoS you've built), :86 (vet boards "for launch states"), evidence_layer_plan.md:55,242 ("launch states").
- **Selection criteria only** (pre-launch-seeding.md:46): documented rollup density, an SoS you've built a scraper for, where you live.
- **Metro definition** is undefined: CBSA, county FIPS list, or zip list? Used as "metro census slice" in research_flows.md:22; a crosswalk source is needed.
- Vets have no NPPES census; the vet denominator for a state comes only from its license board (build_roadmap.md §8, pre-launch W4) — feasibility per state is researched in "Research: SoS and vet license boards in the launch states", which this ticket unblocks.
- Phase 5's "second SoS" was ruled into this ticket (map scope ruling, 2026-10-26).

## Answer

Resolved 2026-10-29 (grilling with the developer).

1. **Launch state 1 is New York**, fixed (the developer lives in Croton-on-Hudson). The goal stays all 50 states; launch starts here.
2. **Deep research covers whole launch states; there are no metros.** Every dental and vet practice in a launch state gets the full connector fan-out. Reasons: the per-state connectors already set the boundary, and Croton's metro area (New York–Newark–Jersey City) crosses into NJ and PA. "Showcase metro" is dropped as a term, so no metro definition is needed. Each state run is limited by a per-batch spend cap, whose value is set in "Operational identity, budgets and guardrail values".
3. **A second launch state is optional.** If chosen, it comes from FL, CO, TX or AZ, and only if it's cheap: free SoS bulk data or an API, plus a downloadable vet licensee list. Otherwise NY launches alone. The choice is made in "Pick the second launch state", after the research.
4. **Selection rule, in order:**
   1. Free SoS bulk data or an API that the terms allow.
   2. A vet licensee list that can be downloaded or scraped.
   3. Documented rollup density.
   4. The developer's home state.
   
   A downloadable vet list is the tiebreaker.
5. **NY vets.** If NYSED's vet board can't be scraped:
   - The developer files a FOIL request for the veterinarian licensee list with addresses. If the list arrives, it becomes the NY vet census.
   - Until then, NY vets get only the §2B coverage states: confirmed from a rollup roster, or unknown with on-demand research. There is no "No PE evidence found" for them.
6. **Vocabulary.** `GLOSSARY.md` gains **Coverage state** and **Launch state**. Docs always write "coverage state" in full, never a bare "state 1–3".

**Recorded in:**
- `GLOSSARY.md`: the new Coverage section.
- `pre-launch-seeding.md`: §2C rewritten as launch-state depth, plus the W4 NY fallback, W5, the checklist and the cost row.
- `decisions.md` §11.
- `research_flows.md` A1.
- `evidence_layer_plan.md` Phase 2 line.

**Left for the sweep:** `build_roadmap.md` metro wording (Steps 18, 27, 27b, the Phase 2/4 exits, §8 "states 2–50").
