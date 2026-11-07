# Research: Public sources that tie a building to its owner

Type: research
Status: open
Map: [housing](../map.md)

## Question

Which free public primary sources name the owner (and the manager) of a US apartment building or rental house, how far each lets code follow an owner LLC to a fund or firm, and what each discloses about individual owners?

## Context

- Charted 2026-11-07 from engine "Funds and their investment firm" (Q5, developer ruling): housing is a separate parked effort (ADR 0004 amended). **Not run until the developer unparks this map.**
- Facts given there, to confirm or correct:
  - building ownership sits in about 3,100 county assessor and recorder systems, each separate;
  - national compilations (Regrid, ATTOM, CoreLogic) are paid secondary sources the project rule excludes;
  - deeds name an LLC, and Delaware LLCs don't disclose their members;
  - public landlords list subsidiaries in SEC filings (Exhibit 21); private ones mostly don't;
  - some cities publish rental registries: New York City's HPD registrations name the owner and managing agent of multi-unit buildings.
- Owner kinds and chains: ADR 0001 (amended 2026-11-07: `real_estate`, `private_equity`, `managed_by`).

## Find out

- **County records:** which large counties publish owner names in free bulk or open data (assessor rolls, recorded deeds), their formats, update cadence and terms of use; whether a state publishes a statewide parcel file.
- **City rental registries:** which cities publish them as open data, what fields they carry (owner, managing agent, units), and their terms.
- **LLC registries:** which states disclose an LLC's members or managers, in bulk or by search, and whether their terms allow automated use.
- **SEC filings:** whether public landlords' subsidiary lists, and any SEC-filed securitizations of rental homes or apartment loans, name properties or their owners.
- **Other federal sources:** whether any public HUD, Fannie Mae or Freddie Mac data names a property's owner or sponsor.
- **Individuals:** what each source discloses about owners who are people, and any state rules on publishing it.
- **Rough coverage:** what share of US rental units the free sources would reach.

## Rules

- Public primary sources only (CLAUDE.md), and competitor sites are never sources. Whether third-party tools that map landlords may be used is engine "Competitor and third-party data rule"; until it closes, list them only as leads, never as sources.
- Respect robots.txt and site terms; user agents carry no contact detail.

## How to resolve

AFK: a subagent invokes the `research` skill and writes `.scratch/housing/research/building-ownership-sources.md`, then appends `## Answer` here. No branches, commits or pushes.
