# Licensed names in v1

Type: grilling
Status: open
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
