# Map: Housing (parked)

Label: wayfinder:map · Tracker: local markdown (`docs/agents/issue-tracker.md`) · Charted 2026-11-07 from engine "Funds and their investment firm"

**Parked by ADR 0004 (amended 2026-11-07).** Not part of chains and brands v1 and not part of local businesses. Unparking it is a developer decision. Don't work this map's frontier until then.

## Destination

`.scratch/housing/spec.md`: a build spec for looking up an apartment building or a house for rent or sale and seeing whether a private equity fund owns or runs it, on top of the [engine](../engine/map.md) spec. It must be complete enough that Claude can build it without asking a design question.

## Notes

- The [engine map](../engine/map.md) Notes apply here too.
- Raised by the developer on 2026-11-07, while grilling engine "Funds and their investment firm" (real estate funds own apartments, rental houses and hotels).
- **The shape that works** (facts given in that ticket): a user who found a place elsewhere enters its address or its landlord's name. Searching homes for rent or sale is a listings business: listing data comes from MLSs, which license it to brokers, and from sites whose terms forbid scraping.
- **Engine fit:** a building is a location and its property manager is its operator. Its owner is usually an LLC, which leads to a fund and its firm, the same walk as a brand. A building's owner needs a location → `owned_by` role, which this map would add (a schema decision).
- **Already in the engine:** the owner kinds `real_estate` and `private_equity` (ADR 0001, amended 2026-11-07), funds linked to firms by `managed_by`.
- **In chains and brands instead:** landlords that own the homes they rent under their own name (single-family rental companies) are a candidate category in chains "Product categories". A brand page doesn't say who owns one building.
- **Research tickets**: findings go to `.scratch/housing/research/<slug>.md`.

## Decisions so far

None yet.

## Not yet specified

- **Privacy rule:** individuals own most homes. The product names a family only as its sources do and never profiles a person; this map needs a firm rule that only company and fund owners are shown, and what happens to a building whose owner is a person.
- **Coverage plan:** which places first (cities with rental registries, counties with open parcel data), and what a building outside them shows.
- **Property managers:** how a building shows a manager whose owner differs from the building's owner.

## Out of scope

- **Listings search** (homes for rent or sale): needs MLS licenses or scraping that site terms forbid.
- **Paid national parcel compilations** (Regrid, ATTOM, CoreLogic): paid secondary sources, excluded by the project rule (CLAUDE.md) unless the developer rules otherwise.
- Everything the [engine map](../engine/map.md) rules out of scope.
