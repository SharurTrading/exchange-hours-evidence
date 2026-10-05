# CME globex evidence thread — #79 (undated 2012 Sunday Pre-Open move 16:15→16:00 CT)

Hunt pass: 2026-10-02 UTC. Evidence files: `docs/evidence/globex_equity_index.md`
(search record) and the four TAS keys'. Issue: SharurTrading/exchange-hours-rs#79.
Bracket: (2012-04-15, 2012-06-16], narrowed by hours-page captures to
2012-05-28..2012-06-07.

## Channels checked this pass

1. **The `/globex/files/` GCC one-pager directory, fully enumerated.**
   Closing condition (c) of the evidence file's search record names "a
   May/June 2012 Global Command Center one-pager of the class the 2013 grain
   notice proves exists" — the 2013 grain notice lives at
   `cmegroup.com/globex/files/cmegroup_reduced_grain_and_oilseed_hours.pdf`,
   so the whole directory was enumerated for 2012-2014
   (`cdx_globex_files_2012-2014.txt` here; 191 rows, `collapse=urlkey`).
   Every plausibly relevant PDF was fetched and read:
   - `enhancementsschedule.pdf` (2013-05-25 capture): "CME Globex Performance
     Enhancements Schedule" — dated Dec 2012-Apr 2013 performance rollouts
     per market. No pre-open entry. (here)
   - `GlobexRefGd.pdf` (2012-02-08): the Globex Reference Guide — generic
     market-state descriptions; the only "16:00 CT" is the grain PCP window.
     No Sunday pre-open times. (here)
   - `cmeglobexcalendar.pdf` (2012-11-03, "Updated-10/24/12"): the **Globex
     Initiative Calendar** months incl. June 2012 — June's cells carry
     CSU/NF/PL/PC entries, **no pre-open or trading-hours entry**,
     independently confirming the evidence file's search record on a second
     capture. (here)
   - `cmeglobexequityindexhoursdailypricelimitchanges.pdf` (2012-11-19): the
     GCC notice for the 2012-11-18 schedule change ("Effective Sunday,
     November 18 ... with a 15 minute market pause (Pre-open) from 15:15 CT
     to 15:30 CT") — dates the November change (already sourced by notice
     20121022), says nothing about the mid-year Sunday move. (here)
   - `tas.pdf` (2014-05-14): TAS product/symbol mapping table. Negative. (here)
   - `CMEG_Customer_Forum_Q2_2012.pdf` (2012-08-20): customer forum deck;
     its only "Sunday prior to market open" line is about GC2 credit-control
     mid-week adds, not the pre-open. (here)
   - `operatorsreleaseschedule.pdf` (capture 20121018153212): **no payload**
     — the WARC record replays to zero bytes in both `id_` and page form
     (revisit record). This one document is unreads; a different capture or
     the CC warc of the same file could still hold it. Noted as the one
     loose end of this pass.
   The enumeration's shape also explains the silence: the directory's
   dominant capture event is the 2012-08-21 bulk crawl — a GCC one-pager
   published in May/June and removed by August would never have been
   archived.
2. **MRAN channel**: the `cmegroup.com/rss/MRANs.xml` feed captured
   2013-08-15 (here) lists five MRAN titles, none about pre-open/Sunday.
   The 2012-2013 domain dump shows the MRAN RSS entries and an MRAN slide
   image only; no 2012 MRAN page about the pre-open exists in the archive.
3. **Client Systems Wiki revision history** (closing channel named by the
   issue): the page `cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457223974`
   was **created 2024-12-21T17:05:53Z** and edited 2025-01-13T19:37:27Z
   (version 2) — read from the public REST/v2 APIs 2026-10-02 UTC. Its
   revision history therefore **cannot date a 2012 change**; the channel is
   checkably closed (the page body itself is the 2025 statement already
   cited by the TAS evidence files).
4. **CME site search for "pre-open", advisoryDropDown=all, captured
   2012-03-08** (here): the results page carries clearing-advisory links
   only; no electronic-trading advisory about the pre-open. (Pre-dates the
   change, so expected silent.)

## What remains (unchanged closing conditions)

