# Task: USPTO access and mark search

Type: task
Status: open
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

What access does the v1 USPTO licensing check need, and how does code find a brand's live registration from its name?

## Context

- Created 2026-11-18 in "Licensed names in v1" (Q6): USPTO joins v1 narrowly, one licensing check per brand in seven licensing-prone industries, about 210 brands ("USPTO trademark data: adopt as a source?", amended).
- HITL: the developer signs up. Facts from "Research: USPTO trademark data as an official source" ([findings](../research/uspto-trademarks.md) §2): the single-mark TSDR API needs a key from https://account.uspto.gov/api-manager/ (header `USPTO-API-KEY`); whether that key now needs an ID.me identity check is unconfirmed; the Open Data Portal API needs a USPTO.gov account plus ID.me and four profile fields; bulk files need a USPTO.gov sign-in; the website terms discourage automated high-volume use of the web pages.
- TSDR looks a mark up by serial or registration number, so code also needs a way to search by a brand's name (word mark, goods classes, live status) to find those numbers.

## Checklist

1. The developer creates a USPTO.gov account and requests a TSDR API key; note whether ID.me was required.
2. Claude (AFK, after the key exists, kept out of the repo) confirms with a handful of calls: a TSDR status lookup by serial returns the current owner; and which official route searches marks by name and goods class (ODP trademark search, or another documented API), with its key requirements and rate limits.
3. Record the key's storage location, the search route, limits and costs here.
