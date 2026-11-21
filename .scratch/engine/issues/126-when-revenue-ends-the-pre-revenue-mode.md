# When revenue ends the pre-revenue mode

Type: grilling
Status: open
Blocked by: none
Map: [engine](../map.md)

## Question

What revenue, measured over what period, ends the pre-revenue mode of "Cost cuts before revenue" (no timers, the engine on the developer's machine), and what turns back on first when it does?

## Context

- Opened 2026-11-21 when the developer reviewed the monetization tickets (developer: "yes" to opening it). "Cost cuts before revenue" brings back scheduled refreshes and a paid host "once the site earns money" but sets no figure, so the switch has no trigger.
- **What runs before revenue** ("Cost cuts before revenue", 2026-11-21): every recurring job is a step of one operator command, the pass; nothing runs between passes; the engine runs on the developer's machine; the static site is uploaded to Cloudflare Pages (free); search is an index built into the site; the "Report a mistake" form is a free Cloudflare function; cards show no "Next check due" line.
- **What the switch would cost** (`.scratch/engine/research/cost-estimate.md`, re-priced 2026-11-21 in §9): a month with no pass about $1 to $2; a "new deals" pass $2 to $25; a full routine pass $7 to $120 per month since the last; a paid host $65 (Hetzner) to about $450 (Fly.io) a month; Claude Code upkeep stays inside the $100 Max plan.
- **What earns in v1:** affiliate links only ("Alternatives and affiliate links"; the how-this-works page says so). The pivot proposal's illustration: 10,000 visits at 8% clicks, 4% purchases, a $120 order and 6% commission earn about $230. In-store industries earn nothing. Donations count too if chains "Donations in v1" adds them.
- **Paid alerts force the switch:** an alert that a followed brand changed hands is only as fast as the refresh that notices the change, so the launch backend's alerts can't ship without timers (developer, 2026-11-21; launch-backend "Follows and alerts" is now blocked by "Refresh schedule and next-check date"). Shipping alerts ends the pre-revenue mode whatever the revenue figure says.
- Candidates to weigh: a fixed monthly figure (for example affiliate income covering a paid host plus one routine pass a month); a run of months above it (one good month is noise); whether the switch is all at once or in steps (timers first on the home machine, the paid host later); and whether it's automatic or an operator decision prompted by a report.
- Hands on to: "Refresh schedule and next-check date" (cadences once timers return), "Hosting, storage and deployment" (the later paid host), "Operational identity, budgets and guardrail values" (monthly caps once timers run).
