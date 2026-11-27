# Evidence index — task `cde-thanksgiving-2026`

Coinbase Derivatives (CDE) Market Notice **26-41**, "2026 Thanksgiving Schedule", posted 11/17/2026,
effective trade date 11/26/2026 — the operator's published holiday arrangement the
`coinbase_derivatives` holiday table was waiting for. Retrieval session **2026-11-18 08:44–08:49 UTC**.
All retrieval times are UTC (`date -u`), per LAW-UTC-DATES. Complements the earlier capture sets
`../cde-2021-2025/` (2026-09-19) and `../cde-2026-2027/` (2026-09-26), both untouched by this directory.

Access: **`www.coinbase.com` answered 200 directly** this session with `curl --http1.1` and a Windows
Chrome User-Agent (`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/131.0.0.0 Safari/537.36`) — no reader and no Cloudflare interstitial, unlike every earlier
recorded attempt (403 on 2026-09-19 and 2026-09-26). The rendered page embeds the complete notice
table as Contentful rich text, with each notice's PDF address on `assets.ctfassets.net`; the PDFs
fetched directly from that CDN with no special headers.

---

## Documents

| Document | URL | Retrieved (UTC) | sha256 | Bytes | What it is |
|---|---|---|---|---|---|
| `cde_market_notices_raw_20261118.html` | https://www.coinbase.com/derivatives/market-notices | 2026-11-18 08:44:30 | `0e654dc1f206c1063c9832a467851eb790361f4cfd34b2bdb8cb24b5f3ddffdc` | 916,120 | **T1.** The operator's Market Notices listing, byte-exact. 506 table rows; newest Market notices 26-41 / 26-40.1 / 26-40 (all posted 11/17/2026); newest Holiday-category notice 26-41. Source of every PDF address below. |
| `pdf/CDE_Market_Notice_26-41_2026_Thanksgiving.pdf` | https://assets.ctfassets.net/k3n74unfin40/6mrPgfFMekNod6VM9XYhXe/edb6b7ccd00a0e13dc6f5868d956de2e/Market_Notice_26-41_2026_Thanksgiving.pdf | 2026-11-18 08:46:14 | `1b679f80bb7592f059e574e21894b76fd2dbd6c6638b402bec36c36d307065b6` | 121,755 | **T1.** Notice 26-41, dated 11/17/2026: the 2026 Thanksgiving schedule. Rows for trade dates 2026-11-26 (closed) and 2026-11-27 (early close; Equity 12:00 CT, Energy/Copper/Platinum 13:45 CT on the 23x5 grid). |
| `pdf/CDE_Market_Notice_26-37_Q4_2026_Quarterly_Maintenance_Window___FIA_DR_Testing.pdf` | https://assets.ctfassets.net/k3n74unfin40/6cvYvCxcHFMAGEjOM1Cfoy/3830c45e49154425f5c14ffc1b24c0bb/CDE_Market_Notice_26-37_Q4_2026_Quarterly_Maintenance_Window___FIA_DR_Testing.pdf | 2026-11-18 08:48:18 | `97f2d841c43239aba313f7a4c594381767ffb759ee0a2bcc869c1de80f869754` | 97,282 | **T1.** Notice 26-37, dated 09/24/2026: the Q4 quarterly weekend maintenance and FIA DR test, Saturday 2026-10-24, `24x7 Products` only. Out of scope for the 23x5 identity; recorded beside, not encoded. |
| `pdf/CDE_Market_Notice_26-38_Perp_Style_Futures_Expiry_Change.pdf` | https://assets.ctfassets.net/k3n74unfin40/2sRoZMeIy9pkFuSqCO2hTD/504ebb20d57091e0795bcb74630bbfd7/CDE_Market_Notice_26-38_Perp_Style_Futures_Expiry_Change.pdf | 2026-11-18 08:48:18 | `a73215ef95477238e79c6bf04a428c69ab3a9bc15687afa631819dbd41869d8e` | 78,100 | **T1.** Notice 26-38, dated 10/19/2026: the Equity Index Perp Style Futures contracts lose their five-year expiration dates effective Monday 2026-10-26 and become true perpetuals. Contract-lifecycle data, not a session arrangement; out of scope. |
| `pdf/CDE_Market_Notice_26-39_Single_Stock_Perpetual_Futures.pdf` | https://assets.ctfassets.net/k3n74unfin40/3hHvaXDpBYPl0tU9saI05D/14f5318561aac87c31ea1eda3eeeee92/CDE_Market_Notice_26-39_Single_Stock_Perpetual_Futures.pdf | 2026-11-18 08:48:20 | `087febbcc3d3ccce88e091a5cc8864b418b8d7e057324bd134f296d0aae741b3` | 119,015 | **T1.** Notice 26-39, dated 11/09/2026: fifty-seven Single Stock Perpetual Futures launch Sunday 2026-12-13 18:50 CT for trade date 2026-12-14, trading "from Sunday 19:00 CT through Friday 16:00 CT". A product launch on a new off-grid tier; out of scope, no key claimed. |
| `pdf/CDE_Market_Notice_26-40_2027_Quarterly_Weekend_Maintenance_Schedule.pdf` | https://assets.ctfassets.net/k3n74unfin40/3B4vmLmGERXDxO5qegRqsF/666b45f07105724e19a7e30adfe7cb37/9a251f3f-921e-42a7-b516-81e2ed4a87cf.pdf | 2026-11-18 08:48:20 | `9c872f322f194925f29ed9c2bedbd29b962157b59ba4cc50140d1a5abf92bf43` | 85,163 | **T1.** Notice 26-40, dated 11/17/2026: 2027 quarterly weekend maintenance for `24x7 Products`, Q1 on Saturday 2027-01-23 9:00 AM–12:00 PM CT, Q2 2027-04-10, Q3 2027-07-24, Q4 2027-10-23 (FIA DR). Saturdays are outside the 23x5 week; out of scope, not encoded. |
| `pdf/CDE_Market_Notice_26-40.1_Updated_Times_on_2027_Quarterly_Weekend_Maintenance_Schedule.pdf` | https://assets.ctfassets.net/k3n74unfin40/12446Fbkb979ABegaKd3A5/ed18e15fd1630b815612eafc2b707b1f/456e7f48-590d-445b-aa34-a8b43e58e435.pdf | 2026-11-18 08:48:20 | `230533aab8d077bb89d542f9ba8f7804378edb57da42124a6bce4302d528c964` | 87,196 | **T1.** Notice 26-40.1, dated 11/17/2026: amends 26-40 with the updated Q1 window of Saturday 2027-01-23 7:00 AM–10:00 AM CT. Same 24x7-only, Saturday scope; out of scope, not encoded. |
| `txt/*.txt` (6 files) | — (derived) | 2026-11-18 08:50 | see command output in the session record | — | `pdftotext -layout` dumps of the six PDFs; the source of every verbatim quoted in `docs/evidence/coinbase_derivatives.md`. |
| `INDEX.md` | — (this file) | 2026-11-18 | — | — | Register and access log. |

