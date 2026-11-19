# The how-this-works page

Type: grilling
Status: resolved
Blocked by: 58, 107  (Card wording; What would change this)
Map: [chains-and-brands](../map.md)

## Question

What does the public how-this-works page cover, in what order, and how does it link from cards?

## Context

- Split off "Card wording" on 2026-11-18 (round 1 Q0). Pivot proposal: a how-this-works page at launch covering AI, funding and affiliate links.
- Topics handed to it so far:
  - what our labels mean (a backup to the cards' own explanation lines; "Card wording" round 1);
  - how documents are read: an AI model or a parser reads them, and every quote is matched word for word against our stored copy (engine "Brand card, receipt and edge shapes");
  - what two independent sources means: different organizations that don't control each other; a copied release is one source; a company and its owners speak with one voice (engine "Source independence and syndication");
  - why a fund manager's passive holding never counts (engine "Category precedence and public companies"; "Brand card, receipt and edge shapes");
  - which sources a check covers and what "checked {date}" means ("Brand-level checked: required sources and freshness"; engine "What 'checked' means and coverage states");
  - when a past owner stops being shown, and the 18-month "no source has shown this since" rule (engine "Conflict, succession and co-investors"; "Edge lifecycle");
  - Form ADV as the PE test, including firms that don't call themselves PE (engine "Owner kind: storage, evidence and the PE-firm test");
  - the USPTO licensing check and its guard ("Licensed names in v1");
  - funding and affiliate links: which programs, that commission never sets order, Amazon's required line ("Alternatives and affiliate links");
  - that the site covers brands' US businesses ("Product categories: vocabulary and assignment");
  - plain-language help for private-credit terms once BDC lenders show on brand pages (map fog).
- **From "What would change this"** (2026-11-18): the page can explain that the "What would change this" lines come from fixed rules, not written by hand or by an AI model, and what kinds of document change a verdict.

## Comments

### Round 1 (2026-11-18)

- **Purpose and authorship** (Q1): one public page, with no live data, for a reader deciding whether to trust a verdict; Claude drafts it from recorded decisions and the developer approves it before launch; card voice (plain words, sentence case, no quality claims).
- **Sections, in order** (Q2): 1 What this site does (US businesses; no quality ratings); 2 What our labels mean; 3 Where our facts come from (and what we never use: paid databases such as PitchBook, competitor sites, Reddit); 4 How a fact gets onto a card; 5 What "verified" means; 6 How we decide what counts as private equity; 7 Checks, dates and past owners; 8 Licensed names; 9 Alternatives and how we make money; 10 When we're wrong; 11 Who runs this site.
- **Format** (Q3): question headings in a reader's words; each section under about 150 words; a contents list at the top.
- **Links from cards** (Q4): each label and term on a card links to its section; each section has a stable link name (`#verified`, `#private-equity-test`) and can be shared alone.
- **The AI model** (Q5): not named; section 4 says "an AI model" reads documents and copies out quotes, code checks every quote word for word and decides every label, and the AI never decides a verdict.
- **Who runs it** (Q6, revised; Q9): named. Draft: "Imanol Goikuria builds and runs this site and pays for it. It earns money from affiliate links. It has no investors, and it never takes money from private equity firms or from PE-owned brands." ("PE-owned brands", not "the brands it covers": affiliate commissions do come from non-PE brands.) Paid alerts are added to the text when the launch backend ships.
- **Paid alerts at launch, raised and withdrawn:** the developer first asked for paid alerts at launch, then kept the original plan once accounts, sign-in and billing came into view: "we want to remove as much friction as possible from people using the site, and not having any sort of sign up or login is much better." v1 stays without accounts; the launch backend stays parked (ADR 0004).

## Answer

Resolved 2026-11-18 in a grilling session (one round, recorded under Comments).

- **One page, eleven sections** in the order above, question headings, under about 150 words each, a contents list; every card label links to its section by a stable name.
- **AI model not named.** Section 4 explains the reading and the word-for-word quote check; the AI never decides a verdict.
- **Section 11** names Imanol Goikuria, self-funded, affiliate income at launch, no investors, never money from private equity firms or PE-owned brands.
- **Section 10** ("When we're wrong") is drafted once "Legal review before launch" (takedowns and corrections) and "Source-link submissions" settle.
- **Drafting:** a pre-launch task, "Task: Draft the how-this-works page", once the sources list ("Brand-level checked: required sources and freshness"), submissions and the legal review settle; the developer approves the text.
- Docs: none changed; no glossary or ADR change.

Handed on:
- "Task: Draft the how-this-works page" (new).
- "Website pages and shareable cards": the page, its section link names, and the label links on cards.
- launch backend map: the no-friction reason for v1 without accounts.
