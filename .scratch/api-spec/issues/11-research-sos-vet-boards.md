# Research: SoS and vet license boards in the launch states

Type: research
Status: resolved
Blocked by: 03  (Launch states and metros)
Map: [api-spec](../map.md)

## Question

For each shortlisted state from "Launch states and metros" (**New York**, which is fixed, plus the candidates **FL, CO, TX, AZ**): how can its Secretary of State business registry and its veterinary license board be accessed, and what records do they give?

## Find out (per state)

- SoS: bulk data vs search UI, captcha/terms, record fields (entity number, status, registered agent, officers/managers, mergers/name changes), rate limits.
- Vet board: does the state license **premises/facilities** (needed for a vet census) or only individual veterinarians? Bulk download vs search; fields; cadence; terms.
- SoS terms: is the bulk data or API free, and do the terms allow automated use? This is the first selection criterion.
- **New York only**: if NYSED's licensee data can't be downloaded or scraped, can it be requested under FOIL? Find which office handles it, what fields a licensee list would contain (practice address?), cost and turnaround.
- Rollup density: any primary-source evidence of dental/vet rollup concentration per shortlisted state. This is supporting evidence only; registry roster counts are what's actually used to decide.


## How to resolve

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/api-spec/research/sos-vet-boards.md`. No branches, commits or pushes (map scope ruling 2026-10-26). Then append `## Answer` here: a short summary + link to the findings file.

## Answer

Researched 2026-10-29. Full findings, each claim cited to its primary source, are in [research/sos-vet-boards.md](../research/sos-vet-boards.md).

- **Selection criterion 1 (free SoS bulk data or API the terms allow).** NY, FL and CO pass.
  - **NY**: data.ny.gov SODA datasets, including weekly all-filings, name history, merger constituents and daily filings, under the permissive OPEN-NY terms.
  - **FL**: free Sunbiz SFTP daily and quarterly fixed-width files with the registered agent, up to 6 officers and merger/name events. The Florida DOS site terms of use say "personal, non-commercial use only", which conflicts with that; open question.
  - **CO**: data.colorado.gov, Public Domain, daily. Registered agent only; no officers.
  - **TX** fails: the bulk master file is $1,350 and the search costs $1. **AZ** fails: the ACC Business Center offers search only, with no bulk file.
- **Vet census.**
  - **FL** licenses vet premises (§474.215) and publishes a free weekly CSV with about 2,489 FL establishments, including street address and DBA.
  - **AZ** licenses premises (§32-2272), but the board site returned 403, so list access is unconfirmed.
  - **NY** and **CO** license individuals only. CO publishes a Public Domain list at city/zip level.
  - **TX** facility registration, including owner and MSO disclosure, is required by 2027-09-01 (SB 2155).
- **NY licensee list.** NYSED OP offers weekly "bulk verification files" on request via a support form. Eligibility and fields are unconfirmed. FOIL is the fallback: Records Access Officer, FOIL@nysed.gov, 5/20 business-day deadlines, actual-cost fees. A no-solicitation certification may be required (POL §89(3)(a)). Whether practice addresses would be released is unconfirmed.
- **Rollup density.** Only weak primary evidence was found: FL name matches as a lower bound, and the TX MSO-disclosure statute. Registry roster counts remain the decider.
