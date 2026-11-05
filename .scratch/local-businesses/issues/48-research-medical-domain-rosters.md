# Research: Rollup rosters for omitted medical specialties

Type: research
Status: open
Map: [local-businesses](../map.md)

## Question

For the medical and care specialties not in Tier 1 (decisions.md §4), which have real rollups with public location rosters, so that they could be added to launch coverage without misleading results?

## Context

- **The gap**: the candidate codes for "physician groups" in [research/nppes.md](../research/nppes.md) reach only family medicine, internal medicine, general practice, pediatrics and emergency medicine, plus multi-specialty group codes. Dermatology, ophthalmology and optometry are their own Tier 1 group. No doc says whether "physician groups" is meant to include anything else.
- **Why rosters decide this**: a specialty in the census without roster coverage leaves PE-owned practices unmatched, so they could show "No PE evidence found", which reads as "likely independent". Roster work is the real cost of adding a specialty, not the extra NPPES codes.
- **The candidate list is a starting point only.** It came from Claude's general knowledge on 2026-10-31, not from sources. Findings may drop candidates or add new ones.
- This ticket adds no specialties. The developer decides from the findings, and until then the launch list stays as it is.

## Candidates

- **Specialist practices**: gastroenterology, orthopedics, urology, cardiology, ENT, allergy, pain management, oncology, OB/GYN, fertility.
- **Hospital-based groups**: anesthesiology, radiology.
- **Mental health**: psychiatry, therapy groups.
- **Other outpatient care**: physical therapy (Tier 2 today), chiropractic (manual search only today), podiatry, audiology.
- **Elder and long-term care**: hospice, nursing homes, home health, senior housing.
- **Other facilities**: dialysis, ambulatory surgery centers.

## Find out (per candidate)

- **Rollups**: which PE-backed rollups operate in this specialty, each with evidence of the PE ownership from a public primary source. National rollups first; note which operate in New York.
- **Rosters**: does each rollup publish its locations? Give the roster URL, whether the list is complete, and whether it needs JavaScript. Note robots.txt or terms that block crawling.
- **Census**: which NUCC taxonomy codes reach this specialty, and in which section (Individual or Non-Individual)? Give the Type 2 count in New York where the NPPES data allows. Note specialties with no usable code, such as senior housing.
- **Roster coverage**: roughly how much of the specialty's New York practices do the known rosters reach? Mark it unknown if there's no sound basis for an estimate.

## Find out (elder and long-term care only)

- **CMS ownership data**: does CMS publish ownership data for nursing homes, hospices or home health? Give the dataset, fields (does it name parent owners?), update cadence, access and terms.
- **Source type**: note whether this data would fit an existing source type or need a new one. That's a schema decision for the developer, so don't pick.

## Rules

- Public primary sources only (CLAUDE.md): no PitchBook, Preqin, CB Insights or any paywalled secondary source.
- These are candidates for the developer's decision, not registry entries. Per-entry registry approval is settled in "Rosters, portfolio pages and the registry".

## How to resolve

AFK. A subagent writes findings, every claim cited to its primary source, to `.scratch/local-businesses/research/medical-domain-rosters.md`, ending with a table of each candidate's rollups, public rosters and census codes. No branches, commits or pushes. Then append `## Answer` here: a short summary + link to the findings file. The developer's decision on what to add goes to "What a business entity is", which fixes the vocabulary and taxonomy mapping.
