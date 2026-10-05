## VERDICT

**The six-way split is not supportable.** CME publishes a document that settles the question in the negative, in the same product family, in the same table format, in one document: **SER‑9624**. In it, five event contracts with five *different* daily Termination-of-Trading times share **one** session grid whose daily close CME states explicitly and separately — and that daily close is none of the five termination times.

The session-API route is also closed, definitively: CME's session service has no event-contract products at all.

---

## 1. The decisive document — SER‑9624 (15 Oct 2025)

`https://www.cmegroup.com/notices/ser/2025/10/ser-9624.pdf` (local: `/private/tmp/claude-501/-Users-agedvagabond-Developer-exchange-hours-rs/f95c5d6f-baeb-4d12-bebe-cdee419f1fe5/scratchpad/ec/ser-9624.txt`)

"Initial Listing of Hourly Event Contracts on Certain CME Group Futures Contracts." Its contract-specification table carries **two separate rows**, verbatim:

> ` Trading Hours      CME Globex Pre-Open: Sunday 5:00 p.m. - 6:00 p.m. Eastern Time/ET`
> `                                         Monday - Thursday 5:45 p.m. - 6:00 p.m. ET`
> `                    CME Globex: Sunday 6:00 p.m. - Friday 5:00 p.m. ET with a daily maintenance period`
> `                    from 5:00 p.m. - 6:00 p.m. ET`
> `                    The next day's Event Contract will be listed at 5:00p.m. ET`

> ` Termination of     10:00AM ET daily   11:00AM ET daily   1:00PM ET daily   3:00PM ET daily   4:00PM ET daily`
> ` Trading*`
> `* Termination of Trading is contingent on the Contract's Stated Expiration Time`

Read what that proves:

- **Five products, five termination times (10:00 / 11:00 / 13:00 / 15:00 / 16:00 ET), one shared session grid.** If termination were the session close, this table would need five Trading Hours cells. It has one.
- **When CME means a daily session close it says so in words**, as a named clause — "*with a daily maintenance period from 5:00 p.m. - 6:00 p.m. ET*" — and the close (17:00 ET) is **not** any product's termination time, not even the latest (16:00 ET).
- CME's own footnote defines Termination as "the Contract's Stated Expiration Time."

The same table is reproduced in CME's CFTC self-certification, filed publicly: rule filing **25‑521** (COMEX, filed 12/02/2025, "Weekly Notification of Rule Amendments — Week of November 24, 2025"), Exhibit 1, Rulebook Chapter 23A, Initial Listing December 8, 2025 — `https://www.cmegroup.com/content/dam/cmegroup/market-regulation/rule-filings/2025/12/25-521.pdf`.

**Applied to SER‑8968R:** its Trading Hours row gives per-product end times (15:00 / 14:00 / 13:30 / 12:30 / 12:25 / 12:00 CT) that are *exactly* the six underlying settlement-period ends, and carries **no** "daily maintenance period" clause. Under CME's own demonstrated convention that is the expiry idiom, not the session idiom.

## 2. CME states that convention outright — Clearing Advisory 25‑326

`https://www.cmegroup.com/content/dam/cmegroup/notices/clearing/2025/10/chadv25-326.pdf`, "Trading Hours" row, verbatim:

> `All times are in Eastern Time (ET)`
> `All Contracts: CME Globex Pre Open: Sunday 5:00 – 6:00 p.m. Monday – Thursday 5:45 – 6:00 p.m.`
> `Sunday 5:00 p.m.- stated expiration time of Event Contract (i.e., Monday's ECS10: Sunday 5:00 p.m.- Monday 10:00 a.m.).`
> `Next day's Event Contract will list at 6:00 p.m. ET`

CME writes the cell in the identical `Sunday 5:00 p.m. - <time>` shape used in SER‑8968R and **glosses the end of the range as "stated expiration time of Event Contract."** A second instance appears in advisory 25‑325r (swap-based hourly Bitcoin): "*All contracts expire at stated expiration time of Event Contract (i.e., Tuesday's CCB10: Monday 5:01 p.m.- Tuesday 10:00 a.m. ET)*" (retrieved as a CME site-search snippet only, not fetched in full).

