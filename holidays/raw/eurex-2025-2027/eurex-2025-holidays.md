# Eurex — 2025 holiday closures, and 2027 status (verbatim transcription)

Retrieved 2026-09-26 (UTC) for the `eurex` served identity, which currently ships only a
2026-01-01 .. 2026-12-31 holiday table (`EUREX-HOLREG-2026`) and therefore returns a coverage
error for all 365 dates of 2025.

Two independent T1 artifacts state the 2025 closures, and they agree:

* **A** — *Eurex trading calendar 2025* (PDF), `Eurex_Trading_Calendar_2025.pdf`,
  column headed **"Overview of holidays by countries"** on page 2.
* **B** — *Holiday regulations* page, `https://www.eurex.com/ex-en/trade/trading-calendar/holiday-regulations`,
  the **2025** section. Still live for **2026** only; the 2025 section survives in three 2025
  Wayback captures saved beside this file.

Neither artifact prints **any session-hours detail** — no early-close instant, no reduced
session, no late open. Both state closures as *scope* statements ("closed for trading …",
"closed for trading and clearing …") and nothing else. **No 2025 early close is sourced by
either artifact.** Every 2025 date is therefore either a full/partial closure named below or
an ordinary trading day.

---

## 1. The operator's recurring-grid table — "Non-trading days at Eurex 2025 - 2030"

Source **B**, verbatim heading and its column for 2025, with the operator's own weekday
names and its footnote. The operator prints these as **recurring named holidays with civil
dates**; the 2025 civil date is the second column.

> **Non-trading days at Eurex 2025 - 2030**
>
> | Holiday | 2025 (verbatim) |
> |---|---|
> | New Year's Day | Wednesday 01 Jan 2025 |
> | Good Friday | Friday 18 Apr 2025 |
> | Easter Monday | Monday 21 Apr 2025 |
> | Labour Day | Thursday 01 May 2025 |
> | Christmas Eve\* | Wednesday 24 Dec 2025 |
> | Christmas Day | Thursday 25 Dec 2025 |
> | Boxing Day | Friday 26 Dec 2025 |
> | New Year's Eve\* | Wednesday 31 Dec 2025 |
>
> `* No trading; clearing and settlement are open if the holiday is not on a Saturday or Sunday.`

The footnote is what distinguishes the two groups, and it matches the day-by-day table in
§3 exactly: the six unnamed-with-an-asterisk-free rows are *trading and clearing* closures;
`Christmas Eve*` and `New Year's Eve*` are *trading-only* closures with clearing and
settlement open.

## 2. Scope statements, verbatim from the Trading Calendar 2025 PDF (source A)

Page 2, column "Overview of holidays by countries", transcribed exactly as printed
(the German sentence is the operator's own mixed-language text; `Xetra@` is the PDF's own
rendering of the Xetra wordmark):

> Eurex is closed for trading and clearing (exercise, settlement and cash)
> in all derivatives: 1 January, 18 April, 21 April, 1 May, 25 December,
> 26 December
>
> Eurex is closed for trading in all derivatives: 24 December, 31 December
>
> Eurex is closed for trading and clearing (exercise and settlement)
> in Exchange Traded Products derivatives as well as British equity
> and equity index derivatives; no cash payment in GBP: 5 May, 26 May,
> 25 August
>
> Kein Handel und keine Ausübung in deutschen Aktien- und Aktienindex-
> derivaten sowie in ETF- und ETC-Derivaten, die auf Xetra@-Börsen-
> notierungen basieren: tba.
>
> Eurex is closed for trading and exercise in Finish equity and equity index
> derivatives: 6 January, 29 May, 20 June
>
> Eurex is closed for trading and exercise in Irish equity derivatives: 5 May
>
> Eurex is closed for trading and exercise in Italian equity derivatives:
> 15 August
>
> Eurex is closed for trading in Norwegian equity derivatives; no cash
> payment in NOK: 17 April, 29 May, 9 June
>
> Eurex is closed for trading in Danish equity derivatives; no cash payment
> in DKK: 17 April, 29 May, 30 May, 5 June, 9 June
>
> Eurex is closed for trading in Polish equity derivatives: 6 January, 19 June,
> 15 August, 11 November
>
> Eurex is closed for trading and exercise in Swedish equity derivatives;
> no cash payment in SEK: 6 January, 29 May, 6 June, 20 June

Note the operator prints "Finish" (sic) for Finnish.

### 2.1 The German (FDAX/FDXM-scope) note is `tba` for 2025 — the open scope question

The task asked whether the operator leaves additional German closures as "to be announced".
**Answer: yes, in the Trading Calendar PDF, for 2025.**

