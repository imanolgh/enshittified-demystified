# Research: Conglomerates among brand owners

Type: research
Status: open
Blocked by: none
Map: [non-pe-owners](../map.md)

## Question

Which owners in the audited and screened industries hold brands across unrelated industries, how does each describe itself, and which are listed, which file with the SEC, and which are private?

## Context

- Charted 2026-11-16. **Not run until the developer unparks this map.**
- v1: `conglomerate` is an owner kind with no official source, and the term table maps only the word "conglomerate" (engine "Owner kind: storage, evidence and the PE-firm test", round 2). A ticker from an SEC filing beats a self-description, so a listed conglomerate reads public company (ADR 0001). The glossary lists the kind without a definition.
- The developer's examples: PepsiCo, Kraft Heinz, Nestlé. On EDGAR's ticker list (2026-11-16): PepsiCo (PEP), Kraft Heinz (KHC), Unilever (UL), General Mills (GIS), J M Smucker (SJM), Conagra (CAG), Newell (NWL), Reckitt (RBGLY). Not there: Nestlé.
- Owners the audits already met:
  - Supplements: Nestlé (6 rows), Unilever (3), Haleon (2), P&G, Kimberly-Clark ([supplements](../../chains-and-brands/research/category-audit/supplements.md)).
  - Beauty and personal care, packaged food and beverages: top 10 brands all owned by public conglomerates or family-controlled public companies ([pe-consumer-scan](../../chains-and-brands/research/pe-consumer-scan.md); [s3-a](../../chains-and-brands/research/pe-consumer-scan/s3-a-beauty-personal-care.md)).
  - Dairy Queen under Berkshire Hathaway ([category-audit-pilot](../../chains-and-brands/research/category-audit-pilot.md) R20); Zinus under the Hyundai Department Store Group, "Korean conglomerate" ([mattresses](../../chains-and-brands/research/category-audit/mattresses.md) MT30); Houchens Industries, a Kentucky ESOP that owns Feeders Pet Supply ([pet-stores](../../chains-and-brands/research/category-audit/pet-stores.md) PT14); Icahn Enterprises, a public holding company with a 13D at Monro ([industry-screen](../../chains-and-brands/research/industry-screen.md)).
  - Ski areas: "conglomerate-owned" in trade press for Vail and Alterra ([a-bowling-golf-ski](../../chains-and-brands/research/industry-screen/a-bowling-golf-ski.md)).

## Find out

1. **The owners:** from the existing audit and screen findings first (no new fetching where they already answer), every owner that holds brands in two or more unrelated industries, with its brands by industry.
2. **Self-descriptions:** each owner's own words for itself on its own site or filings ("conglomerate", "holding company", "diversified", "consumer goods company", "family of brands"), quoted.
3. **Listing and filings:** listed or private; where listed; whether it files with the SEC (10-K, 20-F, or none); whether a family, PE firm, ESOP or another company controls it.
4. **Counts:** how many brands in the audited industries sit under such owners, by industry, and how many of those owners have no SEC filing.

## Rules

- Same rules as chains "Research: Where PE owns consumer brands": public primary sources only, no paywalled sources; robots.txt followed; SEC user agent with the project's name and no email.
- Findings go to `.scratch/non-pe-owners/research/conglomerates.md`.

## Hands on

- "What 'conglomerate' means".