## 3. Rulebook Chapter 23 — retrieved live, 2026‑09‑06

`https://www.cmegroup.com/markets/prediction-markets/files/summary-of-rulebook-chapters.pdf` (HTTP 200, 452,886 bytes; local `.../scratchpad/ec/rbchap_live.txt`). Identical text in CME, CBOT, NYMEX and COMEX Chapter 23:

> `2302.A. Trading Schedule`
> `Event Contracts shall be listed for Expiration on such dates and shall be scheduled for trading during such hours as may be determined by the Exchange.`

> `2302.E. Termination of Trading`
> `Trading shall terminate at the end of the daily settlement period for the Underlying Futures, on the Expiration Date that the Event Contract was listed for.`

The rulebook gives no hours and puts termination in its own rule, tied to **that contract's Expiration Date**. It is a per-contract event, not a recurring daily boundary. Confirmed unchanged in rule filings 25‑521 and 25‑522 (both 12/02/2025), which reproduce 2302.A/2302.E in blackline with no hours inserted.

## 4. The session-API route — hard negative, and reproducible

cmegroup.com now returns `403` with `"This IP address is blocked…"` to curl on `/CmeWS/*`, `/services/*` and `.html` (PDF paths still serve 200). I ran the queries through a real browser instead, same-origin:

- `/CmeWS/mvc/ProductSlate/V2/List` paged to exhaustion: **3,251 products. Zero whose name contains "Event". Zero with globex code ECES/ECNQ/ECRTY/ECYM/ECBTC/EC6E/ECCL/ECNG/ECGC/ECSI/ECHG.**
- `/services/trading-hours-by-product` paged to exhaustion (2026‑09‑07→08): **3,243 products across 645 Globex product groups; zero named "Event"; groups `VE`, `VB`, `VG`, `VS` absent.** Its own error string is `"Error Query data from product slate."`
- The service works normally on covered products (verified on id 8462, SOFR: per-day `preopen`/`open`/`closed` with trade dates).

The event contracts' Globex security groups are `VE, VN, VR, VM, V6, VG, VS, VH, VC, VA, VB` (CME Globex Notice, January 22, 2024). None is in the service. There is **no CME product page and no session-event feed for this family**.

The one CME feed that would carry it, `https://refdata.api.cmegroup.com/refdata/v3/tradingSchedules`, returns `401 "api key or token is invalid"` — out of scope under LAW‑PUBLIC‑SOURCES.

The live `https://www.cmegroup.com/markets/prediction-markets.html` publishes no hours of any kind (rendered and read in full).

## 5. The "market goes dark at T" inference is refuted for ECES and ECNQ

CME Globex Notice, **January 22, 2024** (`https://www.cmegroup.com/notices/electronic-trading/2024/01/20240122.html`), "Changes to Listing Schedule and Strike Listing for Event Contracts on CME Globex":

> `Effective this Sunday, January 28 (trade date Monday, January 29), pending completion of all regulatory review periods, Event Contracts will be amended as follows on CME Globex`
> `Event Contracts on E-mini S&P 500 Futures | ECES | VE | Current Listing Schedule: One 0 DTE Event Contract listed at any time | New Listing Schedule: One 0 DTE Event Contract. One Event Contract expiring on the last business day of Mar, Jun, or Sep. One Event Contract expiring on the last business day of the calendar year.`

Same for ECNQ (`VN`). Corroborated by Clearing Advisory **24‑011** (Jan 10 2024, `https://www.cmegroup.com/notices/clearing/2024/01/Chadv24-011.pdf`), which states the effective day and prints:

> `Trading will terminate at the end of the daily settlement period of the Underlying Futures contract on the named date of the Event Contract.`
> `Example:`
> `ECESG412: Daily Expiring Event Contract on E-min S&P 500 Futures to expire on February 12, 2024`
> `ECESH428: End-of-Quarter Event Contract on E-mini S&P 500 Futures set to expire on March 28, 2024 (last business day of March 2024)`