> Kein Handel und keine Ausübung in deutschen Aktien- und Aktienindex-
> derivaten sowie in ETF- und ETC-Derivaten, die auf Xetra@-Börsen-
> notierungen basieren: tba.

= *"No trading and no exercise in German equity and equity index derivatives as well as in
ETF and ETC derivatives based on Xetra listings: tba."*

So the 2025 edition names **no** German equity / equity-index (and Xetra-based ETF/ETC)
closure dates. The 2026 edition carries the same note, in English, and also still says
`to be announced`:

> Eurex is closed for trading and exercise in German equity and equity
> index derivatives as well as ETF and ETC derivatives which are based
> on Xetra® listings: to be announced

**The holiday-regulations page never carries this note at all** — neither the 2025 captures
nor the live 2026 page contain the words "German" or "tba" anywhere in their article body
(verified by full-text scan; the single `Xetra` occurrence on the page is a footer nav link).
The note exists only in the Trading Calendar PDFs.

Consequence for the crate: a German equity/equity-index closure set for 2025 and 2026 is
**expressly withheld by the operator** and is a genuine, operator-declared gap — not a
retrieval failure. It cannot be filled from these artifacts, and it must not be filled from
T3 restatements.

## 3. The day-by-day 2025 table, verbatim (source B, September 2025 state)

The complete 2025 table, 54 rows, exactly as the operator prints it. `No cash payment in XXX`
rows are printed by the operator and are **not** trading closures.

**37 of the 54 rows are trading closures and 17 are cash-payment-only notes.** A closure row
is marked ✅ below; the marker is added by this transcription, not by the operator.

