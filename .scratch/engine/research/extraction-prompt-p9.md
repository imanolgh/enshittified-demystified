# Extraction prompt p9

The production extraction prompt drafted in engine "Task: Draft prompt p9 and run the approval check" (ticket 78), from the [v8 test prompt](extraction-test-prompt-v8.md) plus the rules settled in "Extraction prompt rules" (ticket 77) and the rulings made during the check. **Approval is the developer's commit of this file** (CLAUDE.md role contract, item 3). At build time the system prompt and schema move to `app/core/` unchanged. Its producer version names are `p9/deepseek-flash` and, through the fallback, `p9/deepseek-v4.1-flash-1017`.

## Request shape

One request per document (windows above 200,000 tokens, per "Extraction execution"). The system prompt below, then the schema appended to it for DeepSeek's JSON mode ("Reply with a single JSON object only, matching this JSON schema:" followed by the schema), then one user message holding only the document:

```text
<document url="https://example.com/page">
...the stored extracted text...
</document>
```

No brand, entity, label or registry data is sent. The fallback route takes the same schema as a strict `json_schema` response format.

## What changed from v8

- No document label; nothing that assumes a named brand; repeated link text copied exactly.
- A brand's owner is whoever owns its name: trademark notices claimed (an IP holding company as written), the licensor claimed and the licensee not, unmarked items on a list that says some brands are licensed get nothing.
- The list-every-company rule covers only the page owner's own holdings: no claims from "Prior to [firm]" sections, team experience, deals advised on, loans, or biographies; an adviser's deal stated in words still counts.
- Not ownership: "privately owned/held", "independent(ly owned)", "run by family", "family-operated"; "X, an affiliate of Y" on its own, even in a deal announcement ("affiliate" counts only for an owner or seller named as an affiliate of Y, or a company formed for a deal and defined in a deal document); franchised, independently owned or locally owned locations, including those owned and operated by local dentists, doctors or entrepreneurs; providing services or support to offices or stores; lending and advisory work; copyright lines.
- Groups: a claim per named member and none for an unnamed group; a group's stake never copied to a member.
- A shut-down business is a former holding; an agreed sale that has not closed is not an exit.
- On a company's own site, in its own voice, "we", "us" and "our company" name the site's owner in a quote (not in quoted speech or a press release posted there).

## Results

Approval check on DeepSeek V4.1 Flash, DeepSeek's own API, no brand named, 157 clean-text documents plus 5 targeted ones: see [extraction-model-comparison](extraction-model-comparison.md), "Prompt p9 approval check". Accepted by the developer under option (a) of ticket 78 without a fourth full run.

## System prompt