`txt/` dump hashes (sha256):
26-41 `f34e7f413964d85af626377c4791e7326d17982145e954cc523e21a3cdff9f23`;
26-37 `a5ce6244c67975634a82884aece1d0788773f7dc68f3dbe8134cc2c0cbbc33e7`;
26-38 `d5205751b758438e54c09a3e9d6068ce2dc1865fd1553915b7b86803c6a88a82`;
26-39 `81fc305988495ca03857dcd2e5de8b4fc43cb8705ffc881607798e57429af9f6`;
26-40 `1de70263ca9aaea554766caa72b813177d7a01494f2b39a52374fca7ed42ff0c`;
26-40.1 `cda02c90e91fbe049bcc5a655e1feefa2c09cdb54bdd57e6e675eef4d9ede722`.

**Where the PDF addresses came from.** From this session's own listing capture: the page's embedded
Contentful rich text carries each notice's title as a hyperlink node with its
`assets.ctfassets.net` address. Notices 26-40 and 26-40.1 both carry the listing title "2027
Quarterly Weekend Maintenance Schedule"; their identity was settled from the PDFs' own header
blocks (`Notice: 26-40.1` / `Notice: 26-40`), not from listing order.

## Retrieval commands

```text
curl --http1.1 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" \
  -o cde_market_notices_raw_20261118.html https://www.coinbase.com/derivatives/market-notices
# -> HTTP 200, 916120 bytes (no reader needed this session)
curl -o pdf/CDE_Market_Notice_26-41_2026_Thanksgiving.pdf \
  https://assets.ctfassets.net/k3n74unfin40/6mrPgfFMekNod6VM9XYhXe/edb6b7ccd00a0e13dc6f5868d956de2e/Market_Notice_26-41_2026_Thanksgiving.pdf
# -> HTTP 200, 121755 bytes; same pattern for the other five PDFs
pdftotext -layout pdf/*.pdf txt/
shasum -a 256 cde_market_notices_raw_20261118.html pdf/*.pdf txt/*.txt
```

## Scope notes

- **26-41 is the only Holiday-category notice the listing carries above 26-36**, and the only one
  encoded: rows for trade dates 2026-11-26 and 2026-11-27 on the venue's 23x5 grid.
- **26-37, 26-40 and 26-40.1 are 24x7-tier maintenance windows on Saturdays** — outside the 23x5
  week and off the venue default's clock. Recorded beside in the evidence file; nothing to encode.
- **26-38 and 26-39 are product notices** (contract-lifecycle change, product launch), not session
  arrangements; out of scope for a holiday table.