| Date (verbatim) | ✅ | Verbatim text |
|---|---|---|
| 01 January | ✅ | Eurex is closed for trading and clearing (exercise, settlement and cash) in all derivatives. |
| 02 January | ✅ | Eurex is closed for trading and clearing (exercise and settlement) in Swiss fixed income as well as equity and equity index derivatives; no cash payment in CHF. No cash payment in JPY. No cash payment in NZD. |
| 03 January | | No cash payment in JPY. |
| 06 January | ✅ | Eurex is closed for trading and exercise in Finnish equity and equity index derivatives. Eurex is closed for trading and exercise in Swedish equity derivatives; no cash payment in SEK. Eurex is closed for trading in Polish equity derivatives. |
| 09 January | ✅ | Eurex is closed for trading in Brazilian, Canadian and U.S. equity derivatives. |
| 13 January | | No cash payment in JPY. |
| 20 January | ✅ | Eurex is closed for trading in Brazilian, Canadian and U.S. equity derivatives; no cash payment in USD. |
| 27 January | ✅ | Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW. No cash payment in AUD. |
| 28 January | ✅ | Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW. |
| 29 January | ✅ | Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW. |
| 30 January | ✅ | Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW. |
| 06 February | | No cash payment in NZD. |
| 11 February | | No cash payment in JPY. |
| 17 February | ✅ | Eurex is closed for trading in Brazilian, Canadian and U.S. equity derivatives; no cash payment in USD. |
| 24 February | | No cash payment in JPY. |
| 03 March | ✅ | Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW. |
| 20 March | | No cash payment in JPY. |
| 17 April | ✅ | Eurex is closed for trading in Norwegian equity derivatives; no cash payment in NOK. Eurex is closed for trading in Danish equity derivatives; no cash payment in DKK. |
| 18 April | ✅ | Eurex is closed for trading and clearing (exercise, settlement and cash) in all derivatives. |
| 21 April | ✅ | Eurex is closed for trading and clearing (exercise, settlement and cash) in all derivatives. |
| 25 April | | No cash payment in NZD. No cash payment in AUD. |
| 29 April | | No cash payment in JPY. |
| 01 May | ✅ | Eurex is closed for trading and clearing (exercise, settlement and cash) in all derivatives. |
| 05 May | ✅ | Eurex is closed for trading and clearing (exercise and settlement) in Exchange Traded Commodities as well as British equity and equity index derivatives; no cash payment in GBP. Eurex is closed for trading and clearing (exercise and settlement) in Irish equity derivatives. Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW. No cash payment in JPY. |
| 06 May | ✅ | Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW. No cash payment in JPY. |
| 26 May | ✅ | Eurex is closed for trading and clearing (exercise and settlement) in Exchange Traded Commodities as well as British equity and equity index derivatives; no cash payment in GBP. Eurex is closed for trading in Brazilian, Canadian and U.S. equity derivatives; no cash payment in USD. |
| 29 May | ✅ | Eurex is closed for trading and clearing (exercise and settlement) in Swiss fixed income as well as equity and equity index derivatives; no cash payment in CHF. Eurex is closed for trading and exercise in Finnish equity and equity index derivatives. Eurex is closed for trading and exercise in Swedish equity derivatives; no cash payment in SEK. Eurex is closed for trading in Norwegian equity derivatives; no cash payment in NOK. Eurex is closed for trading in Danish equity derivatives; no cash payment in DKK. |
| 30 May | ✅ | Eurex is closed for trading in Danish equity derivatives; no cash payment in DKK. |
| 02 June | | No cash payment in NZD. |
| 03 June | ✅ | Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW. |
| 05 June | ✅ | Eurex is closed for trading in Danish equity derivatives; no cash payment in DKK. |
| 06 June | ✅ | Eurex is closed for trading and exercise in Swedish equity derivatives; no cash payment in SEK. Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW. |
| 09 June | ✅ | Eurex is closed for trading and clearing (exercise and settlement) in Swiss fixed income as well as equity and equity index derivatives; no cash payment in CHF. Eurex is closed for trading in Norwegian equity derivatives; no cash payment in NOK. Eurex is closed for trading in Danish equity derivatives; no cash payment in DKK. |
| 19 June | ✅ | Eurex is closed for trading in Brazilian, Canadian and U.S. equity derivatives; no cash payment in USD. Eurex is closed for trading in Polish equity derivatives. |
| 20 June | ✅ | Eurex is closed for trading and exercise in Finnish equity and equity index derivatives. Eurex is closed for trading and exercise in Swedish equity derivatives; no cash payment in SEK. No cash payment in NZD. |
| 04 July | ✅ | Eurex is closed for trading in Brazilian, Canadian and U.S. equity derivatives; no cash payment in USD. |
| 21 July | | No cash payment in JPY. |
| 01 August | ✅ | Eurex is closed for trading and clearing (exercise and settlement) in Swiss fixed income as well as equity and equity index derivatives; no cash payment in CHF. |
| 11 August | | No cash payment in JPY. |
| 15 August | ✅ | Eurex is closed for trading and exercise in Italian equity derivatives. Eurex is closed for trading in Polish equity derivatives. |
| 25 August | ✅ | Eurex is closed for trading and clearing (exercise and settlement) in Exchange Traded Commodities as well as British equity and equity index derivatives; no cash payment in GBP. |
| 01 September | ✅ | Eurex is closed for trading in Brazilian, Canadian and U.S. equity derivatives; no cash payment in USD. |
| 15 September | | No cash payment in JPY. |
| 23 September | | No cash payment in JPY. |
| 13 October | | No cash payment in JPY. No cash payment in USD. |
| 27 October | | No cash payment in NZD. |
| 03 November | | No cash payment in JPY. |
| 11 November | ✅ | Eurex is closed for trading in Polish equity derivatives. No cash payment in USD. |
| 24 November | | No cash payment in JPY. |
| 27 November | ✅ | Eurex is closed for trading in Brazilian, Canadian and U.S. equity derivatives; no cash payment in USD. |
| 24 December | ✅ | Eurex is closed for trading in all derivatives. No cash payment in SEK. No cash payment in DKK. No cash payment in NOK. |
| 25 December | ✅ | Eurex is closed for trading and clearing (exercise, settlement and cash) in all derivatives. |
| 26 December | ✅ | Eurex is closed for trading and clearing (exercise, settlement and cash) in all derivatives. |
| 31 December | ✅ | Eurex is closed for trading in all derivatives. No cash payment in SEK. No cash payment in DKK. No cash payment in JPY. |

### 3.1 The page was revised during 2025 — two states exist

| Capture | Rows | Closure rows | Cash-payment-only rows |
|---|---|---|---|
| 2025-03-19 | 58 | 41 | 17 |
| 2025-06-23 | 54 | 37 | 17 |
| 2025-09-13 | 54 | 37 | 17 |

The June and September captures are **byte-for-byte identical in table content** (`JUN == SEP`
on all 54 rows). The March state differs from them in exactly three ways, all confined to the
`Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures` product scope:

| Row | 2025-03-19 capture | 2025-06-23 / 2025-09-13 capture |
|---|---|---|
| 03 June | **absent** | `Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW.` — **added** |
| 15 August | `Eurex is closed for trading in Daily Futures on KOSPI 200 Derivatives and Daily USD/KRW Futures; no cash payment in KRW.` + Italian + Polish clauses | Italian + Polish clauses only — the KOSPI clause **withdrawn** |
| 03 October | KOSPI Daily Futures closure | **absent — withdrawn** |
| 06 October | KOSPI Daily Futures closure | **absent — withdrawn** |
| 07 October | KOSPI Daily Futures closure | **absent — withdrawn** |
| 08 October | KOSPI Daily Futures closure | **absent — withdrawn** |
| 09 October | KOSPI Daily Futures closure | **absent — withdrawn** |