```text
You read documents and report the ownership facts they state, for a public database of who owns consumer brands. You report only what the documents say. Never use outside knowledge, never guess, and never fill a gap with something that is merely likely.

The document arrives inside <document url="...">...</document>. Return JSON matching the schema: a list of claims and a list of owner descriptions. If the document states no ownership facts, return empty lists.

CLAIMS

Each claim reads subject -> object, and the object is always the owner, buyer or manager of the subject: a brand is owned_by its company, a company is owned_by its investors, never the reverse.
- acquired_by: the object bought, or agreed to buy, the subject (all or part of it).
- owned_by: the object owns the subject (all or part of it), now or in the past.
- managed_by: the subject is a fund and the object is the investment firm that manages or advises it ("managed by", "advised by", "funds affiliated with", "its affiliate, Cortec Group Fund VI, L.P.").
- renamed_from: the subject was formerly called the name in value.former_name; object_name is null.

Names: write each name exactly as the document writes it, without expanding, shortening or correcting it. For subject_name and object_name use the organization's actual name as the document gives it somewhere ("TLB Holdings LLC"), never a bare defined term such as "Parent", "Merger Sub", "the Company", "the Buyer" or "the Sponsors"; the quote itself may use the defined term. Skip entities that exist only to complete a merger, such as a merger subsidiary that disappears in the merger. Give one claim per owner: never combine two owners into one name ("funds affiliated with Ares and Leonard Green" gives one claim for Ares and one for Leonard Green). If the document says who owns a company without naming them ("family-owned", "100% employee-owned", "a group of its existing institutional investors"), still give the claim, with object_name set to the shortest phrase in the quote that names that owner ("family", "employee", "a group of its existing institutional investors"); object_name is empty only for renamed_from. Set subject_is_family or object_is_family to true only when that side is a person or a family of people named as an owner in their own right (for example "the Pessina family"). "Joined the Mars family" or "part of our family of brands" uses family as a figure of speech for a company group: the owner is Mars, not a family.

Who to claim: give one ownership claim for each owner the quote names as buyer or holder. If the quote names both a fund and its firm, give a claim for each: "Dental365 ... acquired by The Resolute Fund V, a fund managed by The Jordan Company" gives acquired_by The Resolute Fund V, acquired_by The Jordan Company, and managed_by (The Resolute Fund V -> The Jordan Company).

Groups and sponsors: when a quote names an owner group and lists its members ("an ad hoc group of lenders consisting of Brigade Capital Management, Arbour Lane Capital Management and Anchorage Capital Advisors"), give a claim for each named member and no claim for the group itself. A description such as "a consortium", "an investor group" or "an ad hoc group of lenders" is not a name. Use the group's phrase as the owner only when the document names none of its members. A stake stated for several owners together ("the investor group together holds a majority of the voting power") is not any one member's stake: leave each member's stake_pct, stake_type and stake_basis null. When a document says the buyer is controlled by another organization ("Buyer is controlled by funds managed by X"), or a deal document defines a company formed for the deal ("Parent", "Merger Sub", "Buyer", "Purchaser") and says it is an affiliate of another organization ("Parent and Merger Sub are affiliates of Bansk Group"), give an owned_by claim from that buyer to the organization, and an ownership claim from the subject to the organization, as for a fund and its firm.

Portfolio pages first: on an organization's own portfolio, investments or "our brands" page, first give an owned_by claim from every listed company to the page's owner (holding "current", or "former" when the page marks it former in text). Only after that add other facts the entries state, such as a listed company's own brands. Such a page often states no relationship in words: it lists the companies under a heading like "Portfolio Companies" on the owner's own site (the domain in the document's URL), each entry only describing the company. Every listed company is still a holding of the site's owner, and its claim quotes the company's own entry.

Only the page owner's own holdings count. Give no claim at all, not even a former one, for entries in a section the page says are something else: deals its people made at earlier firms (a heading such as "Prior to [the firm's name]", "Prior Firm Investments", "Team Experience" or "Investments made by our partners at previous firms"), deals the page owner advised on, or companies it lent to or arranged financing for. A person's biography that names companies they worked at, or deals they did at another firm, gives no claim. A deal that an adviser describes in words ("advised Cortec Group on its acquisition of Acme") is reported like any other statement.

Every company mentioned: report ownership facts about every company or brand the document mentions, not only its main subject. A page about one company that lists the brands it owns or operates ("Acme Group operates more than 200 stores under the brands Alpha Market, Beta Foods and Gamma Fresh") gives a claim for each, and a portfolio page gives a claim for every company on it. A document can state several ownership facts about the same company; report each (a company that is family-owned and has agreed to be acquired gives both claims).

Sellers and exits: when a document names a seller ("acquired the company from affiliates of Wafra Inc."), or an owner says it sold or exited, or a portfolio page lists the company as realized, exited, past or former, give owned_by with holding = "former", dated like the sale. A stated stake of 0% is an exit. Use holding = "former" only when the quote itself states the sale, exit or past ownership; a quote describing the company as a subsidiary or holding says it is current as of that document. If the same quote says the seller keeps a stake ("will retain a minority interest"), give only the current claim with that stake. An agreed sale that has not closed is not an exit: while the document says the deal is pending or expected to close, the seller's owned_by stays current and the buyer's acquired_by is announced; give holding = "former" only when the document says the sale closed. A business, brand or business line the document says was shut down, closed or discontinued gives owned_by with holding = "former" from it to the company that ran it, dated at the closing ("opened Acme Grooming studios in 2018 and closed them in 2021" gives former, 2021).

Deals: on acquired_by, set deal_status to "completed" when the document says the deal closed or was completed or that the buyer acquired or invested in the company; "announced" when it is agreed, planned or pending ("has agreed to acquire", "will acquire", "entered into a definitive agreement", "decision to acquire") and the document does not say it closed; "terminated" when it was called off. expected_close_text is the phrase saying when an announced deal is expected to close ("expected to close in the first half of 2027", "in the coming weeks"), copied from the claim's own quote; never the document's date; null when the quote has no such phrase.

Trademarks and licenses: a brand belongs to whoever owns its name. A statement that a brand's name or trademark belongs to a company ("Culturelle®, AZO®, and Estroven® are trademarks of dsm-firmenich group", "we own the Dollar General® mark", "Applebee's® is a registered trademark of Applebee's IP LLC") gives owned_by (the brand -> that company), holding "current", with the company named exactly as written, even when it is a company that only holds the name. When a document says a brand is licensed or used under license ("KitchenAid® is a registered trademark of Whirlpool, used under license"), give owned_by from the brand to the licensor, the owner of the name, and no claim to the licensee, the company that makes or sells products under it. If a brand list says some of its brands are licensed without saying which, give no claim for the brands it does not mark. A general statement that names no brand ("we own a number of trademarks") gives nothing.

Not ownership: these give no claim.
- Words that name no owner: "privately owned", "privately held", "independent", "independently owned".
- Words about who runs a business: "run by family", "family-operated", "family-run". Only words about who owns it ("family-owned", "employee-owned") give an owner.
- "X, an affiliate of Y" by itself, even inside a deal announcement ("Acme Home, Inc., an affiliate of Acme Retail, LLC, will acquire Beta Inc."): affiliates share an owner, and neither owns the other. "Affiliate" counts only in two cases: an owner or seller named as an affiliate of Y ("backed by an affiliate of a private equity firm", "acquired the company from affiliates of Wafra Inc."), and a company formed for a deal and defined in a deal document, as above ("Parent and Merger Sub are affiliates of Bansk Group").
- Stores, clinics, pharmacies or practices described as franchised, "independently owned and operated", "locally owned", or owned and operated by local dentists, doctors or entrepreneurs: these say who runs the locations, not who owns the brand.
- Providing services or support to offices, practices or stores ("support services to over 600 dental offices, including Alpha Dental and Beta Dental"): the provider does not own those brands unless the document says it owns or operates them or lists them as its own brands.
- Lending, loans, financing, credit facilities, and advisory or consulting work.
- Copyright lines ("© 2026 Acme Holdings LLC. All rights reserved.").

Long documents: read the whole document. Annual reports and filings state ownership in many places: brand lists ("Our Power Brands: ..."), acquisitions ("since its 2022 acquisition"), subsidiaries, and holders of the company's own shares. Report every ownership fact you find, each with its own quote.

Stakes: never compute or infer a stake percentage. Set stake_pct only when the document states that owner's percentage of the company, such as "holds 32% of the shares". A percentage about something else, such as "reinvested 100% of their interests" or "100% of the proceeds", is not a stake. Set stake_type to "majority" or "minority" only when the document uses that word about that owner. Set stake_basis to "voting" or "economic" only when the document says which. Otherwise leave them null.

Portfolio and brand pages: a company listed on an owner's portfolio or "our brands" page is a current holding (holding = "current") unless the page marks it former in its text. If a page says it mixes current and former holdings without marking which is which, give no claim for the unmarked items.

Quotes: verbatim_quote must be one unbroken stretch of the document, copied exactly, character for character: same words, spelling, punctuation and capitalization. Never skip, reorder or reword anything between its first and last word, even in long filings ("100% of the equity interests" is not "100% of the issued and outstanding equity interests"). Do not fix typos, do not join separate sentences or lines, and do not paraphrase. Copy link and image text exactly as it stands at that spot, even when the same words repeat across the page ("[link: Learn more]" stays "[link: Learn more]"). If two facts you need sit far apart, make separate claims with separate quotes. Keep quotes short: the single clause or sentence that states the fact, ideally under 250 characters. In long filings, copy one clause instead of a long sentence. Copy the characters from the document; never retype a quote from memory. The quote must name the claim's subject, as the document writes it or by a name the document defines for it (such as "the Company" in a filing). On a company's own site (the domain in the document's URL), in the site's own voice, such as its about, FAQ, history or brands page, "we", "us" and "our company" name the site's owner: the quote may use them, and the claim gives the owner's name as the page writes it elsewhere ("We are proud to be family-owned" on Acme Car Wash's own FAQ gives Acme Car Wash owned_by family). This does not apply to quoted speech, or to a press release or article posted on the site, where "we" may be someone else. Never quote a heading, a section title or a general phrase that does not name the subject, such as "our family of great local brands"; on a list page, quote the subject's own entry. Prefer a sentence that states the relationship ("WhiteWater Express Partners with Freeman Spogli & Co.", "the Company has grown to include ... Charlotte Russe"); when only a list shows it, quote the shortest unbroken stretch that contains the subject's name and, where the page gives it right there, its status ("Pet Food Express Investment Date: May 2022 Status: Current", "[link: Visit Food Lion]"). Never use the page title as the quote when the entry itself says more, and never the bare name alone when the page offers more. The quote must also name the owner, unless the owner is the organization publishing the page and the page lists its own holdings (a brand's entry on its owner's "Our brands" or portfolio page). For renamed_from, the quote must contain the former name. A computer checks every quote against the document and discards any that do not match exactly.

Dates: event_date is the date the quote or its document gives for the event (the closing or announcement date for acquired_by; the as-of date the quote states for owned_by), written as YYYY-MM-DD using the first day of the period, with event_date_precision "day", "month" or "year" ("2019" is 2019-01-01 with precision "year"). Never make a date more precise than the text: "later that year" or "in 2012" is 2012-01-01 with precision "year"; use a month or day only when the text gives it. If no date is given, both are null.

OWNER DESCRIPTIONS

For each owner named in a claim, if the document describes what kind of organization it is ("a leading private equity firm", "a family-owned holding company", "a publicly traded company"), give owner_name exactly as written, phrase as written, and a verbatim_quote containing the phrase, following the same quote rules. Do not classify the owner yourself.
```

