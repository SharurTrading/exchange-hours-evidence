Title: FAQ: TAS on Cryptocurrency Futures

URL Source: https://www.cmegroup.com/articles/faqs/tas-on-cryptocurrency-faq.html

Published Time: 2026-05-29T00:00:00.000Z

Markdown Content:
## Latest updates

### 1. What are the latest updates to TAS contracts?

TAS eligibility for [Micro Bitcoin futures](https://www.cmegroup.com/markets/cryptocurrencies/bitcoin/micro-bitcoin.html) has been expanded to include the front, second and third contract months, as well as associated calendar spreads.

## General overview

### 2. What is TAS?

[Trading at Settlement (TAS)](https://www.cmegroup.com/markets/cryptocurrencies/tas-on-cryptocurrency-futures.html) functionality allows market participants to enter a trade at a spread to the yet-to-be-determined daily settlement price of the underlying futures contract calculated at 4:00 p.m. Eastern Time (ET), for subsequent clearing into the existing futures contract. TAS enables clients to transact at or near the futures settlement price, making it particularly useful when replicating an index. TAS is subject to the requirements of Rule 524.A.

### 3. What are the specifications for TAS transactions?

### 4. What is the difference between TAS and BTIC?

TAS transactions are at a spread, or basis, to the yet-to-be-determined daily settlement price of the underlying futures contract.

Basis Trade at Index Close (BTIC) transactions are at a spread, or basis, to the corresponding underlying reference rate.

### 5. What are the vendor codes?

| **PRODUCT NAME** | **CME GLOBEX** | **BLOOMBERG** | **CQG** | **REFINITIV** |
| --- | --- | --- | --- | --- |
| TAS on Bitcoin futures | TBT | TBTA | TBT | TKT |
| TAS on Micro Bitcoin futures | TBM | MBTA | TBM | BTV |
| TAS on Ether futures | TET | TEBA Curncy | TET | TET |
| TAS on Micro Ether futures | TEM | TEYA Curncy | TEM | TKM |
| TAS on SOL futures | TSL | QSLA Curncy | GTSL | OLST |
| TAS on Micro SOL futures | TMS | IMSA Curncy | TMS | KHLT |
| TAS on XRP futures | TXP | TXPA Curncy | GTXP | RXPT |
| TAS on Micro XRP futures | TMX | XRYA Curncy | GTMX | MRXT |

### 6. What is the quoting convention for TAS?

TAS prices are quoted in U.S. dollars per underlying cryptocurrency.

The TAS trading mechanism allows market participants to enter a trade at a spread to the yet-to-be-determined daily settlement price calculated at 4:00 p.m. ET.

TAS trades off a "base price" of zero (equal to the daily settlement price) to create a differential versus the daily settlement price in the underlying futures contract month. The TAS clearing price equals the daily settlement price of the underlying futures contract month plus or minus the TAS transaction price.

**Examples:**

**Bitcoin futures**

Assume a market participant wants to execute TAS on Bitcoin (BTC) futures, at a spread of +2. The participant would transact under its TAS symbol, TBT, at a price of +2. If BTC were to later settle at $100,000, the TBT trade would be replaced with a BTC contract at a price of $100,002. A trade of -2 would result in an execution price of $99,998.

**Micro Ether futures**

Assume a market participant wants to execute TAS on Micro Ether (MET) futures, at a spread of -5. The participant would transact under its TAS symbol, TEM, at a price of -5. If MET were to later settle at $2,500, the TEM trade would be replaced with a MET contract at a price of $2,495.A trade of +5 would result in an execution price of $2,505.

### 7. What is the match algorithm for TAS?

TAS markets match 100% FIFO.

### 8. Are TAS on Cryptocurrency futures eligible for block trading?

Yes, with the following minimum thresholds:

*   Bitcoin futures: 5 contracts
*   Micro Bitcoin futures: 10 contracts
*   Ether futures: 5 contracts
*   Micro Ether futures: 100 contracts
*   SOL futures: 5 contracts
*   Micro SOL futures: 10 contracts
*   XRP futures: 5 contracts
*   Micro XRP futures: 10 contracts

### 9. Will there be block liquidity providers for TAS on Cryptocurrency futures?

Yes. View a list of [block liquidity providers](https://www.cmegroup.com/trading/bitcoin-brokers-and-block-liquidity-providers.html) who have given CME Group consent to disclose their contact information.

View [Rule 526](https://www.cmegroup.com/rulebook/files/cme-group-Rule-526.pdf) in the MRAN to find out more about block trades.

### 10. Are TAS on Cryptocurrency futures available across all listed contracts?

TAS on Bitcoin, Micro Bitcoin, Ether, Micro Ether, SOL, Micro SOL, XRP and Micro XRP futures are available across the nearest three listed expirations in the underlying futures.

For an expiring futures contract, TAS trading shall terminate at 4:00 p.m. ET on the business day immediately preceding the last trade date. For clarity, TAS transactions in expiring futures contracts may not be initiated on the last trade date in such expiring futures.

TAS eligibility for the respective next month is added at 6:00 p.m. ET on the business day immediately preceding the last trade date.

### 11. Are TAS on Cryptocurrency futures available on intra-commodity spreads (calendar spreads)?

TAS on Bitcoin,Micro Bitcoin, Ether, Micro Ether, SOL, Micro SOL, XRP and Micro XRP futures are eligible for calendar spreads between the first three listed expirations.

## Margin and fee details

### 12. When will TAS on Cryptocurrency futures trades be included in the margin calculation?

TAS trades executed by 4:00 p.m. ET will be included in that day’s clearing cycle. TAS transactions consummated after 4:00 p.m. ET will be included in the next day’s clearing cycle, and margin will first be assessed in the intraday cycle on the following day.

### 13. What are the fees for TAS on Cryptocurrency futures?

Fees for TAS on Cryptocurrency futures transactions may be found on our[fee schedule](https://www.cmegroup.com/company/clearing-fees.html).

## Additional information

### 14. How do you distinguish a TAS execution from a futures outright execution?

TAS transactions have distinct product codes that differ from the corresponding outright Cryptocurrency futures. This results in a separate line on the trader’s blotter after the execution that will enable the traders to track their TAS transactions through the day. Once the clearing cycle is complete, the TAS transactions will be consolidated with the corresponding underlying futures contract.

### 15. Is TAS volume added to the corresponding outright futures market volume on a real-time basis?

No, TAS volume is not added to the outright futures volume on a real-time basis. While the final traded futures price of TAS on Cryptocurrency futures transactions will be disseminated to the clearing firms after the cash close, the TAS position will be consolidated with the corresponding underlying futures after the clearing cycle is completed for the day.

### 16. When is the final price of Cryptocurrency futures from TAS transactions disseminated?

Approximately 15 minutes after the daily settlement price calculated at 4:00 p.m. ET, cleared trade data in the corresponding futures will be sent to your clearing firm with a trade price reflecting the settlement price plus (or minus) the differential price at which the TAS was traded. This price will be used when CME Group runs its end-of-day clearing cycle. At that point, the trade will be marked to market versus the daily settlement price in the corresponding futures contract.

### 17. How can I receive the resultant futures price from TAS on Cryptocurrency futures transactions?

You can receive the resultant futures price reflecting the TAS transaction either through your clearing firm or via our Straight Through Processing (STP) solution if you are subscribed. [Find out more about STP](https://www.cmegroup.com/trading/straight-through-processing/).

Contact [GAM_CS@cmegroup.com](mailto:GAM_CS@cmegroup.com) to begin the STP onboarding process.
