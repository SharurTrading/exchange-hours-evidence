# `ICE_Futures_US_ExNot2024MomentOfSilence20241230.pdf` — the artifact `#168` recorded as unread

Retrieved 2026-09-26 (UTC date; the wall-clock time was not recorded) from the Wayback raw replay
`https://web.archive.org/web/20250207231515id_/https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_ExNot2024MomentOfSilence20241230.pdf`.

| file | sha256 | bytes |
|---|---|---|
| `ICE_Futures_US_ExNot2024MomentOfSilence20241230.pdf` | `a4dca19c06c46d62886e3379b8db8f95319e94681bd477ac43cac03ce3e002de` | 66,354 |

ICE Futures U.S. notice dated **December 30, 2024**, one page, T1. `pdftotext -layout` twin beside it.

## What it states, verbatim

> In recognition of the passing of President Jimmy Carter, the Exchange will observe a moment of
> silence at 8:18 am NY time on Thursday, January 9, 2025.
>
> Trading in each of the following futures contracts will end at **9:30 am NY time** on that day:
>   Micro NYSE FANG+™ Index futures contracts (contract symbol **FNG**)
>   NYSE Biotechnology GTR Index futures contracts (contract symbol IUT)
>   NYSE Semiconductor GTR Index futures contracts (contract symbol IUS)
>
> Trading in each of the following futures contracts will end at **1:15 pm NY time** on that day:
>   ICE One-Month SOFR Index Futures (SR1); ICE Three-Month SOFR Index Futures (SR3);
>   ICE Conforming 30-year Fixed Mortgage Rate Lock Weighted APR Index Futures (30C);
>   ICE Jumbo 30-year Fixed Mortgage Rate Lock APR Index Futures (30J)
>
> Settlement prices for these contracts will likely reflect prior day settlements, but in the event of
> a significant price move may instead be based on prices during the last minute of trading.
>
> **All other contracts will follow regular trading hours and daily settlement window times.**

## Why it matters

**2025-01-09 is an unstated early close for a served identity.** The `iceus` identity's FANG family
is the *"NYSE FANG+™ Index and ICE Stock, Mortgage and SOFR Index Contracts"* group, and this notice
splits that group on the day: the FANG+/equity-index contracts end at **09:30 NY**, the SOFR and
mortgage contracts at **13:15 NY**, and everything else trades normally.

So `iceus` 2025-01-09 is not an ordinary day, and the venue table's intersection cannot state one
answer for it either — the softs trade a full session while the FANG group closes at 09:30. The
`iceus` change shipped 2025 without a row for it, having recorded this artifact as unread.

**Also note the identity's declared scope.** The ledger's basis note says *"NYSE FANG+ Index Futures
only, not a venue-wide ICE clock"*, while the notice names **Micro** NYSE FANG+ (FNG). Whether the
crate's FANG table covers FNG is a scope question to settle from the table itself, not from this
note.
