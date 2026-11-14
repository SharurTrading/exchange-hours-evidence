# Evidence index — `normal-weeks/nasdaq-night-session-2026-11-14`

Normal-week captures for the Nasdaq **Global Trading Hours / Expanded 23/5**
initiative: the operator alerts that date the system-hours extension the crate's
`nasdaq` row had been holding unencoded pending Equity Data Plan readiness and a
later Nasdaq readiness filing (origin alert ETA2026-46).

Retrieval session: **2026-11-14 07:12 UTC** (LAW-UTC-DATES). `curl` with a desktop
browser User-Agent against `nasdaqtrader.com` Trader News pages; no access
control evaded; no interstitial was served.

| File | Exact URL | Retrieved (UTC) | sha256 | Bytes | What it contains |
|---|---|---|---|---|---|
| `ETA2026-64.live.html` | `https://www.nasdaqtrader.com/TraderNews.aspx?id=ETA2026-64` | 2026-11-14T07:12:08Z | `4ad899e0b4b13627027ccc7cada889abb23c66baca9933bda15ca67324668714` | 74405 | **T1, the dated production statement.** "In connection with Nasdaq's Expanded 23/5 trading initiative, system hours will be extended to 9:00 p.m. ET Sunday through 8:00 p.m. ET Friday, with a daily one-hour pause from 8:00 p.m. to 9:00 p.m. ET Monday through Thursday (excluding holidays), effective December 6, 2026." Defines the "Global Trading Session (9:00 p.m. to 9:30 a.m. ET)" in the halts-file section; cites the Expanded Hours Announcement, ETA2026-55 (now retired — live page and Wayback both 404), DN 2026-03 and DN 2026-08. |
| `ETA2026-66.live.html` | `https://www.nasdaqtrader.com/TraderNews.aspx?id=ETA2026-66` | 2026-11-14T07:12:09Z | `1f8486e5d014a9b6986c65bb690e55f194d41b5cc400bb8428e6b7c141892175` | 68447 | **T1, pre-production readiness.** "Global Trading Hours Pre-Production Period Now Available": pre-production ongoing as of November 1, 2026; "Trading is available Sunday through Thursday, from 9:00 p.m. ET until 3:55 a.m. ET* the following day"; footnote "* Time may be subject to revision and if so, will be indicated in a future ETA" — the 3:55 a.m. end is expressly conditional, the December 6 production date is not. |
| `UTP2026-33.live.html` | `https://www.nasdaqtrader.com/TraderNews.aspx?id=UTP2026-33` | 2026-11-14T07:12:10Z | `e744283cf6e21d220b9c6ef0dad33edbbbe0ad8de9e4417259d1033e2c17c797` | 58093 | **T1, SIP-side readiness.** "Effective December 6, 2026, the UTP SIP transmission schedule will support Extended Trading Hours and operate from Sunday at 9:00 p.m. ET through Friday at 8:00 p.m. ET, with a planned daily maintenance window from approximately 8:00 p.m. to 9:00 p.m. ET." Fee-liability table adds "Extended Trading hours session — 9:00 p.m. to 4:00 a.m. — NEW SESSION". |
| `ETA2026-39.live.html` | `https://www.nasdaqtrader.com/TraderNews.aspx?id=ETA2026-39` | 2026-11-14T07:12:11Z | `4b61ede2a57af6ca7687cce395ba716a45dba2f5da22155496953657a82d344f` | 75006 | **T1, TRF/WorkX alignment.** "effective December 6, 2026, FINRA/Nasdaq TRF system hours will operate from 9:00 p.m. ET Sunday to 8:00 p.m. ET Friday, with a one-hour pause from 8:00 p.m. to 9:00 p.m. ET on Monday through Thursday... WorkX system hours will align with the new TRF hours." Cites a FINRA Technical Notice and a FINRA Rule Filing. |

## Retrieval findings

- The production effective day (2026-12-06) is stated unconditionally in the
  operator's own alert text; the conditional language attaches to the
  pre-production 3:55 a.m. end time only.
- The same 2026-12-06 day witnesses SIP-side readiness (UTP2026-33, "recently
  approved" CTA/UTP Plan amendments per the NYSE-side notice) and TRF alignment.
- Encoding decision deliberately NOT taken in this capture wave: the session's
  topology (overnight matching vs order entry, the unstated production overnight
  end, holiday interaction, trade-date assignment for the Sunday-evening open)
  needs its own work-up. Recorded as the crate's follow-up, not encoded here.
