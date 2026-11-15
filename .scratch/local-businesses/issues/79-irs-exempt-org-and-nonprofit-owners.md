# IRS exempt-org file and nonprofit owners

Type: grilling
Status: open
Blocked by: engine/19  (Entity resolution algorithm)
Map: [local-businesses](../map.md)

## Question

How does the IRS exempt-org data set rank-1 `nonprofit` owner kinds for local owners such as nonprofit hospitals, health systems and clinics: which files, how EINs reach the graph so the file can match, and the cadence?

## Context

- Moved here 2026-11-15 from engine "Form ADV and IRS exempt-org ingestion" (Q4, developer's ruling). The file matches only by EIN, and nothing in the engine writes EINs at launch. The chains-and-brands launch categories have few nonprofit owners. The rank-1 rule stays recorded in ADR 0001 and in `owner_kind_evidence` (evidence_layer_plan.md §4): the IRS exempt-org file emits rank-1 `nonprofit` rows matched by EIN.
- Facts from engine "Research: Form ADV and IRS exempt-org bulk data" ([findings](../../engine/research/form-adv-irs.md)):
  - The EO BMF is a cumulative CSV by state or region, extracted monthly and keyed by EIN, with `SUBSECTION`, `STATUS`, `FOUNDATION` and `NTEE_CD`.
  - It shows that an entity is exempt, not what it holds. Unapplied churches and revoked organizations are absent.
  - Only Form 990 Schedule R (e-file XML, 2019 on) names related corporations and partnerships, with percentage ownership.
  - Pub 78 and the 990 e-file index are other monthly IRS sets.
  - IRS files are U.S. Government works.
- Open points: where EINs come from (NPPES rows carry none; candidates are Form 990 filings, Form 5500, SoS records, 10-K cover pages for for-profit companies); whether Schedule R becomes an ownership source; matching by EIN only versus names.
