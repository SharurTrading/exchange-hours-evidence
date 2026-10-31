# Published special-session source refresh — 2026-10-31 UTC

This directory preserves the primary artifacts, retrieval manifests, derived
text and bounded negative searches used for the calendar update. Each source
area carries its own URL/retrieval/SHA-256 inventory.

The initial scan compared an older 1.1.0 checkout. The implementation was then
reconciled with exchange-hours-rs `origin/main` at
`02a3c89495c4f7f9b51fab833fd04d2bc815f456`, retaining its already published ICE
Christmas closes, CME extension, restored histories and coverage windows.
Early scan reports describe their observed baseline; the independent final
review reports identify the exact final commit and resulting changes.

The remaining implementation covers NSE's 2026-11-08 Muhurat session, Xetra's
2026-12-30 final session, ICE shortened Christmas queues and Cotton's Monday
reopening, and the complete CME October maintenance trade dates and their
Pre-Opens. Other checked publications do not authorize an additional runtime
change for their existing admitted scopes.

- `nse/`: circular NSE/CMTR/76941 (149/2026) and retrieval metadata.
- `europe/`: final Xetra notice, corroborating calendars and comparison reports.
- `ice-americas/`: Christmas notice, exact family transcription and source scan.
- `cme-coinbase/`: T2 trading-hour responses, Globex notices and block derivation.
- `us-readiness/`: conditional overnight launches and scoped options checks.
- `apac-oanda/`: current hours/calendar checks and entity/scope exclusions.
- `independent-nse-review/`: initial second retrieval and review findings.
- Independent final review directories record final source checks and validation.

Forward reconfirmations are tracked by exchange-hours-rs issue #374. These
captures do not advance unchanged ledger review dates or publication horizons.
