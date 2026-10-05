Retrieved and verified. Final answer below.

## 1. Retrieval — succeeded, from SGX itself

`https://www.sgx.com/titan-dt-dc-portal` is a JS shell; its content comes from SGX's own CMS at `https://api2.sgx.com/content-api/?queryId=<CMS_VERSION>:page&variables={"path":"/titan-dt-dc-portal"}` (CMS_VERSION `09434be8973b96b28894aefc57aff9e6c1f8f9c6`, read from `https://www.sgx.com/config/appconfig.json`). That response contains a `download_widget` whose title is verbatim **`Derivatives Product Catalogue`**, holding exactly two items:

- `Derivatives Product Catalogue (v17.5) - Effective 20 Jul` → `.../2026-07/Derivatives%2BProducts%2BDescription%2Bv17.5%20eff%2020260720_2.zip`
- `Derivatives Product Catalogue (v17.6) - Effective 24 Aug, 7 Sep` → `.../2026-08/Derivatives%2BProducts%2BDescription%2Bv17.6%20eff%2020260824%2C%2020260907.zip`

Both downloaded (HTTP 200, no auth, plain curl with browser headers). Local copies:
- `/private/tmp/claude-501/-Users-agedvagabond-Developer-exchange-hours-rs/f95c5d6f-baeb-4d12-bebe-cdee419f1fe5/scratchpad/sgx/v176.zip` (md5 `4f988a6604883b111196d00890495225`) → `Derivatives+Products+Description+v17.6 eff 20260824, 20260907.xlsm`
- `.../scratchpad/sgx/v175.zip` (md5 `bc1374e329d8b794df876d34e6fdf9c9`) → `Derivatives+Products+Description+v17.5 eff 20260720.xlsm`

The `read_me` sheet is byte-equivalent across the two files for every row discussed below.

## 2. The change-log table structure, verbatim

Header row 24: `B24` = **`Issue Date (mm/dd/yyyy)`**, `C24` = `Version Number`, `D24` = `Authors`, `E24` = `Change Description`. There is no fifth column — F–J are empty across the whole sheet except three stray whitespace cells (`J116`, `F124`, `G144`).

## 3. THE 2019 ROW IS WORSE THAN FINDINGS.md RECORDS

`Effective 11 Nov:` is **not** in the v6.9 row. It is at **E87, a row with no date and no version at all** (`<c r="B87" s="194"/>` — genuinely empty). Rows 86–89 carry description text only. Verbatim, cell by cell:

```
R85  B85 = 43739 (fmt mm-dd-yy → 10/01/2019)  C85 = 6.8  D85 = 'SGX'
     E85 = 'Add PW, PWF, CPW, PPW, CPWF, PPWF'
R86  B86 (empty)  C86 (empty)
     E86 = 'Editorial housekeeping/standardisation contract name on Freight contracts'
R87  B87 (empty)  C87 (empty)
     E87 = 'Effective 11 Nov:'
R88  B88 (empty)  C88 (empty)
     E88 = 'Editorial change Contracts_mainmenu:'
R89  B89 (empty)  C89 (empty)
     E89 = '(T+1) session Closing hours to 5:15am all T+1 traded contracts'
R90  B90 = 43745 (fmt mm-dd-yy → 10/07/2019)  C90 = 6.9  D90 = 'SGX'
     E90 = 'Editorial change session_mainmenu:
            SURV_INT to 5:15, REMOVE_DAY_ORDERS to 5:20, SERIES_GEN to 5:22, 
            CLS_CLEAR to 5:25 and CLOSE to 5:30 all T+1 traded contracts'
```

Two corrections to `FINDINGS.md`:
- Its v6.9 quote **is not contiguous** — it splices E87 and E89 and drops E88 between them.
- The cell that actually sits on the v6.9 row (E90) says something else entirely, and FINDINGS.md never quotes it.

