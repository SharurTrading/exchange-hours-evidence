# Current and forward OANDA source audit

Reviewed 2026-10-12 UTC against release branch `acd44a009028d84b513997f67e41f5933d132e4c`. This is a bounded, read-only source audit. No code, issue or external post changed. Fresh UK operator bytes, response headers, retrieval UTC and digests are retained beside this report.

Two current/forward limitations need explicit handling: TRY has a witnessed current normal week but no runtime holiday coverage, and every other native book stops holiday coverage at 2026-10-30. The 26 withheld date/book pairs are all before 2026-10-12; none independently blocks a next-session walk starting now. Historical walks into them still refuse and remain disclosed in #332.

## TRY: category membership supports a bounded holiday audit

The fresh [UK hours page](https://www.oanda.com/uk-en/trading/hours-of-operation/) places the TRY row within Forex CFDs. It explicitly separates the ordinary FX row from TRY by instrument label, then gives TRY Central Europe, daily Monday–Friday 08:00–17:00. The separation is a normal-hours exception within a shared Forex category. It is not a statement that TRY is outside Forex.

The fresh [UK holiday page](https://www.oanda.com/uk-en/trading/holiday-trading-hours/) publishes changes by category. Its generic Forex statements contain no TRY exclusion. Thus category membership plus generic holiday wording is admissible operator-scope reasoning: an explicit TRY label is not inherently required to establish that a generic Forex holiday restriction applies. This is an interpretation of the operator's two documents, not a quotation claiming the operator expressly named TRY. No contradictory UK TRY-specific holiday rule was found in the bounded primary-source search. Japanese/TMS calendars do not establish UK applicability and were not imported.

A restriction and an instrument's available normal hours must be intersected. Generic Forex holiday reopens do not expand the TRY daily grid. For example, the Christmas Day 2025 and New Year's Day 2026 generic Forex reopening at 17:05 Eastern is 22:05 Central European winter time, after TRY's 17:00 daily close. Therefore the holiday's daytime TRY interval is removed; the next weekday returns to 08:00–17:00. A preceding generic Forex close at 16:59 Eastern is 21:59 Central European winter time, after TRY has already closed, and does not shorten its daytime session. Do not encode a TRY executable opening at 22:05 or carry an overnight FX block into it. These past examples calibrate category interpretation; they do not establish the restricted UK grid before its 2026-10-10 witness.

**Current recommendation:** accept an audited TRY holiday window **2026-10-10..2026-10-30**, with no exception rows in that window, against the current UK changes list and witnessed TRY grid. The only published future dated changes are 19 October CHINAH/HK33 and 30 October Swedish share CFDs; neither scopes Forex/TRY. This is the same bounded publication-window audit used for the native FX book, not a claim of perpetual holiday-free TRY operation. No Turkish equity, bank or national-holiday calendar was inferred into spot Forex. In particular, October 28/29 Turkish local holidays cannot be converted into broker closures merely because the pair contains TRY.

At the exact reviewed release head, `src/calendar/schedules/holidays/routing.rs` still maps `OandaTryFx` to `None`; `sourcing.rs` witnesses the normal week from October 10. The evidence file's requirement for a TRY-specific holiday artifact is stricter than the source-category evidence warrants. A bounded audited table would remove that current applicability refusal while leaving the pre-witness history and forward publication limit honest. The runtime coverage change requires a source-backed implementation and review; this report does not claim it already ships.

TRY DST check: October 12–23 sessions are 06:00–15:00Z; October 26–30 sessions are 07:00–16:00Z, using Europe/Berlin after the October 25 clock change. The fresh page still prints Central Europe and no separate TRY daylight-saving override. Its interpretation is a local Central European clock, not fixed UTC or Istanbul time.

## Forward publication boundary remains October 30

Fresh UK holiday bytes still end their 2026 forward list at Friday 30 October (Swedish share early close). They contain no November/December 2026 or 2027 UK notice. A bounded official-domain search found old 2025 Christmas/2026 New Year statements, other OANDA legal entities, and underlying-exchange publications, but no sufficiently specified UK year-end 2026 arrangement. This is a negative research result, not a claim that no document exists anywhere.

All six native family holiday windows (FX ex-TRY, metals, US index, US Treasury, US commodity and Brent), plus the venue clock mirror, therefore correctly refuse beyond October 30. October 31 is outside the audited range even though it is a weekend; it must not be labelled a known ordinary closure merely from the weekly grid. A forward walk beyond the Friday October 30 last session can need the Sunday November 1 / Monday November 2 session and encounter the publication boundary. The same limit applies to TRY if the proposed bounded window is implemented.

**Closing evidence:** a UK/OANDA Europe Limited holiday publication extending the window with unconditional, sufficiently specified dates and exact family hours, or an explicitly selected caller policy with User provenance that supplies later arrangements. Do not copy 2025 Christmas dates/hours into 2026 or turn underlying CME/ICE publication into broker T1 proof. Thanksgiving, Christmas Eve/Day, Boxing Day and New Year remain outside the broker publication horizon here. This bounded horizon can be operationally release-grade only when callers handle coverage refusal and the documented watch process refreshes the evidence before forward queries reach it; it does not provide unbounded future operation.

## Current normal-hour comparison and scope

The fresh UK hours page corroborates the released native clocks: FX ex-TRY 17:05–16:59 New York with its daily break; XAU/XAG 18:05–16:59 New York; US index and US Treasury products 17:01–15:59 Chicago; the five US commodity/energy listings equivalent to 18:01–16:59 New York; Brent's London Sunday 23:01 opening, weekday breaks and Friday 21:59 close. No newly changed current native endpoint was found. October US/European DST mismatch is handled by each book's named IANA zone rather than a hard-coded ET/London offset. NZD-specific Auckland breaks remain instrument scope.

The fresh [UK help page](https://help.oanda.com/uk/en/faqs/hours-of-operation.htm) expressly identifies OANDA Europe Limited. It says hours can change during public holidays/DST and that not every instrument is guaranteed to be quoted during operating hours. Those statements preserve the distinction between scheduled executable windows and live liquidity or close-only/product restrictions. They do not supply a dated session exception, and pending stop/entry-order storage outside market hours does not add an executable phase.

The other past 26 pairs, undated historical cutovers and later launch history remain #332 disclosures. This current audit neither resolves them nor needs to retry the OANDA archive channels already refused twice.

## Saved sources and exact attribution

| Fresh operator artifact | Retrieval UTC | SHA256 |
|---|---|---|
| [UK hours](https://www.oanda.com/uk-en/trading/hours-of-operation/) | 2026-10-12T00:39:55.742904Z | `1c986aee21fdd7b76d04cabc2a8846fe00e08bb28257a27cfada828291c7e063` |
| [UK holidays](https://www.oanda.com/uk-en/trading/holiday-trading-hours/) | 2026-10-12T00:39:55.726174Z | `ce7cd4c3d4db0e32ec629715ee321bdd4d48455845894bee1eb8df768d066eff` |
| [OEL help hours](https://help.oanda.com/uk/en/faqs/hours-of-operation.htm) | 2026-10-12T00:39:55.833741Z | `3a42f46d4a4c3f6f165c3815fe122cc0e47faed305b293c93a8c0eca9a985332` |

Each HTML and headers file, extracted text and the isolated 2026 holiday section are saved in this directory. `retrieval.json` records successful HTTP retrievals and errors; `release-reviewed-hashes.json` and `release-*.rs` preserve the exact named release-head source bytes, despite subsequent changes in the shared checkout. `source-observations.json` records the current-date versus historical-gap check. This was source review only; no global quality or runtime-test claim is made.
