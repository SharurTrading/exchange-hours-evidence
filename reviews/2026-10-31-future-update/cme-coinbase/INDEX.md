# CME and Coinbase source check — 2026-10-31 UTC

## Implemented CME finding

The five CME weekly Globex bulletins from 2026-09-28 through 2026-10-26 were retrieved directly and their full contents inspected. The October 5 bulletin adds an unconditional October 31 02:00–05:00 CT maintenance extension for 24/7 markets; October 12/19/26 repeat it. No later unconditional in-scope session change was found in these bulletins. The January 23, 2027 gold/silver multicast-channel migration changes connectivity, not a fully specified session arrangement.

The Bitcoin service (product 8478, group BF) was fetched for complete Friday-to-Tuesday windows around October 3, October 24 and October 31. It supplies exact Saturday Pre-Open times and the following Monday trade dates. `derive_october.py` reconstructs the complete Monday arrangements from those event streams and compares all 21 blocks against the crate; result: three rows, seven blocks each, matches true. Raw JSON is retained unchanged. The October 31 Saturday extension was already elapsed at this inspection; this corrects historical answers and the still-running Monday November 2 trade date.

## Coinbase bounded result

The live official market-notices page and the developer market-hours page were retrieved. The regular 23x5 energy/metals hours and 16:50–17:00 CT Pre-Open are unchanged. Newer market notice 26-33.3 of September 24 cancels the planned rolling-deployment/removal-of-Friday-maintenance transition and keeps the 16:00–17:00 CT Friday maintenance; this concerns the separately unmodelled 24x7 product set, not a change to the existing 23x5 default. Notice 26-37 specifies October 24 05:00 close, 13:50 Pre-Open and 14:00 reopen for 24x7 products; the crate default is already closed on that Saturday and no 24x7 family key is claimed. The current index supplied no newer 2026 Thanksgiving/Christmas schedule to extend the existing holiday horizon. No Coinbase runtime edit was made.

## Artifact inventory

`MANIFEST.json` records raw public source URL, exact UTC retrieval instant, byte count and SHA-256. Text files beside HTML/PDF are local readable extractions, not cited originals.

| File | SHA-256 | Bytes |
|---|---|---|
| `cme_globex_20261026.html` | `4437b14e5287982fcb50d272399e2bffd99469b61aea2d8fd411224479f483a7` | 177726 |
| `coinbase_market_hours.html` | `3f50bfe357eb91c27948111678c37b80a6a8ae3d3d8cb3bcd2cd1297cfba27ac` | 528101 |
| `coinbase_market_notices.html` | `46fcf224cb617ea3fd29e81dc6ede4edb262f68a7ac88e6d0672b41a8d613985` | 795742 |
| `cme_service_oct3.json` | `784668d4ebd69ad6051a29c1a72d4b76781b31d712ca3fd1b245617efc7ed473` | 1506 |
| `cme_service_oct24.json` | `9381985ebf35e61364d7dc43980ae8afd6bea5bba61dab82b74de2ea8cafd786` | 1506 |
| `cme_service_oct31.json` | `302d9c48d836ab6930af17be73fb215a06d3cdd5bf8cd034f861df9214d3861d` | 1506 |
| `cme_globex_20261019.html` | `464d7b60ca6562ae6417673463172ff046a57f4210032bbe7683ab1162d49728` | 175044 |
| `cde_notice_26-33.3.pdf` | `ac4f9f5da7d7174fa787834ad286575e3eeae5c7af1af08d0d34f46174763858` | 101118 |
| `cde_notice_26-37.pdf` | `97f2d841c43239aba313f7a4c594381767ffb759ee0a2bcc869c1de80f869754` | 97282 |
| `cme_globex_20260928.html` | `46bab83f42b1338864d4ec58094b87205aeffeb8e899e643d15644580e939a29` | 189847 |
| `cme_globex_20261005.html` | `20977144329a72c5586c03a287cd75c723872ff17e983eb661347cb4e7663f2d` | 182089 |
| `cme_globex_20261012.html` | `d0d8811eb26b56a529fa8032b9f28da2fc3e6630d011b3917d193756335a2a78` | 181177 |

## Count verification

A separately compiled public-API probe enumerated `holiday_on` for every civil date 2019-01-01 through 2027-12-31 and returned 89 rows. The complete module-date parser agrees: 86 baseline rows plus the three sourced October-weekend replacements. The earlier evidence prose said 87 for its baseline; that stale total is corrected.

## Reconciliation with current main

The initial working checkout was stale. After fetching and rebasing onto `origin/main` at `02a3c89495c4f7f9b51fab833fd04d2bc815f456`, all 98 upstream cryptocurrency exception rows and four audited coverage windows were preserved; this change adds three complete October Monday replacement rows, for 101 rows total. The October 31 matching-hours extension and October 3 replacement queue were already upstream. The newly added behavior is the October 24/31 queues and date-exception representation, including the detached normal-week contract. The September 19 07:45 Pre-Open, witnessed launch-era queues, launch-to-2018 window and resolved 2023-01-16 date remain intact.
