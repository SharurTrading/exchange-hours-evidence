# Verification of the three remaining CME families — 2026-09-05

Raw: `verify-result.json`, `journal.jsonl`. Each family was independently re-verified
(every citation retrieved and checked) then adversarially challenged on its identity verdict.

## A RETRIEVAL BREAKTHROUGH — use this everywhere from now on

**cmegroup.com serves normally to curl if you send a full browser header set**: User-Agent +
Accept + Accept-Language + Referer + Sec-Fetch-Dest/Mode/Site + Upgrade-Insecure-Requests.
The blanket "CME 403s automated clients" note in the plan and in `sources.md` is therefore too
strong — it 403s a *bare* curl.

Two machine-readable CME endpoints were found, and they are far better than scraping:
- `https://www.cmegroup.com/CmeWS/mvc/ContractSpecs/List/productId/<N>` — the spec API. Returns
  the exact `TradingHours` strings the product page renders.
- `https://www.cmegroup.com/services/trading-hours-by-product?id=<N>&fromEventDate=&toEventDate=`
  — the session-event API: per-day `preopen` / `open` / `closed` events with trade dates. This
  settles queue windows, the no-Friday-reopen shape, and holiday behaviour directly.

This closes the plan's standing complaint that archived spec pages from ~2015 are useless.

## 1. CME Weather — READY TO IMPLEMENT
Grid **CONFIRMED**. Revisions **8/8 CONFIRMED**. Confidence high.
`SER-9519` verified character-for-character: *"Effective Sunday, April 13, 2025, for trade date
Monday, April 14, 2025"*, expanding Globex from `17:00-15:15` to `17:00-16:00` CT. The date rests
on a **stated effective day**, not the notice's 2025-03-10 publication date.

**Verdict: ONE key `globex_weather`, scoped to FUTURES, excluding options.**
Folding was refuted with evidence, and the refutation is the crate's own law in miniature:
`globex_fx` and `globex_energy` both match weather's *current* envelope byte-for-byte, and neither
matches its history (weather ran to 15:15 until 2025-04-13). **Three keys, one envelope, three
histories.** Do NOT create a `globex_weather_options` key — its floor era starts before the audit
floor and ends only bracketed to (2023-03-08, 2023-09-29], so encoding either endpoint would
violate LAW-NO-FABRICATED-DATES.

Corrections the research file needs: a misstated source on claim (d); an overstated evidential gap
("no archived capture resolves the interval" is false — 11+ server-rendered captures do, through
2025-02-18); two brackets narrower than written; an incomplete rulebook-chapter list; and an
unrecorded ClearPort-hours change in SER-7606R.

## 2. Spot-quoted futures — READY, WITH TWO CORRECTIONS
Grid **CONFIRMED**. Revisions **5/5 CONFIRMED**. Confidence high.
**Verdict: ONE key `globex_spot_quoted` for all eight roots. HOLDS** — but the research's *grounds*
were false and must be restated before coding.

- **The stated reason is wrong.** The file says "there is no document in which the equity SQF grid
  and the crypto SQF grid differ." CME's own trading-hours service is that document, twice:
  half-day closes of **12:00 vs 13:45 CT on 2026-11-27** and **12:15 vs 12:45 CT on 2026-12-24**,
  splitting D1-D4 against D5/D6/D7/D9. One key is still right, but because holiday and early-close
  data is **caller-owned** (`exceptions.rs` ships none) and the *normal weeks* are identical — not
  because the grids never differ.
- **Effective-day off-by-one on both listing revisions.** `SER-9506R`: *"Effective Sunday, June 29,
  2025 for trade date Monday, June 30, 2025"*. The first executable Sunday session is
  **2025-06-29**, not 06-30. Same shape for **2025-12-14** (QSOL/QXRP).
- CME's notice index lists SER-9630RR's effective date as its *posting* date, disagreeing with the
  document body. Trust the body.

