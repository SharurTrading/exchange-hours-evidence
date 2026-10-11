<!-- SPDX-License-Identifier: MIT-0 -->

# Legacy OANDA FIX context — 2026-10-11 UTC

The operator's FIX Rules of Engagement specification was retrieved through
[the August 2012 Wayback replay](https://web.archive.org/web/20120816084810id_/http://fxtrade.oanda.com:80/images/FixSpecifications2.pdf).
Its cover says last updated November 25, 2011 and names fxTrade and fxTrade
Practice FIX Server 2.3.20. The original PDF bytes are retained; the text is a
derivative. Independent extraction and visual inspection of page 8 confirm
continuous currency trading during the trading week and typically Friday
system maintenance after market close starting at 5 p.m. Eastern.

The adjacent DAY-order expiry paragraph describes order lifecycle and is not a
session boundary. This specification does not establish the complete opening
and closing endpoints of the week, the UK legal-entity scope at the permanent
2010 floor, or an unconditional later change date. It is context for ongoing
research in exchange-hours-rs#332, not complete history or runtime data.

The four saved CDX query responses and retrieval results are also retained.
Three specified hours-pattern queries return empty arrays; the FIX-document
query returns one capture. Empty results concern those exact queries and do
not establish that all archive research angles are exhausted. The capture is
an observation date, distinct from the document's own last-updated date; neither
is fabricated into an effective day.

`pdf-retrieval.json` records the replay and original URLs, byte length and
reproduced digest. `SHA256SUMS.txt` fences all files in this directory except
itself. No broker contact occurred.
