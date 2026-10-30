# Research: SoS and vet license boards in the launch states

Type: research
Status: open
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
