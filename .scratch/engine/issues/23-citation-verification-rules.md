# Citation verification rules

Type: grilling
Status: open
Blocked by: 16, 17  (Claim value schemas and values over time; Claim producers and the claims door)
Map: [engine](../map.md)

## Question

What exactly does `verify_citations` normalize and check, and which sanity checks run where?

## Context

- **Normalization spec** (only edge cases are listed: build_roadmap.md:69; conformance-tests SKILL:15–16, which still owes "the developer's own edge-case list"): case sensitivity, NFKC, smart quotes/dashes/nbsp/ellipsis mapping, PDF hyphenation and ligatures, table-cell separators, min/max quote length, whether "…" elisions are allowed, mapping normalized offsets back to the original.
- **Sanity checks** (evidence_layer_plan.md:184–186): "doc mentions the subject alias" — exact or fuzzy; object too? "event_date plausible" — by what rule? "numbers in value appear in the quote" — formats, "in thousands", parenthesized negatives, basis points.
- **Do structured claims go through verify?** Form 5500, NPPES, selector-made claims (see "Claim producers…").
- **Where the BDC numeric cross-check sits**: bdc-parser SKILL:14 and build_roadmap.md:117 say the claim is never emitted; ADR 0002:16 and research_flows.md:133 say rejected; evidence_layer_plan.md:186 makes it a verify-stage sanity check (`sanity_check_failed`). "Withheld filing" has no status/reason in the settled vocabulary (claim status pending|accepted|rejected|retracted + rejection_reason).
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): answered here: every producer's claims go through `verify_citations`. Quote rules per document kind are settled (bulk row = the whole data line; JSON = code-rendered field lines). Identity record values are checked in the door with this ticket's normalization, as found and before storage normalization. A code producer's per-record failure raises an alert. Where the BDC numeric cross-check sits stays here.
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): a new sanity check: a resolved claim whose subject or object type the role table doesn't allow is rejected with `sanity_check_failed`.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): `renamed_from` adds a check: `value.former_name` must appear in the quote.
- **From "Claim identity"** (2026-11-06; notes in evidence_layer_plan.md §4 `claims`): checks this adds: each name as written must appear word for word in the document (whether also inside the quote is this ticket's); a vague phrase passed off as a name ("the company") needs a rule here; after resolution both entity types must fit the role table (misfit → `sanity_check_failed`). Offsets are `quote_start`/`quote_end` into the stored `raw_text`; mapping a normalized match back is this ticket's.
