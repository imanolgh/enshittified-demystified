# Form 5500 ingestion and the headline exposure number

Type: grilling
Status: open
Blocked by: 05, 16  (Research: Form 5500 bulk data contents; Claim value schemas and values over time)
Map: [api-spec](../map.md)

## Question

How is Form 5500 data ingested into plans and `allocates_to` claims, how does a user find their employer's plan, and how is the free headline exposure number defined and computed?

## Context

- Depends on whether fund lineups exist in structured data ("Research: Form 5500 bulk data contents" — high risk).
- Clean → plan entities + `allocates_to` claims with file/row provenance, published verified via the official-filing rule (build_roadmap.md:111); sponsor-name normalization is "the real work".
- **Employer → plan**: no predicate/column (research_flows.md:124,146; pre-launch-seeding.md:71); "sponsor index" undefined.
- **Headline exposure number** (pre-launch-seeding.md:71; monetizationideas.md:35,76): never defined — what counts as exposure, computed from the 5500 lineup alone (N-PORT deferred)?
- Which years at launch; amendments; 5500-SF; EIN+PN key; what the quote is (RawDocument: one row per document).
- In scope by map ruling 2026-10-26.