Net: 58 − 5 + 1 = 54. So the operator **added** a 3 June KOSPI closure and **withdrew** the five
October KOSPI closures plus the 15 August KOSPI clause — consistent with that product going away
during 2025 rather than with a change to any Eurex-wide session.

**Every closure of the eight recurring holidays of §1, and every `… in all derivatives` row, is
byte-identical in all three captures.** The revision touched only the KOSPI/USD-KRW Daily Futures
product scope. The September capture is the controlling in-year state and is what §3 transcribes;
the March capture is kept because it is the state in force from 2025-01-01 to 2025-06-23.
Neither state names any early close or reduced session.

## 4. The 2027 published future

Retrieved: **yes, as a column** — but see the caveat in §4.2, which is decisive.

### 4.1 What the operator prints, verbatim

Both the three 2025 captures (heading `Non-trading days at Eurex 2025 - 2030`) and the live
2026 page (heading `Non-trading days at Eurex 2026 - 2030`) print a 2027 column. From the
live 2026 page, verbatim, with the operator's own weekday names:

> New Year's Day — Friday 01 Jan 2027
> Good Friday — Friday 26 Mar 2027
> Easter Monday — Monday 29 Mar 2027
> Labour Day — *Saturday 01 May 2027*
> Christmas Eve\* — Friday 24 Dec 2027
> Christmas Day — *Saturday 25 Dec 2027*
> Boxing Day — *Sunday 26 Dec 2027*
> New Year's Eve\* — Friday 31 Dec 2027
>
> `* No trading; clearing and settlement are open if the holiday is not on a Saturday or Sunday.`

The italicised entries are italicised in the operator's own markup (they fall on a weekend).
The `*` footnote is verbatim.

### 4.2 The operator's parallel 2027 publication is expressly preliminary

**Yes — 2027 is expressly marked preliminary, on a different Eurex page.** The
*Indicative Trading Calendars* page states, verbatim:

> The following trading calendars are provided on a preliminary and indicative basis for the
> years 2027 to 2036 to support forward planning by our customers and are subject to change.

and, under the sub-heading **"Indicative trading holidays by calendar for the period 2027-2036"**:

> The trading calendars for the years 2027 to 2036 are provided on an indicative and
> preliminary basis. All dates are subject to change and may be updated to reflect official
> announcements, holiday schedules, or other adjustments from the home exchanges, including
> any ad-hoc modifications. Please note that while Christmas Eve and New Year's Eve may not
> be recognized as trading holidays by the home exchanges, they are marked as holidays in the
> trading calendars of Eurex Deutschland.

**The holiday-regulations page's own 2027 column carries no such caveat**: a full-text scan of
the live 2026 page and all three 2025 captures finds zero occurrences of `preliminar`,
`indicativ`, or `subject to change`, and the only footnote is the `*` asterisk note above.

So Eurex publishes 2027 holidays twice, with **conflicting labels**: unconditionally stated on
the holiday-regulations page, and expressly preliminary and subject to change on the
indicative-calendars page, whose stated scope ("trading holidays … 2027-2036") covers the same
dates. Recorded as a live conflict, unresolved by lineage — the maintainer decides. Under
LAW-NO-FABRICATED-DATES, 2027 cannot be encoded as unconditional dated future on this evidence.

### 4.3 There is no Trading Calendar 2027 PDF

The `trading-calendar-archive` page lists editions **2012 through 2026** and contains the
string `2027` zero times. A CDX query for `tradingcalendar_2027` returns nothing.

**Do not be misled by an HTTP 200**: Eurex's blob route
`/resource/blob/<id>/<hash>/data/<filename>` is a **catch-all** — it returns the file named by
the blob, not by the trailing filename. Substituting `tradingcalendar_2027_en.pdf` for
`tradingcalendar_2026_en.pdf` under the 2026 blob returns HTTP 200 with the **2026** PDF
(sha256 `b0796b42…`, byte-identical to the stored 2026 artifact); a bogus name
`zzz-does-not-exist.pdf` returns the same 200 and the same bytes. Verified, not assumed.

## 5. Cross-check between the two artifacts

The PDF's `all derivatives: 1 January, 18 April, 21 April, 1 May, 25 December, 26 December`
matches the page's six all-derivatives rows exactly. The PDF's `24 December, 31 December`
matches the page's two trading-only rows. The PDF's ETP/British `5 May, 26 May, 25 August`,
Finnish `6 January, 29 May, 20 June`, Irish `5 May`, Italian `15 August`, Norwegian
`17 April, 29 May, 9 June`, Danish `17 April, 29 May, 30 May, 5 June, 9 June` and Polish
`6 January, 19 June, 15 August, 11 November` each match the corresponding day-by-day rows.
No disagreement was found between the two T1 artifacts.