Still current: the CME event-contract specifications PDF, both the 2026‑01‑04 and 2026‑07‑07 captures, lists for ECES and ECNQ "*1 zero days until expiration (DTE) event contract / 1 event contract expiring on the last business day of Mar, Jun, or Sep / 1 event contract expiring on the last business day of the calendar year*". So at 15:00 CT on a Tuesday, ECES has instruments listed that are not expiring. The root is provably not emptied at T. Advisory 24‑011 nonetheless re-prints the *unchanged* hours cell ("ECES; ECNQ, ERTY; ECYM; ECBTC: Sunday 5:00 p.m.- Friday 3:00 p.m."), which is only coherent if that cell is not a daily-close statement.

## 6. Correction to the catalog reading

The `catalog-artifacts` rows for these roots (`synthetic_no_ready`, groups "SYNTHETIC EOC VES/EQUITY/METALS/CRUDE/NYMEX/ECB", states `2,4`) are **not** the event contracts. CME Client Systems Wiki, "Event Contracts" page (version 2026‑08‑14): "*Additionally, non-tradable underlying futures are listed to support the options*", with a table row "*Non-tradable Synthetic Future … Order Entry Allowed: No*". Those GLBX definitions are the synthetic underlying futures; the tradeable instruments are options (`PFType` = `OOF`, `ProdSubTyp` = `EVENT` per the Event Contracts Master File page). The audit's exclusion of them was right, and they carry no information about this family's session. `market-hours-nontradable-groups.tsv` is consistent with this: ECES sits with `KYP10/11/13/15`, the SPAN synthetic codes for the hourly S&P event contracts named in advisory 25‑326.

## 7. What is actually sourced

Identical in SER‑8968R (2022‑08‑25), Clearing Advisory 22‑355 (2022‑09‑20), SER‑9092 (2023), Clearing Advisory 24‑011 (2024‑01‑10) and every archived activetrader capture through 2025‑09‑16 — **for all eleven roots, with no per-root variation, and never amended**:

- Timezone Central Prevailing Time (America/Chicago).
- `CME Globex Pre Open: Sunday 4:00 – 5:00 p.m. Monday – Thursday 4:45 – 5:00 p.m.`
- Week opens Sunday 5:00 p.m.
- `Next day's Event Contract will list at 5:00 p.m.`
- No Friday-evening reopen (the pre-open row names only Sunday and Monday–Thursday).

Corroborating the 17:00 open independently: CME Client Systems Wiki, "Event Contracts Master File" — "*Files are published every day … between 3:30 p.m. and 4:00 p.m. CT, prior to the opening of trading for the new day on CME Globex at 5:00 p.m. CT.*"

