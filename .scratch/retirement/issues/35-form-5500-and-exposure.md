# Form 5500 ingestion and the headline exposure number

Type: grilling
Status: open
Blocked by: engine/05, engine/16  (Research: Form 5500 bulk data contents; Claim value schemas and values over time)
Map: [retirement](../map.md)

## Question

How is Form 5500 data ingested into plans and `allocates_to` claims, how does a user find their employer's plan, and how is the free headline exposure number defined and computed?

## Context

- Depends on whether fund lineups exist in structured data ("Research: Form 5500 bulk data contents" — high risk).
- Clean → plan entities + `allocates_to` claims with file/row provenance, published verified via the official-filing rule (build_roadmap.md:111); sponsor-name normalization is "the real work".
- **Employer → plan**: no predicate/column (research_flows.md:124,146; pre-launch-seeding.md:71); "sponsor index" undefined. Alias, sponsor index, or entity relation? (also moved here from engine "Predicate semantics"; a new predicate would be a schema decision.)
- **Endpoint**: the employer→plan lookup has no path (moved from engine "API conventions, internal auth and operator surface").
- **Refresh**: the Form 5500 load date in the Beat schedule (moved from engine "Retrieval fan-out, tracked entities and refresh cadence").
- **Headline exposure number** (pre-launch-seeding.md:71; monetizationideas.md:35,76): never defined — what counts as exposure, computed from the 5500 lineup alone (N-PORT deferred)?
- Which years at launch; amendments; 5500-SF; EIN+PN key; what the quote is (RawDocument: one row per document).
- In scope by map ruling 2026-10-26; deferred by ADR 0004 (2026-11-04).
- **From "Predicate semantics"** (2026-11-05; role table in evidence_layer_plan.md §4 `claims`): `allocates_to` is retirement plan or insurer → fund, never an ownership hop; it stays in the vocabulary but no engine producer emits it. `holds_position` (fund|retirement_plan|insurer → company|fund) will also carry CAFR fund commitments if CAFRs return.
