# Ownership

How the project describes who owns a local business and how private equity sits above it.

## Language

**Ownership chain**:
The ordered list of owners from a local business up to a private equity fund, e.g. Dentist → Smile Partners → Fund X. A business can have more than one chain.
_Avoid_: Ownership tree, path (in user-facing text)

**Hop**:
One ownership link between two neighbours in an ownership chain.
_Avoid_: Step, level, link (when counting)

**Separation degree**:
The number of hops from a local business to one specific private equity fund. A fund that owns the business directly is at separation degree 1.
_Avoid_: Distance, depth

**PE-owned**:
The category of a business that has at least one ownership chain to a private equity fund with no minority hop, whether the fund owns it directly or through intermediate companies.
_Avoid_: PE-backed, PE-affiliated

**PE minority stake**:
The category of a business whose every ownership chain to private equity contains at least one minority hop.
_Avoid_: Partial PE, PE-invested

**Minority hop**:
A hop where a cited document states a stake under 50% or calls it a minority investment. A hop with no stated stake counts as control.
_Avoid_: Partial stake

**Formerly PE-owned**:
History shown for a business whose chain to a private equity fund has ended, with the years it lasted. It is history, not a current category.
_Avoid_: Ex-PE, previously backed

**No PE evidence found**:
The category of a business that was checked against every known ownership source and has no chain to private equity, always shown with the date it was checked.
_Avoid_: Independent, PE-free, not PE-owned

## Owners

**Owner kind**:
What sort of owner an entity is: PE firm, other investment fund (venture capital, hedge, or real estate only), conglomerate, family, employee-owned, trust, public company, nonprofit, or government. It is a fact about the owner, not about any single hop.
_Avoid_: Ownership type, owner category

**Certified Independent**:
A future badge a business earns when automated checks of official records show no PE ownership. The only way the product will call a business independent.
_Avoid_: Verified independent, independent (unqualified)

**Owner type not confirmed**:
What the product shows when an owner's owner kind cannot be established from any source, or its sources disagree. The ownership chain is still shown.
_Avoid_: Unknown owner, unclassified

**Investment firm**:
A company that manages funds. Its owner kind says whether it is a PE firm.
_Avoid_: Sponsor, GP, asset manager (as entity labels)

**Fund**:
A pool of money run by an investment firm that owns or lends to companies. Whether it owns or lends is a relationship, not part of what it is.
_Avoid_: Lender, vehicle

**Rollup**:
A company that owns or operates many local practices, such as a dental support organization, a vet group, or a physician management company.
_Avoid_: DSO (for anything that is not dental), consolidator, platform

**Retirement plan**:
A public pension or an employer 401(k) plan that a user can check for exposure.
_Avoid_: Pension (for 401(k) plans), scheme

## Evidence

**Verified**:
Backed by two independent sources, or by one official filing.
_Avoid_: Confirmed, proven

**Reported**:
Backed by exactly one non-official source, and labeled that way to the reader.
_Avoid_: Unverified, alleged, single-source (in user-facing text)

**Sources disagree**:
The state of a fact whose sources contradict each other. It is not published as a fact; the reader sees that the sources disagree, with links to each.
_Avoid_: Disputed, conflict (in user-facing text)

**Last confirmed**:
The most recent date any source still showed a fact. A hop not confirmed for a long stretch is shown with this date and stops counting as current ownership.
_Avoid_: Stale, expired, out of date (in user-facing text)

**Official filing**:
A record a government agency publishes or requires by law, such as an NPPES provider record, a Form 5500, or a Form ADV. One is enough to make a fact verified.
_Avoid_: Government source, authoritative source

**Independent sources**:
Two sources from different publishers' datasets or different web domains. A press release copied onto five sites is one source.
_Avoid_: Separate sources, multiple sources

**Registry**:
The curated list of PE firms and rollups and where their pages are. It tells the crawler where to look and is never itself evidence.
_Avoid_: Database, list of PE firms (as a source)
