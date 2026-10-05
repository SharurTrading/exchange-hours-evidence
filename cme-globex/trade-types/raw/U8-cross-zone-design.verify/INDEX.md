<!-- SPDX-License-Identifier: MIT-0 -->
# Evidence index — adversarial verification of gate U8-cross-zone-design

Captured 2026-09-06 by the verifier, independently of the researcher's run. Channel: the public
text reader `https://r.jina.ai/<cme url>` in front of the same cmegroup.com URL (www.cmegroup.com
403s this host directly). No authentication anywhere; LAW-PUBLIC-SOURCES holds.

**Capture date is not artifact date.** `/services/trading-hours-by-product` returns a
forward-looking *published calendar*. A 2026-09-06 capture of the 2026-12-07 week states what CME
publishes today for that week. Used here only as evidence of which zone each boundary is anchored
to — never as a dated cutover.

## Why these were fetched

The researcher's `dead_ends` field asserted: *"no product id was located for CLL/CLS/CLC, so those
three closes are not measured first-hand"*. That claim of absence is false. CME's own product
slate endpoint returns the ids in two calls through the channel the researcher was already using.

`https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=N&sortAsc=false&sortField=oi&pageSize=500&cleared=Futures&exch=NYMEX|CME|COMEX`

| root | product id | CME's own product name | slate file |
|---|---|---|---|
| CLL | 6266 | WTI Crude Oil London Trade at Marker Futures | `slate-NYMEX-futures-pg2.txt` |
| BZL | 6268 | Brent Crude Oil London Trade at Marker Futures | `slate-NYMEX-futures-pg2.txt` |
| HOL | 6270 | NY Harbor ULSD London Tradable Marker | `slate-NYMEX-futures-pg2.txt` |
| RBL | 6273 | RBOB Gasoline London Trade at Marker Futures | `slate-NYMEX-futures-pg2.txt` |
| CLS | 6332 | WTI Crude Oil Singapore Trade at Marker Futures | `slate-NYMEX-futures-pg2.txt` |
| BZS | 6333 | Brent Crude Oil Singapore Trade at Marker Futures | `slate-NYMEX-futures-pg2.txt` |
| CLC | 10725 | WTI Shanghai Marker TAM | `slate-NYMEX-futures-pg2.txt` |
| DVT | 8005 | BTIC on E-mini FTSE Developed Europe Index Futures | `slate-CME-1.txt` |
| E3T | 9999 | BTIC on E-mini S&P Europe 350 ESG Index Futures | `slate-CME-1.txt` |
| BTB | 8970 | BTIC on Bitcoin Futures London Close | `slate-CME-1.txt` |
| ABB | 10664 | BTIC on Bitcoin futures against APAC Close | `slate-CME-1.txt` |
| NIT | 8633 | BTIC on Nikkei (JPY) Futures | `slate-CME-2.txt` |
| TPB | 8492 | BTIC on TOPIX (JPY) Futures | `slate-CME-1.txt` |
| HGF | 8652 | Copper London TAM | `slate-COMEX-1.txt` |

`6EB` was not present in the pages fetched; its Chicago pair rests on CME's FX BTIC FAQ prose.

## Measured, first-hand, both DST states

`svc-<id>-oct.txt` = trade dates 2026-10-26..30 (US CDT, UK GMT — **misaligned**).
`svc-<id>-dec.txt` = trade dates 2026-12-07..11 (US CST, UK GMT — aligned).
URL shape: `https://www.cmegroup.com/services/trading-hours-by-product?id=<id>&fromEventDate=<from>&toEventDate=<to>&pageSize=100`

| root | grp | aligned (dec) | misaligned (oct) | open / pre-open, both weeks |
|---|---|---|---|---|
| CLL | TM | `closed@10:30` x5 | `closed@11:30` x5 | `open@17:00`, `preopen@16:50` |
| CLS | TS | `closed@02:30` x5 | `closed@03:30` x5 | `open@17:00`, `preopen@16:50` |
| CLC | WM | `closed@01:00` x5 | `closed@02:00` x5 | `open@17:00`, `preopen@16:50` |
| HGF | TR | `closed@06:35` x5 | `closed@07:35` x5 | `open@17:00`, `preopen@16:50` |
| DVT | DT | `closed@10:30` x5 | `closed@11:30` x5 | `open@17:00`, `preopen@16:45` |
| E3T | EQ | `closed@10:30` x5 | `closed@11:30` x5 | `open@17:00`, `preopen@16:45` |
| TPB | BJ | `closed@00:30` x5 | `closed@01:30` x5 | `open@17:00`, `preopen@16:45` |
| NIT | N6 | `closed@00:30` x5 | `closed@01:30` x5 | `open@17:00`, `preopen@16:45`; plus a fixed Chicago-clock midday block `preopen@10:30`, `open@11:00`, `paused@16:00` x4 / `closed@16:00` x1 in BOTH weeks |
| BTB | BX | `closed@10:00`, `preopen@10:01`, `open@10:05` | `closed@11:00`, `preopen@11:01`, `open@11:05` | `preopen@16:01`, `open@16:02` both weeks |
| ABB | HB | `closed@02:00`, `preopen@02:01`, `open@02:05` | `closed@03:00`, `preopen@03:01`, `open@03:05` | `preopen@16:01`, `open@16:02` both weeks |

