# SGX T+1 close 04:45 -> 05:15 : triangulated to Monday 2019-11-11, but NOT law-closable

Retrieved 2026-09-06. Relates to: exchange-hours-rs issue #45 (and #44 for the Japan T-session).

## The date, corroborated three independent ways

Three readable, public, third-party broker notices — in three languages, published
within days of each other — all state the SGX T+1 session close moved from 04:45 to
05:15 SGT on **Monday 11 November 2019**:

- Henghua International Futures (横华国际期货), notice KF-2015-07-22, dated 2019-11-07 (Chinese):
  "根据新交所通知，由 2019 年 11 月 11 日（星期一）起，部分衍生产品将延长收市后交易时段
  （T+1 时段）至凌晨 5 点 15。" — table shows 04:45 -> 05:15 for UC/FE/CN/NK/TW/IN/SG.
  URL: https://www.henghua.hk/cmsbigfile/2019/11/80f813c2-254b-4739-9619-b089ec09c92c/...T+1...pdf
- Phillip Futures, announcement 1329, dated Fri 8 November 2019 (English):
  "Please be informed that with effect from Monday, 11 November 2019, the Singapore
  Exchange will be extending its T+1 session close from 4.45am to 5.15am."
- Rakuten Securities, 2019-11-06 (Japanese; prior-agent finding).

## Why this does NOT close #45 under LAW-PRIMARY-SOURCES

Every readable source is a third party's OWN notice ("根据新交所通知…" / "the Singapore
Exchange will be extending…"). None is a verbatim reproduction of an SGX circular. Under
this repo's law a third party's assertion cannot date a revision row — exactly the
distinction that let SGX Circular DTAM 15 of 2025 stand (it was mirrored *verbatim* on
CITIC) but keeps these out.

The SGX-own primary for this exact change IS publicly hosted but UNREADABLE:
"Titan DTDC Newsletter - Extension of T+1 Trading Hours" and two follow-ups (Go-Live
Schedule 2019-10, Reminder 2019-11) at api2.sgx.com — all RC4/128 encrypted with a
non-empty OPEN password (empty-password check fails; /O owner string byte-identical
across all three = one fixed SGX scheme). LAW-PUBLIC-SOURCES puts password-protected
material out of scope as a data source; defeating the encryption is not on the table.

Unlike 2025, **no numbered public SGX circular for the 2019 T+1 extension exists on any
mirror.** The change was member-facing only, distributed via the encrypted newsletters
and the read_me change-log (already ruled out). This is why it cannot be law-closed.

## Channels now exhausted for #45 (do not re-run)

1. SGX Derivatives Product Catalogue read_me change log — cell E87, no date/version,
   bound only by cell-border formatting. RULED OUT.
2. Titan DTDC newsletters (the SGX-own primary) — RC4-encrypted, out of scope.
3. Numbered SGX circular on member mirrors (the CITIC/KGI route that worked for 2025) —
   KGI hosts DTAM 103 of 2020, CITIC hosts DTAM 15 of 2025, but NO 2019 trading-hours
   circular exists on KGI, Phillip/POEMS, UTrade, CITIC, Henghua or Yuanta doc stores.
4. SGX media/press release — none exists; CDX of sgx.com / links.sgx.com media-centre
   and mondovisione (verbatim SGX-release mirror) show no 2019 T+1 hours release.
5. SGX rulebook — delegates hours to Contract Specifications, which it explicitly
   excludes from the Rules (FTR 4.1.5 + Definitions). Structurally cannot carry it.
   (see 2026-09-06-rulebook-channel-ruled-out.md)
6. DT/AM circulars 2019-2020 on sgx.com / api2.sgx.com and Wayback CDX — absent.
7. Pre-2020 Derivatives Trading Calendar PDFs — none in the archive.

## Bearing on #44 (Japan T-session 14:25 -> 14:55, believed 2024-11-04)

Same outcome: Phillip Nova's own notice "Extension of T-session Trading Hours for SGX
Nikkei Derivatives..." states effect from Monday 4 November 2024; a Fubon "SGXChange.pdf"
that might have been verbatim now 404s. Corroborated at 2024-11-04, not law-closed.

## Conclusion

The date is not in doubt as a matter of fact — three independent parties in three
languages agree on 2019-11-11. It is un-*sourceable* under this repo's primary-source law
because the only operator-authored statement is behind SGX's newsletter encryption and no
numbered circular was published. #45 stays a documented, sessionless pre-2020 era with the
reason stated truthfully: the predecessor channels were searched and the operator's own
statement is access-controlled, not absent.

## Addendum 2026-09-06 — channel 8 closed: open-source calendar libraries

Read in full: exchange_calendars, quantopian/trading_calendars, pandas_market_calendars
(released tree + open PR #461), QuantLib, QuantConnect/Lean (+ ~12 forks), nautilus_trader,
and several smaller repos. Result: NOTHING. Structurally, not for lack of searching —
the libraries that carry effective-dated session history (exchange_calendars,
pandas_market_calendars) do not cover SGX derivatives at all (XSES is cash equity, 09:00-17:00);
the one library that does cover SGX derivatives (Lean, "Future-sgx-NK", commit ec6abfa
2020-06-17) has no effective-date mechanism — every entry is a single undated snapshot, so a
cutover is invisible by design. pandas_market_calendars PR #461 keys every SGX boundary to
`(None, ...)`, cites only "SGX DT Trading Calendar 2025", and its author disclaims accuracy.
GitHub-wide code/issue/commit searches for any SGX circular reference return only this
repository's own citations. Do not re-run.
