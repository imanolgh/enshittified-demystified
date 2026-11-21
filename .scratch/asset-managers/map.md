# Map: Asset Managers (parked)

Label: wayfinder:map · Tracker: local markdown (`docs/agents/issue-tracker.md`) · Charted 2026-11-20 from engine "Retrieval fan-out, tracked entities and refresh cadence"

**Parked by ADR 0004 (amended 2026-11-20).** What the largest asset managers hold in, and lend to, the companies behind the brands we cover. Unparking it is a developer decision. Don't work this map's frontier, research tickets included, until then.

## Destination

`.scratch/asset-managers/spec.md`: a build spec for tracking and showing large asset managers (BlackRock, Vanguard, State Street and others) as holders of and lenders to the companies behind brands, on top of the [engine](../engine/map.md) and [chains-and-brands](../chains-and-brands/map.md) specs.

## Notes

- The engine map Notes apply here too: authorship, skills, how to resolve, no application code.
- **Origin** (developer, 2026-11-20, ticket 37 round 2): readers should be able to see whether a brand's company is held or funded by the big asset managers, which "are basically trying to own everything". The developer wants them tracked from launch and full support later.
- **What v1 already gives this map** (facts as of 2026-11-20):
  - Large advisers with private funds load from the monthly Form ADV file.
  - Every tracked public company's 13D and 13G filings are read, so a manager's 5%-plus stakes in those companies are stored as claims and edges. A 13d-1(b) filing never changes a verdict (engine "Category precedence and storage").
  - BDC loans from a manager's own BDCs (BlackRock TCP Capital) are read universe-wide with `managed_by` to the manager.
  - Ended hops and documents are never deleted, so this map can build on what v1 keeps.
- **Decided in ticket 37 (round 2, 2026-11-20):** BlackRock, Vanguard and State Street are tracked from launch through an operator list (wire-feed matching and Form ADV reads), and the list grows by operator upload. Showing 5%-plus holders of public owners on v1 cards is chains [121](../chains-and-brands/issues/121-large-shareholders-of-public-owners-on-the-card.md). Resolved 2026-11-20: v1 cards list every 5%-plus 13D and 13G holder of each public company on a brand's chains, asset managers included, with a "Passive" tag where the filer certifies it, and none changes a verdict. Holdings of 5% or less (13F) stay on this map. The private equity firm test is engine [120](../engine/issues/120-pe-firm-test-and-asset-managers.md).
- **Settled in v1** (engine [120](../engine/issues/120-pe-firm-test-and-asset-managers.md), 2026-11-20): asset managers are their own owner kind, `asset_manager` (a firm with $50bn or more in registered funds), with the category `asset_manager_owned`. They are no longer classed private equity firms, and Vanguard is loaded from Form ADV.
- **Research tickets:** findings go to `.scratch/asset-managers/research/<slug>.md`, primary sources only; bot rules as in CLAUDE.md; no OpenAI models.

## Decisions so far

None yet.

## Not yet specified

- **13F holdings:** each manager's quarterly list of listed stocks, including stakes below 5%: whether to load it, for which managers, and how holdings below 5% are shown.
- **N-PORT look-through:** each fund's holdings, including the loans and bonds that fund companies; shared with the [retirement map](../retirement/map.md).
- **Firm pages:** "what BlackRock holds among the brands we cover"; overlaps engine "Graph endpoint and non-brand shapes".
- **Labels:** how a reader is told an index or mutual-fund manager apart from a buyout firm on cards and firm pages.
- **Which managers:** a named list or a rule.

## Out of scope

- **Any change to chains and brands v1 verdicts.**
- **The private equity firm test:** an engine ticket.
- Everything the [engine map](../engine/map.md) rules out of scope.
