# Pick the second launch state

Type: grilling
Status: open
Blocked by: 11  (Research: SoS and vet license boards in the launch states)
Map: [api-spec](../map.md)

## Question

Given the research findings, does the launch add a second launch state alongside New York and, if so, which one? Also, does NY need the FOIL fallback for its vet census?

## Context

- The rule and shortlist come from "Launch states and metros":
  - Shortlist: FL, CO, TX, AZ.
  - Add a state only if it's cheap: free SoS bulk data or an API the terms allow, plus a downloadable vet licensee list.
  - Rule order: SoS access, then the vet list, then rollup density, then home state. A downloadable vet list is the tiebreaker.
- If NYSED can't be scraped, the developer files a FOIL request for the NY veterinarian list. This ticket confirms whether that's needed and what the request asks for.
- Rollup density per state can be measured from registry roster locations once the registry crawl exists. Otherwise use the research's density evidence.
