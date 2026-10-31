# Xetra future-session confirmation — issue #374

Confirmation completed on 2026-10-31 UTC, before the original 2026-12-29 UTC
confirm-by deadline. This confirms the operator's published schedule as checked
on this date; the 2026-12-30 session is still in the future.

## Current operator artifact

Re-fetched the live final-session PDF at
`2026-10-31T23:19:02.444473+00:00` (HTTP 200, 158,845 bytes):

https://www.cashmarket.deutsche-boerse.com/resource/blob/5673886/22764993c4b1617c5f465186066344e6/data/Final%20trading%20session%202026.pdf

SHA-256:
`d3618ef9738a3cae92909d11d4eaf820ab7b71d1e723c1fa04a21062e9738115`

The bytes are identical to the source cited by the merged row. The prior
22:06:59 UTC capture and the existing Documents table remain unchanged. Fresh
retrieval metadata and the corroborating circulars 049/2026 and 050/2026 are
retained in `captures.json`, `channel-checks.json` and this report; they add no
new Documents rows or runtime sourcing basis.

## Scope and phase check

The PDF explicitly dates the session to Wednesday 30 December 2026 and states
that its times are CET. Only section 2, MIC XETR, and its DAX-share scope are
compared with the crate. The XFRA section and off-book TES/EnLight deadlines
are excluded. Eight literal time statements were checked in the XETR section:
pre-trading 07:00; retail early 08:00; opening auction call 08:55; intraday
auction call 13:00; closing auction call 14:00; closing-price determination no
earlier than 14:05; DAX/MDAX/SDAX Trade-at-Close end 14:10; post-trading end
15:00.

At crate head `6078da48c15a2dc602961a7ea0759ef0cfcaa17c`, the seven replacement
blocks match the documented derivation. `runtime-comparison.json` records the
module digest, decoded blocks and comparison. `verify_confirmation.py`
reproduces those checks from the captured PDF text and current module. The
09:00:30 opening and 13:02:30 intraday conservative uncross boundaries remain
the unchanged normal-profile conventions, rather than literal times newly
printed by the final-session notice. The classification of pre/post trading
as order entry and the combined extended closing-auction/TAC block retains
the existing documented scope. No runtime discrepancy was found or changed.

The existing public regression test
`suite::xetra::the_2026_final_session_replaces_retail_late_with_shortened_post_trading`
passed at the merged baseline: 1 test passed, 0 failed. The runtime module is
byte-identical at the current comparison head. Its executable end at 14:10, post-trading end
at 15:00, removal of late retail and following executable reopening remain
consistent with this capture.

## Supersession check and bounds

The live operator calendar, circulars first page, RSS feed, query results and
both relevant circular pages were captured through
`2026-10-31T23:19:27.707498+00:00`. Exact URLs, retrieval times and hashes are
in `captures.json`; rendered result inventories are in `channel-checks.json`.

- The calendar still links the identical final-session PDF URL.
- The circulars first page contains ten entries, displayed from 29 September
  through 30 October 2026. Its two newest entries are circulars 050/2026 and
  049/2026, displayed as 30 October 2026.
- The current ten-entry RSS feed likewise begins with those circulars. Its
  publication timestamps are 2026-10-29 23:15 and 23:00 GMT, respectively;
  these coexist with the pages' displayed 30 October civil date.
- The public circular search for `final trading session 2026` returned five
  rendered results: the two 2026 circulars, one unrelated May 2026 technical
  circular and the two 2025 final-session circulars.
- Both 2026 circular pages reaffirm 30 December 2026 and refer readers to the
  calendar's official announcement; neither states an amended timetable.

No superseding or amending timetable was located in these checked operator
channels. This is a bounded current-publication check, not an assertion that
all possible publications were exhaustively searched or that later notices
cannot change the schedule. It does not claim the future session occurred.
The separate 2027-hours watch under issue #200 is unchanged.
