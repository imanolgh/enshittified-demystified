# Source independence and syndication

Type: grilling
Status: open
Map: [api-spec](../map.md)

## Question

What precisely makes two sources independent, and how is a syndicated or same-publisher copy detected so it counts once?

## Context

- Rule as written: "different source_type OR domain" (CLAUDE.md:26; ADR 0002:9; evidence_layer_plan.md:191; conformance-tests SKILL:17). As intended: a release syndicated to five sites counts once (GLOSSARY:91–93).
- The written rule counts one wire release on five domains as five sources, and a firm's own site + its own press release as independent — while ADR 0001:9 treats them as one "firm's own words" rank.
- ADR 0003:5,11 says source_type names *who published*, but company_site / press_release / news are genres, not publishers.
- Detection options: text similarity, shared-quote check, wire attribution, same issuer.
- python-types-primer.md:55,107 shows the rule as distinct source_type only (omits domain).