## 3. Event contracts — NOT READY. DO NOT IMPLEMENT YET
Grid **UNREACHABLE**. Revisions 4/4 confirmed, but the *shape* does not survive challenge.

The verdict was SEVEN keys (six by daily termination time T, plus ECBTC). The challenge's strongest
counterargument is decisive and unresolved:

> **The six T values may be contract EXPIRIES misread as session closes.** Nothing in any retrieved
> document states a Monday-Thursday session *close* at T. SER-8968R states a weekly range
> ("Sunday 5:00 p.m. - Friday 3:00 p.m."), a queue, and a relist time. The daily dark window from T
> to 16:45 — which is the entire basis of the six-way split — is **derived, never quoted**.

Under this repo's law the regular/extended classification and the session boundaries must be
sourced, not inferred. So the six-way split cannot be coded on present evidence. What is needed is
a document stating a daily session close, distinct from the contract's termination-of-trading time.

Other defects found: a misquote attributed to SER-8968R; a false "byte-identical" claim between the
2024-03-30 and 2025-09-16 captures; three dated Saturday maintenance extensions on channel 329 that
the file's grid omits; and a scope-warning date resting on a document date rather than an effective
day.

## Implementation order
1. **Weather** — one key, futures-scoped.
2. **Spot-quoted** — one key, with the restated rationale and the corrected 2025-06-29 / 2025-12-14 dates.
3. **Event contracts** — blocked pending a source that states a session close rather than an expiry.


---

# CORRECTIONS, 2026-09-06 — two of this file's conclusions were wrong

## The SGX catalogue change log is a WEAKER source than this file claimed
A direct retrieval of the workbook (SGX's own CMS, no auth: `api2.sgx.com/content-api/` behind
`sgx.com/titan-dt-dc-portal`, v17.5 and v17.6, `read_me` sheet byte-equivalent across both) shows:

- **"Effective 11 Nov:" is at cell E87, a row with NO date and NO version.** It is not on the v6.9
  row at all. The v6.9 row is R90 and its text (E90) says something else entirely, which this file
  never quoted.
- **This file's v6.9 quote is not contiguous.** It splices E87 and E89 and silently drops E88
  between them.
- **There are no merged cells.** The only thing binding E87 to any issue date is *cell-border
  formatting* — rows 86-90 render as one bordered box whose date sits on the bottom line. That
  grouping looks sound and the same pattern repeats one box earlier, but it is drawn formatting,
  not a stated relation.

So dating the T+1 extension from this source needs **two stacked inferences** — first which block
E87 belongs to, from borders; then the year, from that block's date cell — before it yields
"11 Nov 2019". Under LAW-NO-FABRICATED-DATES that cannot key a revision row.

**Consequence: issue #45 stays open, and PR #44's undated Japan T-session transition stays
undated.** The optimistic reading above is withdrawn. The catalogue is still useful corroboration
and worth citing as evidence that a change occurred; it is not a document that states an effective
day.

## Event contracts: the six-way split is REFUTED, and the family is ONE key
The blocker recorded above is resolved, in the negative, by **SER-9624** (15 Oct 2025): five event
contracts with five *different* daily Termination-of-Trading times (10:00 / 11:00 / 13:00 / 15:00 /
16:00 ET) share **one** Trading Hours cell —
`CME Globex: Sunday 6:00 p.m. - Friday 5:00 p.m. ET with a daily maintenance period from
5:00 p.m. - 6:00 p.m. ET`, with Pre-Open `Sunday 5:00-6:00 p.m. ET, Monday-Thursday 5:45-6:00 p.m. ET`.

If termination were the session close that table would need five hours cells; it has one. CME's own
footnote defines Termination as "the Contract's Stated Expiration Time". Applied back to SER-8968R,
its six per-product end times are the six underlying settlement-period ends and carry no maintenance
clause — the expiry idiom, not the session idiom.

**So event contracts are ONE key on the standard 17:00->16:00 CT envelope, not seven.** The
proposed six-way split would have invented six grids from one.
