# INDEX — task cbot-261 closure wave (PR #224)

All artifacts in this directory were retrieved on **2026-09-29 (UTC)** by the
closure wave for the `cbot` withheld-date census (#223, PR #224). `cmegroup.com`
answers 403 to this machine, so every operator document was read through the
Wayback Machine's verbatim `id_` raw replay of the operator's own bytes.
`capture` is the Wayback capture timestamp (UTC); replay it as
`https://web.archive.org/web/<capture>id_/<source url>`.
`cmegroup.com/files/trading-hours.html` is the trading-hours page the 2023
calendar links; the 2023-04-07 capture carries the
`Download a summary view of the Good Friday Holiday Hours` button linking
`/files/good-friday.pdf`, the pointer the #224 review used.

| file | sha256 | bytes | source url | capture (UTC) | what it is |
|---|---|---|---|---|---|
| `2023-mlk-day-advisory.pdf` | `2338a383ea4d43248a18b1b70fc4c4d09f10770502262cc193c584f11ae02720` | 365409 | https://www.cmegroup.com/tools-information/holiday-calendar/files/2023-mlk-day-advisory.pdf | 2023-02-03T07:12:56Z | CME Clearing memorandum; states no Globex session hours. |
| `2023-presidents-day-advisory.pdf` | `3d6619e8bf5c012ce59b315d900ba2f3a7600ab29fe48a4da9e22eb8e48b11bb` | 154069 | https://www.cmegroup.com/tools-information/holiday-calendar/files/2023-presidents-day-advisory.pdf | 2023-02-03T07:07:09Z | CME Clearing memorandum; states no Globex session hours. |
| `2023-good-friday-advisory.pdf` | `2faa51cf54f97c30f9474f18a34e69fd3a8f8fb5834640d9a1daf96a73de7d35` | 173297 | https://www.cmegroup.com/tools-information/holiday-calendar/files/2023-good-friday-advisory.pdf | 2023-02-03T06:53:33Z | CME Clearing memorandum; states no Globex session hours. |
| `holiday-calendar-2023-01-16.html` | `2917984167c50c026062068a5301e524565e32541ec5ed0b8b79bb3acbc18a9a` | 138297 | https://www.cmegroup.com/tools-information/holiday-calendar.html | 2023-01-16T03:24:37Z | Archived 2023 calendar page; hours moved into the trading-hours service. |
| `holiday-calendar-2023-01-29.html` | `c505c6102cf16de3272382b477a872ea6ac09030d0aec55f5abc959ffd0e1c47` | 138948 | https://www.cmegroup.com/tools-information/holiday-calendar.html | 2023-01-29T22:57:27Z | Archived 2023 calendar page; hours moved into the trading-hours service. |
| `trading-hours-2023-04-07.html` | `2d314e400c8995e9159fbffe8457fc5931bc2625ff88bac8169eff28e868a90e` | 150154 | https://www.cmegroup.com/trading-hours.html | 2023-04-07T03:15:32Z | The trading-hours page whose summary-view button links `/files/good-friday.pdf`. |
| `svc_2022-01-12_2022-01-14-mostactive.json` | `72f0617d61c3d6e4b00b375e78c3c016d8ec98e90e7b8fa8929412334fae7e6a` | 2916 | https://www.cmegroup.com/services/trading-hours-by-product?...fromEventDate=2022-01-12&toEventDate=2022-01-14... | 2026-05-28T07:13:26Z | T2 recapture; January-2022 window answers `hasEvents:false`. |
| `svc_2023-05-28_2023-05-30.json` | `7d8a5f8b6ef7370c7e1aedceccee3d9a0bcc10c5d91df4c0159b9aa80faa4d94` | 3898 | https://www.cmegroup.com/services/trading-hours-by-product?...fromEventDate=2023-05-28&toEventDate=2023-05-30... | 2024-07-08T16:14:38Z | T2 window; `hasEvents:false`. |
| `svc_2023-06-18_2023-06-20.json` | `54653e5c3c66922abc17869c68c09828badc6d4843b2ca2d9c750ec2ad679bee` | 3898 | https://www.cmegroup.com/services/trading-hours-by-product?...fromEventDate=2023-06-18&toEventDate=2023-06-20... | 2024-07-08T16:14:38Z | T2 window; `hasEvents:false`. |
| `svc_2023-11-22_2023-11-24.json` | `f5f88ee3c5ce71a3f8ab794f1ca9ec0619e62cc37eaf2dc96aeec9450dcbf51b` | 8484 | https://www.cmegroup.com/services/trading-hours-by-product?...fromEventDate=2023-11-22&toEventDate=2023-11-24... | 2024-07-08T16:14:39Z | T2 window; evented — bounds the start of the service's event history. |
