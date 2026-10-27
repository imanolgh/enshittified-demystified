# Product-doc contradictions

Type: grilling
Status: open
Map: [api-spec](../map.md)

## Question

How should the product-strategy docs (monetizationideas.md, marketgaps.md, pre-launch-seeding.md) be reconciled with the engine's rules and the scope rulings, so `docs/` agrees with itself?

## Context

- **Human-written content vs no manual review**: ADR 0002:5 and CLAUDE.md:26 vs monetizationideas.md:23,41 ("editorial monthly brief… an editorial commitment") and marketgaps.md:12,102,234 ("human-verified", "human-written"); research_flows.md:151 says reports compose from published edges with "no new asserting".
- **Certified Independent** (post-MVP): GLOSSARY:45–47 and ADR 0002:13 automated checks only vs marketgaps.md:199 and monetizationideas.md:48 (the business proves ownership, pledges disclosure, pays $200–500/yr).
- **Launch scope vs engine scope**: build_roadmap.md:173–175 vs pre-launch-seeding.md:74,122 and monetizationideas.md:65–76 (deep-dive, retirement monitor, digest, alerts, accounts, billing before beta; deep-dive needs N-PORT). Map ruling: launch backend out of this effort — docs should say so.
- **CAFRs**: pre-launch-seeding.md:73 not at launch vs research_flows.md:120,136–140 (B1c among initial seeding), evidence_layer_plan.md:217,248, marketgaps.md:72; research_flows.md:146 routes users without a 5500 to a pension flow that won't exist. Map ruling: CAFR out.
- **National brands** post-MVP (pre-launch-seeding.md:63; monetizationideas.md:97) vs free-tier brand lookups (monetizationideas.md:34) and launch brand verdicts (pre-launch-seeding.md:54).
- marketgaps.md:208–214 bundles community submissions + certification + a "submission queue" into V1; prices at :32,68,108,120,132 superseded by monetizationideas.md §3.
- Product numbers (follows, beta date, founding price, billing trigger; monetizationideas.md:36,69,72,73) — out of scope unless the launch backend comes in.
