# SGX pre-2020 evidence sweep — findings

Raw: `sweep-result.json`, `journal-wf_4b4e4f3d-898.jsonl`, `artifacts/`.
Swept 2026-09-05. Five archive channels. Synthesis agent died on a usage limit; these
conclusions are read directly off the raw agent returns.

## HEADLINE: a previously unknown SGX-hosted primary source dates several cutovers

The **SGX Derivatives Product Catalogue** ships a `read_me` change-log sheet inside its
`Derivatives+Products+Description+vNN.N` workbook, published on SGX's own Titan DT/DC portal.
It is SGX-hosted, publicly reachable, and it states effective days. Retrieved independently
from two live catalogue files (v17.5 and v17.6).

Entries found, verbatim:

| catalogue version | doc date | verbatim entry | dates what |
| --- | --- | --- | --- |
| v6.1 | 2019-05-21 | "Amended trading hours for SGP, SGPO and ST eff 10 Jun" | MSCI Singapore suite, 2019-06-10 |
| v6.9 | 2019-10-07 | "Effective 11 Nov:" / "(T+1) session Closing hours to 5:15am all T+1 traded contracts" | **T+1 extension, 2019-11-11** |
| v14.2 | 2024-11-04 | "Amend trading hours of SGX Nikkei Derivatives and SGX FTSE Blossom Japan Index Futures (eff 4 Nov)" | **the Japan T-session extension #44 left UNDATED — 2024-11-04** |
| v14.9 | 2025-03-19 | "Amend T+1 session trading hours for SGX Equity Index Futures/Options, Dividend Index Futures and US SSFs (eff 7 Apr)" | corroborates the 2025-04-07 cutover landed in #44 |
| v3.3 | 2017-10-05 | "Change of Trading Hours" (bare label, no contracts, no date) | nothing |
| v3.6 | 2017-12-29 | "Change of Trading Hours for EM and NTR suite" | nothing |

### Two consequences

1. **Issue #45 is closeable.** The 2019 T+1 extension is dated 2019-11-11 by an SGX document.
2. **PR #44's remaining gap is closeable.** The Japan T-session extension, which #44 serves via a
   conservative sourced intersection because it was undated, is dated **2024-11-04** by the same
   source. It also independently matches the Phillip Nova third-party attestation #44 rejected
   (correctly, at the time) as a third-party assertion.

### CAVEAT that must be checked before encoding
The v6.9 cell says "Effective 11 Nov" **with no year written**. The year 2019 is inferred from the
block's own date cell (Excel serial 43745 = 7 Oct 2019) and adjacent blocks (v6.8 = 1 Oct 2019,
v7.0 = 8 Nov 2019). 11 Nov 2019 was a Monday. Under LAW-NO-FABRICATED-DATES this inference must be
re-verified directly before it keys a revision row. Same check applies to "eff 4 Nov" in v14.2 and
"eff 7 Apr" in v14.9.

## Corroboration (member notices — cannot date a row, but agree)
- Phillip Futures, 2019-11-08: "with effect from Monday, 11 November 2019, the Singapore Exchange
  will be extending its T+1 session close from 4.45am to 5.15am".
- HGNH International Futures, 2019-11-07 (Chinese) and Rakuten Securities, 2019-11-06 (Japanese):
  both state 2019-11-11.
- Phillip Futures, 2019-05-31: MSCI Singapore SGP T close 17:10 -> 17:20, T+1 open 17:40 -> 17:50,
  effective Monday 2019-06-10. This is the change that produces the 2020 calendar's SiMSCI grid.

## Newly discovered intermediate step — STILL UNDATED
The T+1 close ran **02:00** on the 2018-07-11 SGX page and **04:45** by the Phillip notice of
2019-05-31. So there is an intermediate 02:00 -> 04:45 step between those dates that **no retrieved
document dates**. The 2019-11-11 change is 04:45 -> 05:15, not 02:00 -> 05:15.
This means the pre-2020 history has at least THREE steps, not one.

## Hard negatives (verified, not assumed)
- **No SGX Derivatives Trading Calendar PDF exists in the Wayback Machine for 2016-2019.** The 2020
  edition is the earliest. The two PDFs linked from the 2018 hours page are not archived.
- The four Titan newsletters naming the change were **downloaded but are AES-128 password-encrypted**
  (`Command Line Error: Incorrect password`; `/EncryptMetadata true`). Contents unreadable.
  Their HTTP last-modified dates: 2019-07-16, 2019-08-28, 2019-10-08, 2019-11-05.
- **No DT/AM circular from 2019 or 2020 is archived** anywhere on sgx.com or api2.sgx.com. The only
  archived DTAM PDFs are from 2022 onward, plus one from 2006.
- The old derivatives hours page was already dead (301) by 2019-04-19, so no capture can witness the change.
- SGX rulebook does not state hours: Futures Trading Rule 4.1.5 defers to Contract Specifications,
  and Rule 8.1 says those "are distinct and separate documents which are not part of this Rules".
- No verbatim 2019 SGX circular exists on any member site.

## Additional dated grids retrieved
- 2013-08-20 portal capture: Nikkei 225 T 07:45-14:25 / T+1 15:15-02:00; FTSE China A50 09:00-15:55 /
  16:40-02:00; MSCI Singapore 08:30-17:10 / 18:15-02:00.
- A calendar in api2 folder `2019-01` (SGX date field 2019-01-23) shows T+1 close **04:45**.
  NOTE: this contradicts the "no 2016-2019 calendar archived" negative from another channel —
  RECONCILE BEFORE USE.

## Next actions
1. Re-verify the catalogue change-log entries directly (years are inferred; see caveat).
2. Reconcile the `2019-01` calendar claim against the "earliest is 2020" negative.
3. If both hold: date the 2019-11-11 and 2024-11-04 cutovers; #45 and #44's residual gap both close.
4. The 02:00 -> 04:45 step stays undated -> sourced intersection for that interval.
