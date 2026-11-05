# Brands, companies and locations are separate entities

Status: accepted (2026-11-05). Replaces the `business` and `rollup` entity types in `evidence_layer_plan.md` §4. ADRs 0001–0004 still stand.

The graph no longer has a `business` entity. What a reader calls "a business" is split into a **brand** (a name sold to consumers, such as Dunkin'), a **company** (a legal entity that owns, is owned or runs locations, such as Inspire Brands Inc. or a franchisee LLC) and a **location** (one place where customers are served). We chose this because the three change hands separately. Pizza Hut left Yum! Brands for LongRange in 2026 while Yum! kept Taco Bell and KFC. A franchisee can sell one Dunkin' store to another franchisee, and the store stays the same store. A dental office keeps its address when a rollup buys the practice and a new company runs it. With one merged row, each of these changes rewrites the identity of the thing people look up. With three, each changes one link. The split also builds in the franchise rule (`decisions.md` §4): the brand's owner and the store's operator are different rows, so a search can show both verdicts.

## Rules

- **Entity types:** `brand, company, location, family, investment_firm, fund, retirement_plan, insurer`. `rollup` is dropped: a rollup is a company, and "rollup" is a word the product may use about one. `chain` is not a type. A trust, an ESOP trust, a nonprofit and a government body are companies, with the matching owner kind.
- **Brand:** exists only for a name that spans several locations or is sold as a product. A single-site independent's name is the location's name. A brand owns nothing; its owner is usually a company, but a source may name a fund, investment firm or family as the owner directly *(amended 2026-11-05, engine "Predicate semantics")*.
- **Location:** one place where one company at a time serves customers, under zero or more brands. The same address is not the same location (a vision center run by an independent optometrist inside a Walmart is its own location). A new operator keeps the location; a move to a new address starts a new one.
- **Family:** one person or a family who owns a company in their own name, named only as sources name them. It carries no personal identifiers and is never searchable as a person. "No person entities" (2026-10-26) now means no profiles of individual people. Without this node, a family-owned chain such as Chick-fil-A tops out at its company and reads "owner type not confirmed".

## Consequences

- A name in a quote must resolve to the right type ("Subway" may mean the brand or the company): "Entity resolution algorithm".
- No predicate links a location to its brand. *(Settled 2026-11-05 by "Predicate semantics": the link is identity data, `location_brands` rows written by code producers, never a claim or a hop. A location is run by its operator through `operated_by`.)*
- Which of brand, company and location carry an ownership category: "Category precedence and storage". Whether chains v1 stores locations at all: chains-and-brands "Brand and chain model".

## Considered options

- **Keep `business` as the site and its local operator merged, and add `company`:** simplest for one-site local businesses, but a franchise resale or a practice buyout turns one business into another, and the brand still has no home.
- **`business` means the legal entity, with no location type:** matches SoS and SEC records, but cannot express one site changing operator, and the store a consumer visits has no row of its own.
