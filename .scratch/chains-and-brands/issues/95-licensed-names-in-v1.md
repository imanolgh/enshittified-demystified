# Licensed names in v1

Type: grilling
Status: resolved
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

How does v1 keep a licensee from being published as a brand's owner when the licensee's own pages list the brand without saying it's licensed, now that cookware and clothing and shoes launch and USPTO is not a v1 source?

## Context

- Split off "Category brand lists and checked" on 2026-11-17 (round 1 Q0).
- The gap: a brand's owner is whoever owns its name, never a licensee (GLOSSARY "Brand"). The extraction prompt claims the licensor on "licensed from" or "used under license" and gives the licensee nothing, and a brand list that says some items are licensed gives nothing for unmarked items (engine "Extraction prompt rules", Q2). But a licensee's "our brands" page that never mentions licensing still yields a claim that the licensee owns the brand: Meyer's page lists KitchenAid, Rachael Ray, Ayesha Curry and Farberware, and none of its pages in the test set mentions licensing ("Product categories: vocabulary and assignment", context).
- Under the engine's rules, two owners with no stated stakes are co-owners, not sources disagreeing (engine "Conflict, succession and co-investors"), so a correct licensor claim (Whirlpool for KitchenAid) would stand beside the wrong licensee claim (Meyer) rather than replace it.
- Where it bites in v1: cookware (five licensed rows: Farberware, KitchenAid, Martha Stewart, Rachael Ray, Pioneer Woman; [category-audit-full](../research/category-audit-full.md) §7 item 10) and clothing and shoes (five Authentic Brands Group names and Dr. Scholl's shoes, made or sold by licensees; [apparel-other](../research/product-industry-audits/apparel-other.md)).
- USPTO would fix it only with a precedence rule (the registered owner of a live mark outranks a brand list that never says who owns the name); that question moved to the parked non-PE owners map ("USPTO trademark data: adopt as a source?").
- A fix may change the extraction prompt, which the developer approves (CLAUDE.md); prompt rules live in engine "Extraction prompt rules" and "Task: Draft prompt p9 and run the approval check".

## Comments

### Round 1 (2026-11-17 to 2026-11-18)

- **First proposal, withdrawn** (Q1 a, Q2): give each brand-owner fact a basis ("name" for trademark notices, mark ownership, licensing and brand acquisitions; "list" for brand and portfolio lists) and let a current "name" fact set aside "list" facts naming a different company. The developer asked whether a "name" document would nearly always exist; the cookware audit found one for 2 of its 5 licensed names (KitchenAid: Whirlpool's 10-K; Martha Stewart: Marquee Brands), none for Farberware, Rachael Ray or Pioneer Woman. Revisiting USPTO then exposed a flaw: a trademark notice or a USPTO owner often names an IP-holding subsidiary with no link to its parent (Dunkin's footer names "DD IP Holder LLC"; USPTO named such subsidiaries in 5 of 8 spot checks), so "name beats list" would set aside Inspire's list fact and cut Dunkin', Subway, Arby's and Crunch off from their PE owners.
- **Set-aside rule** (Q2, revised 2026-11-18): a list-grounded owner fact is set aside only by licensing evidence: a licensor saying it licenses the name (Whirlpool for KitchenAid), a licensee saying it holds a license (Lifetime Brands' 10-K for Farberware), or a page saying "used under license". Trademark notices keep working as before: they add an owner and remove none.
- **USPTO reopened, narrow** (Q1, revised 2026-11-18; "USPTO trademark data: adopt as a source?" amended): one licensing check per brand in the licensing-prone launch industries (cookware, clothing and shoes, beauty products, personal care, home furnishings, sporting goods and outdoor gear, pet food and supplies; about 210 brands): the live registration for the brand's name in that industry's goods classes, nothing recorded when several live registrants match. The registered owner is a reported owner fact. **Guard:** when a brand's only chain to private equity starts with a list fact, and USPTO names a different company with no link to the list's company, that chain cannot make the brand PE-owned or PE minority stake; the brand reads "owner type not confirmed" until a source links them. Never an override of other facts. Not broad: restaurants and gyms, where IP-holding subsidiaries are the norm, would lose their best-known PE chains. Reported, not self-verifying; one source type `uspto`; no identifier scheme.
- **Accepted trade-off (developer, 2026-11-18):** some PE-owned product brands whose name is registered to an unlinked IP-holding subsidiary may read "owner type not confirmed" instead of "PE-owned" until a source links the two companies. A false "PE-owned" is the worse error, so the guard errs toward "not confirmed".
- Still open: how licensing evidence is recorded in the claim schema, what the card shows, the brand's own website as a required source, and the prompt and engine changes.

### Round 2 (2026-11-18)

- **Recording licensing evidence** (Q3): a new predicate `licensed_to` (brand → company; never a hop; never shown in v1), and a `basis` value on brand-subject owner claims (`listing` for brands or portfolio pages, `license_grant` when the owner says it licenses the name out). Rule: a `listing` claim (brand → X) makes no hop while the brand has a current `licensed_to` claim naming X or a current `license_grant` claim naming a different company. Checked: KitchenAid (Meyer's listing set aside by Whirlpool's license grant), Dunkin' (a trademark notice has no basis, so Inspire's listing and Roark stay), Farberware (Lifetime's own listing set aside by Lifetime's license statement).
- **The brand card** (Q4): set-aside listing claims and `licensed_to` claims don't show in v1 (showing licensees stays with the parked non-PE owners map). When the USPTO guard applies, the verdict reads "owner type not confirmed" and the card shows the USPTO owner as an owner line with its receipt; a one-line reason goes to "Card wording and the how-this-works page".
- **The brand's own website** (Q5): requested as a required source in "Brand-level checked: required sources and freshness", to catch trademark footers.
- **Follow-on work** (Q6): prompt p10 and a new approval run (engine task); `licensed_to` in "Predicate semantics", `basis` in "Claim value schemas", the set-aside rule in "Conflict, succession and co-investors", the guard in ADR 0001, `licensed_to` in CLAUDE.md; a task for the developer to get USPTO access.

## Answer

Resolved 2026-11-18 in a grilling session (two rounds, recorded under Comments).

- **The gap:** a licensee's "our brands" page that never says "licensed" makes the engine claim the licensee owns the brand (Meyer listing KitchenAid). With no stated stakes the two owners are co-owners, and a PE-owned licensee would make the brand read PE-owned falsely.
- **Set-aside rule:** a listing claim makes no hop when licensing evidence exists: a licensor's license grant naming a different company, or the listing company's own license statement (`licensed_to`). Trademark notices set nothing aside.
- **USPTO, narrow** ("USPTO trademark data" amended): one licensing check per brand in seven licensing-prone industries (about 210 brands); the registered owner is a reported owner fact; a guard stops a listing-only PE chain from making the brand PE when the registered owner is a different, unlinked company.
- **Accepted trade-off:** some PE-owned product brands whose name is registered to an unlinked IP-holding subsidiary may read "owner type not confirmed" instead of "PE-owned" until a source links the two. A false "PE-owned" is the worse error.
- **Known limit:** a licensed name in another industry, or with no live registration and no licensing statement anywhere, keeps the licensee's listing claim; its receipt shows the reader it rests on a brand list.
- Docs: ADR 0001 amended (the guard); CLAUDE.md predicate list (`licensed_to`); evidence_layer_plan.md §4 (`licensed_to` role, `basis`, `uspto` source type); engine "Predicate semantics", "Claim value schemas" and "Conflict, succession and co-investors" amended. No new ADR, no glossary change.

Handed on:
- engine "Task: Draft prompt p10 and run the approval check" (new): the prompt changes and the approval run.
- "Task: USPTO access and mark search" (new, for the developer).
- "Brand-level checked: required sources and freshness": the brand's own website; the USPTO check as a required source for brands in the seven industries.
- "Card wording and the how-this-works page": the guard's one-line reason.
- non-PE owners "Brand licensors and licensees on the brand page": showing licensees (`licensed_to` is now stored).

### Amended 2026-11-18 (from "Card wording", round 2 Q5)

- **Licensees now show in v1**, labeled only as far as sources go: a "Products under this name" section lists "Licensed to {company}" where the company itself says it holds a license, and "Also listed among {company}'s brands" for a set-aside listing, plus "This page reports who owns the name." The licensee's own ownership isn't shown. This replaces round 2 Q4's "don't show in v1".