(a) a written reply from CME's desk (T1, closes under either reading) —
human task; (b) a T1/T2 artifact covering an ordinary week at the 2025
floor with `hasEvents: true` (channel retention limit already shown);
(c) the one unreads file: `operatorsreleaseschedule.pdf` — worth one
attempt through Common Crawl's CC-MAIN-2012 warc or a different Wayback
capture before declaring it empty. Do not key 2012-06-03 (the evidence
file's warning stands).

## Addendum (2026-10-02 ~03:00 UTC)

The Internet Archive entered a "Temporarily Offline" banner state during
this sweep (after hours of intermittent CDX 504s), so the
`operatorsreleaseschedule.pdf` re-check could not be completed: the
`:80`-form exact-URL CDX query now returns the offline page. The loose end
above stands, re-runnable when IA is stable. All Wayback-adjacent queries
in the other threads' notes share this caveat for anything attempted after
~02:45 UTC.

## Second pass addendum (2026-10-02 ~17:20-17:55 UTC) — the loose end is read; channels re-checked

Raw artifacts of this pass: `retry-2026-10-02/` (SHA256SUMS inside).

1. **`operatorsreleaseschedule.pdf` — re-probed; now a completed negative.**
   The IA hiccup that blanked this document was transient: the CDX exact query
   now returns capture `20121018153218` (mimetype application/pdf, status 200,
   length 49667, digest `LGFGI4WXCEYXPZMKMVSORM7L3ZSQMEBS`) — a different WARC
   record from the empty revisit (`…53212`) read last pass. Fetched and
   verified: the PDF's base32 sha1 equals the CDX digest exactly
   (`wb_20121018153218_operatorsreleaseschedule.pdf` here). It is the
   **FIX/FAST Operators Release Schedule** — dated channel-migration waves
   (2012-07-01, 07-15, 07-29, 08-19, 11-04, 11-18) listing FIX/FAST channel
   assignments per product. It carries no session times, no pre-open, no
   Sunday pause. Channel closed at the document level.
2. **`/globex/files/` 2012-2014 enumeration re-run** — the capture set is
   byte-identical to last pass's 190 file rows (`cdx_globex_files_2012-2014_reread.txt`
   here; only delta is the directory-listing row itself). No new captures
   since the prior sweep.
3. **The advisory tree, fully enumerated 2012-2014**
   (`cdx_cme_advisories_2012-2014.txt`, 626 urlkeys: clearing 368,
   disciplinary 58, electronic-trading 45, market-data 62, market-regulation
   53, ser 40). Every electronic-trading notice the archive holds for the
   bracket was already read last pass (20120409 = the 16:15 statement;
   20120521/20120528/20120604 silent) — this pass confirms there is **no
   other captured electronic-trading page between 20120518 and 20120806**.
   The **market-data** series pages inside the approach window that last pass
   had not read are now fetched and read
   (`wb_2012*_marketdata_2012{0409,0416,0423,0430}.html` here): all four are
   the MDP B-feed multicast source-IP change effective 2012-06-17 — no
   session language. `ser` 2012 is one rough-rice storage PDF. **CMRG's
   modern `/notices/` path has zero captures 2011-2014**
   (`cdx_cme_notices_2011-2014.txt` here, empty file) — that URL shape did
   not exist in the era.
4. **Common Crawl CC-MAIN-2012** (the only CC collection predating 2013 with
   an index): the `/globex/files/` slice is 127 rows, crawled 2012-02-13/14
   and 2012-05-24 (`cc2012_globex_files.json` here) — **zero** files named
   calendar/holiday/hours/schedule/operator, and the crawls predate the
   October capture anyway, so CC never held this PDF. A filtered query for
   electronic-trading advisory pages was still 504-degraded at write time
   (`cc2012_et_advisories.json` holds the last error); advisory coverage is
   already complete from the Wayback side (point 3), so this residual query
   is confirmatory only.

Net: every named lead of the #79 hunt is now a completed negative. The
closing conditions stand as written in the evidence file: (a) a written
reply from CME's desk, or (b) a T1/T2 artifact covering an ordinary week at
the 2025 floor with `hasEvents: true`. Do not key 2012-06-03.

## Second-pass close-out (2026-10-02 ~18:20 UTC)

The confirmatory CC-MAIN-2012 query for electronic-trading advisory pages
exhausted its retry budget against continuous 504s
(`cc2012_et_advisories.json` holds the last error); the Wayback-side advisory
coverage is complete (addendum point 3), so nothing rests on it. Every named
lead of the #79 hunt now has a completed-search record. Remaining closing
conditions unchanged.

## Resolution (2026-10-03 UTC)

Loose end (c) is closed: `operatorsreleaseschedule.pdf` was fetched at
17:18Z on 2026-10-02 (after the addendum's note) and its extracted text
(`ops.txt` beside the PDF) is the **FIX/FAST Operators Release Schedule** —
market-data channel release dates for July 1 - November 18, 2012. No session
or pre-open content; the document is definitively negative for #79.

The full 2026-10-03 re-read pass over this thread's artifacts, with newly
saved bracket captures and CDX dumps, is recorded in
`../../cme-bracket-rereads/INDEX.md`.
