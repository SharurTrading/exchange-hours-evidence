# ECBTC weekday maintenance window — the wiki's version history settles the ORDER

Retrieved 2026-09-06 via the Confluence REST v1 and v2 APIs, anonymously (no auth).
Relates to: exchange-hours-rs issue #57.

## The question this was sent to answer

Is there a CME statement of ECBTC's weekday daily maintenance window dated AFTER the
2026-05-29 cutover, which would break the tie between the wiki's `3:00:00 p.m.` and
SER-9740R's figure?

Answer to that literal question: **NO.** Conclusively, for the wiki.

## What it settled instead — and this is the useful part

Page 1394343937 "Event-Based Contracts Expansion to 24-7 Trading" has exactly FOUR
versions:

    v4  2026-04-23T13:12:28.596Z   (current)
    v3  2026-03-25T19:33:10.407Z
    v2  2026-03-25T19:25:32.840Z
    v1  2026-03-25T19:22:04.740Z

`/history` returns `latest:true` with **no `nextVersion`**; `?status=historical&version=5`
returns HTTP 404. Confirmed independently by the v2 API. There is no revision after
2026-04-23.

The maintenance-window table is **absent from v1, v2 and v3** and enters at v4. String
counts in the storage bodies:

    v1/v2/v3:  "Maintenance Window" 0   "3:00:00" 0   "4:01:00" 0   "4:02:00" 0
    v4:        "Maintenance Window" 4   "3:00:00" 1   "4:01:00" 2   "4:02:00" 2

The page's own Revision History row, verbatim:

    April 22, 2026 | Added Event-Based Contract Maintenance Windows and Market Hours
                     schedule impacts.

## Therefore the two primaries are ORDERED, not simultaneous

    wiki table authored   22–23 April 2026
    SER-9740R              28 May   2026
    cutover                29 May   2026

The wiki figure is **the earlier statement**, not a later restatement. The hypothesis
that some later revision quietly corrected 3:00 to 4:00 is eliminated — the `3:00:00`
cell is the page's first, only and final word on that number, and it is still live today.

## The disputed row, verbatim (v4 storage format)

    <td><p><em>Close</em>: 3:00:00 p.m. to 4:01:00 p.m. CT</p></td>

Rendered in full:

    Monday through Friday | Daily Maintenance Window (with Trade Date roll)
    | Close: 3:00:00 p.m. to 4:01:00 p.m. CT
    | Pre-open: 4:01:00 p.m. to 4:01:30 p.m. CT
      No cancel: 4:01:30 p.m. to 4:02:00 p.m. CT
      Open: 4:02:00 p.m. CT

Product scope on the same page ties it to ECBTC unambiguously:

    Event contracts on Bitcoin Futures | ECBTC | VB | 329 | 74

## Page disambiguation — re-confirmed

The neighbouring page 988020743 "Swap-Based Event Contracts and 24-7 Trading" (v57,
2026-08-14) contains **zero** occurrences of "3:00:00", "4:01:00" or "4:00:00 p.m".
The two pages are distinct; the earlier mis-retrieval is not repeated here.

A space-wide CQL search for "ECBTC" returns totalSize 1 — page 1394343937 alone.

## Explicitly NOT evidence

The agent flagged, as an observation and not a finding, that on the crypto page every
table whose Close begins at 3:00:00 p.m. also carries an intervening reopen
("Open: 3:05:00 p.m. to 4:01:00 p.m. CT") before the 4:01 pause, whereas the ECBTC v4
row has a 3:00:00→4:01:00 Close with no intervening reopen — a shape consistent with a
dropped row. **No CME document says this.** It cannot be used to overwrite the row. It
is recorded here only so a future reader does not rediscover it and mistake it for
evidence.

## URLs

    .../wiki/rest/api/content/1394343937/version?limit=50
    .../wiki/api/v2/pages/1394343937/versions?limit=50
    .../wiki/rest/api/content/1394343937?status=historical&version=1|2|3|4&expand=body.storage,version
    .../wiki/rest/api/content/1394343937/history?expand=lastUpdated,previousVersion,nextVersion
    .../wiki/spaces/EPICSANDBOX/pages/1394343937/Event-Based+Contracts+Expansion+to+24-7+Trading

all on host `cmegroupclientsite.atlassian.net`.
