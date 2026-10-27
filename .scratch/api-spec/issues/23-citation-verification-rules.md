# Citation verification rules

Type: grilling
Status: open
Blocked by: 16, 17  (Claim value schemas and values over time; Claim producers and the claims door)
Map: [api-spec](../map.md)

## Question

What exactly does `verify_citations` normalize and check, and which sanity checks run where?

## Context

- **Normalization spec** (only edge cases are listed: build_roadmap.md:69; conformance-tests SKILL:15–16, which still owes "the developer's own edge-case list"): case sensitivity, NFKC, smart quotes/dashes/nbsp/ellipsis mapping, PDF hyphenation and ligatures, table-cell separators, min/max quote length, whether "…" elisions are allowed, mapping normalized offsets back to the original.
- **Sanity checks** (evidence_layer_plan.md:184–186): "doc mentions the subject alias" — exact or fuzzy; object too? "event_date plausible" — by what rule? "numbers in value appear in the quote" — formats, "in thousands", parenthesized negatives, basis points.
- **Do structured claims go through verify?** Form 5500, NPPES, selector-made claims (see "Claim producers…").
- **Where the BDC numeric cross-check sits**: bdc-parser SKILL:14 and build_roadmap.md:117 say the claim is never emitted; ADR 0002:16 and research_flows.md:133 say rejected; evidence_layer_plan.md:186 makes it a verify-stage sanity check (`sanity_check_failed`). "Withheld filing" has no status/reason in the settled vocabulary (claim status pending|accepted|rejected|retracted + rejection_reason).