**Binding E87 to a date requires a second inference before the year inference even starts.** There are **no merged cells** anywhere in `read_me`. The only thing tying E87 to an issue date is cell borders: `B86:E86` has a thin top border and no bottom; 87, 88, 89 have neither; `B90:E90` has a thin bottom. So rows 86–90 render as one bordered box whose date cell sits on its bottom line. The same pattern holds one box earlier (83–85 → `10/01/2019`, v6.8). That is a real, document-internal structural signal and I regard the block grouping as sound — but it is drawn formatting, not a stated relation, and it must be declared as the basis if this is ever cited.

## 4. Verbatim contents of the other two rows

```
R163 B163 = 45600 (fmt mm-dd-yy → 11/04/2024)  C163 = 14.2  D163 = 'SGX'
     E163 = 'Amend trading hours of SGX Nikkei Derivatives and SGX FTSE Blossom Japan Index Futures (eff 4 Nov)'

R170 B170 = 45735 (fmt mm-dd-yy → 03/19/2025)  C170 = 14.9  D170 = 'SGX'
     E170 = 'Amend T+1 session trading hours for SGX Equity Index Futures/ Options, Dividend Index Futures and United States Single Stock Futures (US SSFs) (eff 7 Apr)'
```

Both are single-row entries with a full thin border box each — their date binding is unambiguous, unlike the 2019 case. Note `E170`'s exact spacing: `Futures/ Options` (space after the slash); FINDINGS.md renders it `Futures/Options`.

## 5. Is the year stated anywhere retrievable? **No.**

I checked every channel you named and several more, on both files:

| Channel | Result |
|---|---|
| The `eff` text itself | No year in E87, E163, E170 |
| Any other column | F–J empty sheet-wide (3 whitespace cells only) |
| Sheet header/footer (print) | All six header/footer slots empty |
| Document properties | `creator` `Jovan Ang`; `title` `Derivatives Products Description`; `lastModifiedBy` `Teo Hui Ning`; `created` 2015-11-26; `modified` 2026-08-28 (v17.6) / 2026-07-14 (v17.5). No effective-date property. |
| Cell comments/notes | `read_me` has none. The workbook's only two comment parts belong to `contracts_mainmenu` and `contracts_data`, both reading `Joyce Goh / Max no of quarter strips listed for trading / Max no of cal strips listed for trading` |
| Hidden rows/columns in `read_me` | None (`hidden` empty for both dimensions) |
| Hidden sheets | Five exist (`DormantDelist`, `Non-Tradable Indexes`, `Futures Strategies`, `contracts_writeup_data`, `dropdownlist_data`) — none carries change-log dates |
| Defined names | Five, all dropdown OFFSET ranges |
| Adjacent rows | The only year-bearing cells near the 2019 block are the Issue Date column: `10/01/2019` (R85), `10/07/2019` (R90), `11/08/2019` (R91) |
| Older editions of the workbook | The portal publishes only the current two. Wayback CDX returns **zero** captures for any `Derivatives*Products*Description*` file under `api2.sgx.com`; archived portal HTML captures (2021–2026) are JS shells containing no catalogue filenames. |

**The only year-bearing datum is the Issue Date column, and that is the issue date, not the effective date.** The header even says so verbatim: `Issue Date (mm/dd/yyyy)`.

## 6. Two things that weaken the "just take the next occurrence" inference

**The log's `eff` dates run both forwards and backwards from the issue date.** Parsing all 200 yearless `eff <day> <Mon>` mentions under a nearest-occurrence rule, the spread is **−77 to +60 days**. Concrete backdated examples, verbatim:
- R180, issue `10/06/2025`: `'... Amended the Last Trade Date of India SSFs effective for September contracts onwards (eff 21 July)'` — 77 days *before* issue.
- R197, issue `07/07/2026`: `'Amend NLT MVT for FVN and FID from 50 to 2 (eff 30 Apr), RT from 60 to 2 (eff 13 Jul)'` — one backdated, one forward, in one cell.