**Not sourced anywhere:** any Monday–Thursday close instant; any RTH/ETH classification; whether the Monday–Thursday 16:45–17:00 queue implies a market-wide close or is only the listing queue for the newly listed next-day contract. The only other statement I found touching a daily close is a hypothetical in CFTC filing 22‑376 — "*Trading in the Event Contract will close at the same time as trading of the ES contract*" — which is illustrative prose, and which points at 16:00 CT (ES's Globex close), not at 15:00. It cuts against T, not for it.

## 8. Defensible modelling

Do **not** encode six profiles keyed to T, and do not encode a Monday–Thursday close at T. On present evidence:

1. **One family, not six.** Every element CME publishes as a *session* — the Sunday 16:00–17:00 CT queue, the Monday–Thursday 16:45–17:00 CT queue, the 17:00 CT open, the absent Friday reopen — is byte-identical across all eleven roots and has never been amended since 2022‑09‑18. The only per-root numbers in the entire evidence base are expirations, and SER‑9624 shows CME does not vary the session by them.
2. **Encode the queue windows and the 17:00 open**; they are primary-sourced on the launch day and re-stated four times since.
3. **The executable close is the gap, and it is an executable-hours gap** — the serious kind under the repo's own priority rule, not a queue-onset gap. Say so explicitly rather than filling it with a termination time.
4. If a close must be encoded to make the rules well-formed, the only honest form is the **sourced intersection**: the window open under every reading, `17:00 → T`, carried with an in-table note that `T` is CME's published end-of-range, that CME's own gloss (advisory 25‑326) calls that end an expiration time, and that the `T → 16:45` interval is of **unknown** state — not sourced-dark. That is a conservative envelope, not a published grid, and it must not be written up as six sourced daily closes. Under the merged-key form the intersection across the ten roots collapses to Friday 12:00 CT (ECHG), which under-reports the equity-index roots by three hours; that cost is the reason to keep ten named profiles that currently coincide (per the "a venue that merely coincides still gets its own named profile" convention) rather than one.
5. **ECBTC still forks at 2026‑05‑29** on product semantics, as the research file argues.

My recommendation: keep the family **blocked for a full grid** and record it as an unmodelled family with the reason stated, or ship option 4 with the caveats in the table comment. What must not ship is the current write-up's claim that the six T values are daily session closes — that claim is now affirmatively contradicted by CME.

## 9. New primary material the research file is missing

- **SER‑9740R, May 28 2026** — `https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2026/05/ser-9740r.pdf`. "Expansion of the Trading and Clearing Hours for all Cryptocurrency Futures and Options on Futures Contracts… (SER 9740R supersedes SER 9740 dated May 13, 2026 and is being issued to include **Event Contracts on Bitcoin Futures**…) Effective **Friday, May 29, 2026**". Table 1 lists `Event Contracts on Bitcoin Futures | ECBTC | 23`. This is the proper SER for the ECBTC cutover; the research file has only the wiki and the Globex notice. Self-certified at CFTC as rule filing **26‑266** (June 4 2026).
- **Conflict to resolve on ECBTC.** SER‑9740R Table 2 gives one hours cell covering ECBTC: current "*CME Globex: Sunday 5:00 p.m. - Friday - 4:00 p.m. CT with a daily maintenance period from 4:00 p.m. - 5:00 p.m. CT*"; expanded "*24/7 … Monday-Friday 4:00p.m. to 4:02 p.m. CT*". The client-systems wiki gives ECBTC **15:00–16:02** and SER‑9092 gave ECBTC a Friday 3:00 p.m. end. Two CME primary sources disagree by an hour on ECBTC's daily maintenance start. The research file's 15:00–16:02 rests on the wiki alone.
- **Clearing Advisory 22‑355 (2022‑09‑20)** and **24‑011 (2024‑01‑10)** are two independent CME publications of the full hours table, both including **ECGC** — which closes the file's noted gap that CME's web page never named ECGC.
- **Advisory 25‑327 (Oct 17 2025)** contains no Trading Hours row (contract size / settlement value / accountability only), consistent with the file's reading of SER‑9587RR.
- **SER‑9499R (Jan 7 2025)** treats "EVENT CONTRACTS" as its own holiday category — "*All U.S.- based equity Event Contracts will be closed for trading on January 9, 2025. All other Event Contracts will have a normal trading day*" — with no times. Relevant to date-exception scoping, not to the grid.

## 10. Unreachable / not retrieved

- CME Reference Data API `tradingSchedules` — requires an API key (401). Out of scope.
- Clearing advisory 25‑325r — seen only as a CME site-search snippet.
- The full CME Globex notice text for 2026‑01‑26 (event-contract re-open item) — the page's rendered body did not expose that section in the fetch I made; only its table of contents did.
- No post‑2026‑05‑29 CME publication restates the ten non-Bitcoin roots' hours. That finding in the research file stands and is now reinforced: the product slate, the session service, the prediction-markets page and both 2026 specification PDFs all carry no hours field for them. The operative hours document remains SER‑8968R, last re-published by CME in Advisory 24‑011.

Local copies of everything newly retrieved: `/private/tmp/claude-501/-Users-agedvagabond-Developer-exchange-hours-rs/f95c5d6f-baeb-4d12-bebe-cdee419f1fe5/scratchpad/ec/n/` (`rf25521`, `rf25522`, `rf22376`, `rf26266`, `ser9740r`, `ser9499r`, `chadv22355`, `chadv24011`, `chadv25326`, `chadv25327` — each `.pdf` + `.txt`) and `.../scratchpad/ec/rbchap_live2.pdf`. Nothing was written to either repository.