Every Chicago pair the researcher listed is confirmed. `sha256` for all files in `SHA256SUMS.txt`.

## Conflict this surfaced

CME's BTIC-on-Cryptocurrency FAQ (shape-queue block [7], capture 2024-04-16) states the London
window as *"Sunday - Friday 6:00 p.m. ET - 4:00 p.m. London time (11:00 a.m./12:00 p.m. ET).
Monday - Thursday 4:30 p.m. London time (11:30 a.m./12:30 p.m. ET) - 5:00 p.m. ET"* — a
**30-minute** stop ending 16:30 London (10:30/11:30 CT). `svc-8970-*.txt` shows CME's own service
restarting at 16:05 London (10:05/11:05 CT) — a **5-minute** stop. Two CME statements, neither
superseding the other on its face. AGENTS.md's sourced-intersection rule governs: serve what both
state, withhold the 25-minute disputed remainder, record the conflict beside the table.

---

## Second adversarial pass — 2026-09-12 (same gate id, independent re-run)

Same channel (`https://r.jina.ai/<cme url>`), no authentication. Product ids were re-derived
independently through `ProductSlate/V2/List` with `searchString=` rather than by paging the whole
slate, which returns them in one call each:
`https://www.cmegroup.com/CmeWS/mvc/ProductSlate/V2/List?pageNumber=1&sortAsc=false&sortField=globexCode&searchString=<root>&pageSize=20`

Re-measured and byte-identical to the first pass's captures (sha256 equal, see `SHA256SUMS.txt`):
`svc-6266-CLL-{oct,dec}` == `svc-6266-{oct,dec}`; likewise 10725/CLC, 6332/CLS, 8652/HGF, 8970/BTB.
`live-refetch-svc-8407-dec.txt` is byte-identical to the researcher's stored
`raw/U8-cross-zone-design/svc-8407-dec.txt` (`0917c5f9…`).
`svc-nopagesize-400.txt` reproduces the documented dead end verbatim:
`{ "message": "Requiered Parameters Missing: Check if the required parameters pageSize, fromEventDate, toEventDate are present."}`
`recheck-rerun-by-verifier.txt` is byte-identical to the researcher's `recheck-2026-09-06b.txt`.

### NEW finding of this pass: the 24/7 crypto BTIC weekend block spans a DST transition

| file | product | what it shows |
|---|---|---|
| `svc-8970-BTB-uktransition.txt` | BTB, 2026-10-22..27 | Sat 2026-10-24 `open@04:00` (td 2026-10-26); Sun 2026-10-25 **no events**; next `closed` 2026-10-26 `11:00`. One open block Sat 04:00 CDT → Mon 11:00 CDT, containing the UK fall-back at Sat 2026-10-24 20:00 CDT. |
| `svc-8970-BTB-2027spring.txt` | BTB, 2027-03-25..30 | Sat 2027-03-27 `open@04:00` (td 2027-03-29); Sun **no events**; Mon 2027-03-29 `closed@10:00`. Block spans the UK spring-forward at Sat 2027-03-27 20:00 CDT; the close is the *aligned* 10:00 while the opening Saturday was *misaligned*. |
| `svc-10664-ABB-usfallback.txt` | ABB, 2026-10-29..11-03 | Sat 2026-10-31 `open@04:00` (td 2026-11-02); Sun **no events**; Mon 2026-11-02 `closed@02:00`. Block contains the US fall-back at Sun 2026-11-01 02:00 CDT. |
| `svc-8970-BTB-spring.txt` | BTB, 2026-03-26..31 | The **pre-24/7** grid for contrast: `closed@11:00, preopen@11:15, open@11:30` (a 30-minute stop, matching the 2024 FAQ) and a bounded Saturday session `open@05:00 … closed@17:00`, which ends before the Sat 20:00 CDT UK transition. |