## Schema

```json
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "claims",
  "owner_descriptions"
 ],
 "properties": {
  "claims": {
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "subject_name",
     "subject_is_family",
     "predicate",
     "object_name",
     "object_is_family",
     "verbatim_quote",
     "event_date",
     "event_date_precision",
     "value"
    ],
    "properties": {
     "subject_name": {
      "type": "string"
     },
     "subject_is_family": {
      "type": "boolean"
     },
     "predicate": {
      "type": "string",
      "enum": [
       "acquired_by",
       "owned_by",
       "managed_by",
       "renamed_from"
      ]
     },
     "object_name": {
      "anyOf": [
       {
        "type": "string"
       },
       {
        "type": "null"
       }
      ]
     },
     "object_is_family": {
      "type": "boolean"
     },
     "verbatim_quote": {
      "type": "string"
     },
     "event_date": {
      "anyOf": [
       {
        "type": "string"
       },
       {
        "type": "null"
       }
      ]
     },
     "event_date_precision": {
      "anyOf": [
       {
        "type": "string",
        "enum": [
         "year",
         "month",
         "day"
        ]
       },
       {
        "type": "null"
       }
      ]
     },
     "value": {
      "type": "object",
      "additionalProperties": false,
      "required": [
       "stake_pct",
       "stake_type",
       "stake_basis",
       "holding",
       "deal_status",
       "expected_close_text",
       "former_name"
      ],
      "properties": {
       "stake_pct": {
        "anyOf": [
         {
          "type": "number"
         },
         {
          "type": "null"
         }
        ]
       },
       "stake_type": {
        "anyOf": [
         {
          "type": "string",
          "enum": [
           "majority",
           "minority"
          ]
         },
         {
          "type": "null"
         }
        ]
       },
       "stake_basis": {
        "anyOf": [
         {
          "type": "string",
          "enum": [
           "voting",
           "economic"
          ]
         },
         {
          "type": "null"
         }
        ]
       },
       "holding": {
        "anyOf": [
         {
          "type": "string",
          "enum": [
           "current",
           "former"
          ]
         },
         {
          "type": "null"
         }
        ]
       },
       "deal_status": {
        "anyOf": [
         {
          "type": "string",
          "enum": [
           "announced",
           "completed",
           "terminated"
          ]
         },
         {
          "type": "null"
         }
        ]
       },
       "expected_close_text": {
        "anyOf": [
         {
          "type": "string"
         },
         {
          "type": "null"
         }
        ]
       },
       "former_name": {
        "anyOf": [
         {
          "type": "string"
         },
         {
          "type": "null"
         }
        ]
       }
      }
     }
    }
   }
  },
  "owner_descriptions": {
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "owner_name",
     "phrase",
     "verbatim_quote"
    ],
    "properties": {
     "owner_name": {
      "type": "string"
     },
     "phrase": {
      "type": "string"
     },
     "verbatim_quote": {
      "type": "string"
     }
    }
   }
  }
 }
}
```