So the document contains no rule that `eff` means the next occurrence. The inference is behavioural, not stated. (It does bound the year uniquely in practice — the alternative years sit ±365 days out, far outside the ±3-month observed spread — but that is inference about SGX's habits, not a date SGX wrote.)

**The log has typo-level defects.** `B108` (version 8.7) is not a date at all but the *text string* `'11/31/2020'` — 31 November does not exist. Also `E90` names a session state `CLS_CLEAR` while `session_mainmenu` row 34 labels it `CLS_SIGNAL`.

**Contrast worth noting:** when SGX means an effective date in this same publication chain it *does* write the year — the ZIP filenames are `... eff 20260720` and `... eff 20260824, 20260907`. The yearless form is confined to the change-log cells and the portal's display names (`Effective 20 Jul`).

## 7. Second-trap check on the 2019 content: this one is a genuine session boundary

`(T+1) session Closing hours` refers to the `contracts_mainmenu` field labelled verbatim **`Trading Session & Hours on SGX (From open to close, (SG Time)`**, which today reads e.g. `(T) 9:00am –4:35pm` / `(T+1) 4:45pm – 5:15am` for CN. The workbook keeps termination-of-trading in a *separate* field one row below, `Last Trading Day / Last Trade Time`. So 5:15am is a session close, not an expiry or settlement time.

But the same bordered block also carries `CLOSE to 5:30`, and `session_mainmenu` confirms the distinction: for a T+1 contract, `SURV_INT` = 05:15, `REMOVE_DAY_ORDERS` = 05:20, `CLS_SIGNAL` = 05:25, `CLOSE` = 05:30. 05:30 is a post-trading system state — the electronic-envelope tail, not the trading close. Anyone reading this block quickly could take 5:30 as the close. 05:15 is the correct number.

## 8. Answers to your two direct questions

**Is the workbook a primary SGX publication?** Yes, unambiguously. It is authored by SGX (the `Authors` column reads `SGX` on every row), hosted on `api2.sgx.com`, published from SGX's own `sgx.com` portal under SGX's own widget heading `Derivatives Product Catalogue`, and reachable with no authentication. It satisfies LAW-PRIMARY-SOURCES and LAW-PUBLIC-SOURCES.

**Can its change log date a revision under this project's law?** As currently written, **no** for 2019-11-11 and 2025-04-07, and **borderline** for 2024-11-04.

- LAW-NO-FABRICATED-DATES requires "an unconditional, **day-level** effective date". `Effective 11 Nov:` and `(eff 7 Apr)` state a day and a month. The year is supplied by the reader from a neighbouring cell that the document labels *Issue Date*. That is exactly the inference the law forbids from keying a revision row. For 2019 it is compounded: the effective-date cell has no date row of its own, and its attachment to `10/07/2019` rests on drawn cell borders.
- **R163 is different and the caller should weigh it separately.** Its own row's Issue Date is `11/04/2024` and its own text says `(eff 4 Nov)` — day and month coincide with the dated cell *on the same row*, inside a single-row border box. Nothing has to be carried across rows and no "next occurrence" rule is invoked; the row is internally self-consistent on one line. That is a materially stronger construction than the other two, though the four digits are still never typed.
- Independently of the year problem, note *what kind* of statement this is. The 2019 block is captioned `Editorial change Contracts_mainmenu:` and `Editorial change session_mainmenu:` — the workbook recording that **it** amended **its own printed fields**. It is a catalogue-maintenance log carrying an effective day, not the exchange's rule-change notice. It is good corroboration and a good dating *pointer*; it is not the notice itself.

**Net effect on the two issues:** the catalogue does not, on its own, close issue #45 (2019-11-11) or supply #44's undated 2024-11-04 cutover in the form the law requires. It does corroborate all three, and it independently confirms that a T+1 close change to 5:15am and a Japan trading-hours amendment both happened and were effective on an 11 Nov and a 4 Nov respectively. The residual work is unchanged: an SGX circular or notice that writes the year.