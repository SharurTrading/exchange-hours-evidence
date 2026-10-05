Title: 20220718 - CME Group

URL Source: https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html

Markdown Content:
For the latest roadmap of CME Group technology initiatives:

[See the Development Launch Schedule.](https://www.cmegroup.com/globex/develop-to-cme-globex/development-launches.html)

## Critical System Updates

### CME Benchmark Administration Premium SBE Schema Update- August 7

Effective **Sunday, August 7**(trade date Monday, **August 8**), CME Group will launch a new Simple Binary Encoding (SBE) schema on CME Benchmark Administration Premium channel ID 261. With the introduction of the new SBE schema and streaming CVOL, messaging is expected to increase up to 100 packets per second. The new SBE incremental schema will be sent on:

*   [CME Benchmark Administration Premium - SBE UDP Multicast](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+-+SBE+UDP+Multicast)
*   [CME Benchmark Administration Premium - GCP SBE](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+-+GCP+SBE)

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+SBE+Schema+Update)for additional details.

The new SBE schema is currently available for customer testing in New Release.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Update Update - CVOL Live Streaming Launch and SBE Template Migration- August 7

† Denotes update to the article

Effective **Sunday, August 7**(trade date Monday, **August 8**), CME Group will launch CME Group Volatility Index (CVOL™), Live Streaming and migrate all current CVOL messaging to a new Simple Binary Encoding (SBE) template. With this launch, messaging is expected to increase up to 100 packets per second. †A new [republish methodology section](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Streaming+CVOL+Index+Launch+and+SBE+Template+Migration#StreamingCVOLIndexLaunchandSBETemplateMigration-CMEBenchmarkAdministrationPremiumRepublishMethodology) has been added to the Client Impact Assessment.

The CVOL indicator market data messages will be sent on:

*   [CME Benchmark Administration Premium - SBE UDP Multicast](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+-+SBE+UDP+Multicast)
*   [CME Benchmark Administration Premium - GCP SBE](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+-+GCP+SBE)

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Streaming+CVOL+Index+Launch+and+SBE+Template+Migration)for additional details.

These changes are currently available for customer testing in New Release.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### iLink 3 SBE Schema Update- August 28

To support the upcoming CME Globex enhancements, the iLink 3 SBE schema will be updated to **version 8** starting**Sunday, August 28**.More information regarding these enhancements will be published in the future CME Globex Notices. The [overview of iLink 3 schema updates](https://www.cmegroup.com/confluence/display/EPICSANDBOX/iLink+3+SBE+Schema+Update) is now available.

In order to ease customer development efforts, the new SBE schema files will support[Template Extension](https://www.cmegroup.com/confluence/display/EPICSANDBOX/iLink+3+-+Simple+Binary+Encoding#iLink3SimpleBinaryEncoding-TemplateExtension)for iLink 3 messages sent from client systems to CME Globex until the end of day**Friday**,**November 18**.Client systems can send iLink 3 messages using schema version 7 or 8; however CME Globex will only send messages using schema version 8.

**Futures and Options on Futures - Production Rollout**

| DATE | MESSAGES FROM CLIENT | MESSAGES FROM CME GLOBEX |
| --- | --- | --- |
| Currently | V7 | V7 |
| August 28 through October 2: Phased launch | V7 or V8 for market segments that support V8 | V8 for market segments that support 8 |
| October 2 | V7 or V8 for all segments | V8 only |
| November 20 | V8 only | V8 only |

Effective**Sunday, November 20**, version 8 schema will be the only version supported in production. Client systems can only send version 8 messages.

The new version 8 schema is currently available in New Release for customer testing.

To support the new iLink 3 schema rollout the CME SFTP site will be updated as follows:

| NEW RELEASE: /MSGW/PRODUCTION/TEMPLATES |
| --- |
| SCHEMA VERSION | CURRENT STATE | July 5 |
| V7 | ilinkbinary.xml | iLinkbinary_v7.xml |
| V8 | n/a | ilinkbinary.xml |
| PRODUCTION: /MSGW/PRODUCTION/TEMPLATES |
| SCHEMA VERSION | CURRENT STATE | August 28 |
| V7 | ilinkbinary.xml | iLinkbinary_v7.xml |
| V8 | n/a | ilinkbinary.xml |

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Event Contracts- September 18

Effective **Sunday,September 18**(trade date Monday, September 19), [event options contracts](https://www.cmegroup.com/markets/event-based-contracts.html)will be listed for trading on CME Globex, pending completion of all regulatory review periods. Event contracts are daily-expiring, cash settled, European Style, options on futures contracts. Event contracts will provide access to some of our most recognized global products, including metals, energy, equities, and foreign currencies.Additionally, non-tradable underlying futures will be listed to support the new event options. Event contracts will be listed on a new MDP 3.0 channel (329 - Event Contracts).

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Event-Based+Contracts)for additional details.

The event contracts are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CME, CBOT, COMEX, and NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

## Product Launches

### BTICs on New York Cryptocurrency Reference Rates- This Week

Effective this **Sunday,July 24**(trade date Monday, July 25), pending completion of all regulatory review periods, BTICs on New York Cryptocurrency Reference Rates will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| BTICs on New York Cryptocurrency Reference Rates |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| BTIC on Bitcoin futures against New York Close (Bitcoin Reference Rate New York – BRRNY) | BNB | BI | 326 |
| BTIC on Micro Bitcoin futures against New York Close (Bitcoin Reference Rate New York – BRRNY) | MYB | BI | 326 |
| BTIC on Ether futures against New York Close (Ether-Dollar Reference Rate New York - ETHUSD_NY) | ENB | RN | 326 |
| BTIC on Micro Ether futures against New York Close (Ether-Dollar Reference Rate New York - ETHUSD_NY) | EYB | RN | 326 |

These BTICs is currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Enable Trading At Settlement (TAS) Functionality for Micro Crude Oil Futures- August 6

Effective **Saturday, August 6** (trade date Monday, August 8), pending completion of all regulatory review periods, Micro Crude Oil TAS will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| Enable Trading At Settlement (TAS) Functionality for Micro Crude Oil Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| Micro Crude Oil TAS | MCT | CT | 382 |

These Micro Crude Oil TAS will be available for customer testing in New Release on **Monday, July 25.**

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### S&P Select Industry and PHLX Semiconductor Sector Futures- August 7

Effective **Sunday, August 7** (trade date Monday, August 8), pending completion of all regulatory review periods, S&P Select Industry and PHLX Semiconductor Sector futures will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| S&P Select Industry and PHLX Semiconductor Sector Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| E-mini S&P Regional Banks Select Industry Futures | SXB | X3 | 318 |
| BTIC on E-mini S&P Regional Banks Select Industry Futures | RKT | H4 |
| E-mini S&P Insurance Select Industry Futures | SXI | X4 |
| BTIC on E-mini S&P Insurance Select Industry Futures | IST | H5 |
| E-mini S&P Biotechnology Select Industry Futures | SXT | X5 |
| BTIC on E-mini S&P Biotechnology Select Industry Futures | BOT | H6 |
| E-mini S&P Oil & Gas Exploration & Production Select Industry Futures | SXO | X6 |
| BTIC on E-mini S&P Oil & Gas Exploration & Production Select Industry Futures | SWT | H7 |
| E-mini S&P Retail Select Industry Futures | SXR | X7 |
| BTIC on E-mini S&P Retail Select Industry Futures | RET | H8 |
| E-mini PHLX Semiconductor Sector Futures | SOX | X9 |
| BTIC on E-mini PHLX Semiconductor Sector Futures | SOT | H9 |

These futures will be available for customer testing in New Release on **Monday, July 25.**

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Listing Cobalt Metal (Fastmarkets) Futures Spreads- August 7

Effective **Sunday, August 7** (trade date Monday, August 8), the CME will add Cobalt Metal (Fastmarkets) futures spreads for the first 6 contract months on CME Globex.

| **Listing Cobalt Metal (Fastmarkets) Futures Spreads** |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | **Tag 762- SecuritySubType** |
| Cobalt Metal (Fastmarkets) Futures | COB | CA | SP (Standard Calendar Spreads) |

These futures spreads will be available for customer testing in New Release on **Monday, July 25.**

These contracts are listed with, and subject to, the rules and regulations of COMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Financially Settled TTF Futures and Options- August 7

Effective **Sunday, August 7** (trade date Monday, August 8), pending completion of all regulatory review periods, Financially Settled TTF futures and options will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| **Financially Settled TTF Futures and Options** |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| Dutch TTF Natural Gas (USD/MMBtu) Futures | TFU | FD | 386 |
| Dutch TTF Natural Gas (USD/MMBtu) Futures-Style Margined Average Price Option | TFF | T7- OUTS T8- UDS | 387 |
| Dutch TTF Natural Gas (USD/MMBtu) Average Price Option | TFP |

These contracts will be available for customer testing in New Release on **Monday, July 25.**

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### CBL Carbon Offset Trailing Futures- August 7

Effective **Sunday,August 7**(trade date Monday, August 8), pending completion of all regulatory review periods, CBL Carbon Offset trailing futures will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| CBL Carbon Offset Trailing Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| CBL Core Global Emissions Offset Trailing (C-GEO-TR) Futures | COT | VX | 380 |
| CBL Nature-Based Global Emissions Offset Trailing (N-GEO-TR) Futures | NOT | VX | 380 |

These CBL Carbon Offset trailing futures will be available for customer testing in New Release on **Monday, July 25**.

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Lumber Futures and Options on Lumber Futures- August 7

Effective **Sunday, August 7** (trade date Monday, August 8), pending completion of all regulatory review periods, Lumber Futures and Options on Lumber futures will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| Lumber Futures and Options on Lumber Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| Lumber Futures | LBR | LU | 316 |
| Options on Lumber Futures | LBR | W3 | 317 |

These contracts will be available for customer testing in New Release on **Monday, July 25.**

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Listing Pack Spreads on 3-Month SOFR Futures: Resting Order Eliminations- August 28

Effective **Sunday, August 28** (trade date Monday, August 29), pack spreads on 3-Month SOFR futures for 1-year average priced bundle future spreads (tag 762-SecuritySubtype=SB) will be listed for trading on CME Globex. With this listing,

*   certain existing Balanced Strip Spreads (SB) for example, SR3 1-Year AB vs. 1-Year AB spreads will be removed.

*   the external alias on specific balanced SB spreads for example 1-Year AB vs. 1-Year AB spreads will reflect PK for example, SR3:SB PK to support both consecutive and non-consecutive 1-Year SB spreads based upon the two nearest quarterly months to expiration.

To facilitate this change, customers will be asked to cancel all Good ‘Till Cancel (GTC) and Good ‘Till Date (GTD) orders for existing 1-year average priced bundle future spreads, by the close on Friday, August 26. After 16:00 CT on Friday, August 26, any remaining GT orders on these markets will be removed by the CME Global Command Center (GCC).

| Listing Pack Spreads on 3-Month SOFR Futures: Resting Order Eliminations |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | TAG 762-SECURITYSUBTYPE | TAG 969 - MINPRICEINCREMENT | MDP 3.0 CHANNEL |
| 3-Month SOFR Pack Spread | SR3 | SS | PK (Pack Spread) | 0.100000000 | 312 |

These spreads will be available for customer testing in New Release on **Monday, August 1.**

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Event Contracts- September 18

Effective **Sunday,September 18**(trade date Monday, September 19), [event options contracts](https://www.cmegroup.com/markets/event-based-contracts.html)will be listed for trading on CME Globex, pending completion of all regulatory review periods. Event contracts are daily-expiring, cash settled, European Style, options on futures contracts. Event contracts will provide access to some of our most recognized global products, including metals, energy, equities, and foreign currencies.Additionally, non-tradable underlying futures will be listed to support the new event options. Event contracts will be listed on a new MDP 3.0 channel (329 - Event Contracts).

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Event-Based+Contracts)for additional details.

The event contracts are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CME, CBOT, COMEX, and NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Bursa Malaysia Derivatives (BMD) Crude Palm Oil vs East Malaysia Crude Palm Oil Inter-Commodity Futures Spreads- October 2

Effective **Sunday,October 2**(trade date Monday, October 3),and pending final regulatory approval, inter-commodity spreads between Bursa Malaysia Derivatives (BMD)’s Crude Palm Oil vs BMD East Malaysia Crude Palm Oil futures will be made available for trading on CME Globex.

| BURSA MALAYSIA DERIVATIVES (BMD) CRUDE PALM OIL VS EAST MALAYSIA CRUDE PALM OIL INTER-COMMODITY FUTURES SPREADS |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | TAG 762-SECURITYSUBTYPE | Market Data Channel |
| Crude Palm Oil vs East Malaysia Crude Palm Oil Futures | FCPO | BC | IS | 430 |

This change is currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of BMD.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### 30-Year Uniform Mortgage-Backed Security (UMBS) To-Be-Announced (TBA) Futures- October 2

Effective Sunday, **October 2** (trade date Monday, October 3), pending completion of all regulatory review periods, 30-Year Uniform Mortgage-Backed Security (UMBS) To-Be-Announced (TBA) futures will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| **30-Year Uniform Mortgage-Backed Security (UMBS) To-Be-Announced (TBA) Futures** |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| 30-Year UMBS TBA Futures - 2.0% Coupon | 20U | BM | 344 |
| 30-Year UMBS TBA Futures - 2.5% Coupon | 25U |
| 30-Year UMBS TBA Futures - 3.0% Coupon | 30U |
| 30-Year UMBS TBA Futures - 3.5% Coupon | 35U |
| 30-Year UMBS TBA Futures - 4.0% Coupon | 40U |
| 30-Year UMBS TBA Futures - 4.5% Coupon | 45U |
| 30-Year UMBS TBA Futures - 5.0% Coupon | 50U |

These futures are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CBOT.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

## Product Changes

### New New - Delisting and Removal of eight (8) NYMEX Refined and LNG Futures Contracts- July 18

On **Monday, July 18,**the following eight (8) NYMEX Refined and LNG futures contracts were delisted, and effective close of business **Friday, July 22**, these futures will be removed from CME Globex.

| Delisting and Removal of eight (8) NYMEX Refined and LNG Futures Contracts |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group |
| LNG DES Japan (RIM) Futures | JNG | GU |
| Singapore Fuel Oil 180 cst (Platts) Mini Weekly Spread Futures | SDM | PT |
| Singapore Fuel Oil 380 cst (Platts) Mini Weekly Spread Futures | SMW | PT |
| European 3.5% Fuel Oil Barges FOB Rdam (Platts) Mini Weekly Spread | EMW | ZZ |
| Mini Middle East Naphtha FOB Arab Gulf (Platts) Futures | MME | PT |
| Mini Middle East HSFO 380 cst FOB Arab Gulf (Platts) Futures | MSE | PT |
| Mini Middle East Naphtha FOB Arab Gulf (Platts) BALMO Futures | MNE | PT |
| Mini Middle East HSFO 380 cst FOB Arab Gulf (Platts) BALMO Futures | MHS | PT |

These futures currently have no open interest.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Renaming BTICs on Cryptocurrency Futures- This Week

Effective this **Sunday, July 24** (trade date Monday, July 25), the BTICs on Cryptocurrency futures will be renamed as follows:

| **Renaming BTICs on Cryptocurrency Futures** |
| --- |
| **Current Product Name** | New Product Name | iLink: tag 1151-Security Group MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group |
| BTIC on Bitcoin futures | BTIC on Bitcoin futures against London Close (Bitcoin Reference Rate – BRR) | BTB | BX |
| BTIC on Micro Bitcoin futures | BTIC on Micro Bitcoin futures against London Close (Bitcoin Reference Rate – BRR) | MIB | BX |
| BTIC on Ether futures | BTIC on Ether futures against London Close (Ether-Dollar Reference Rate – ETHUSD_RR) | ETB | RJ |
| BTIC on Micro Ether futures | BTIC on Micro Ether futures against London Close (Ether-Dollar Reference Rate – ETHUSD_RR) | EMB | RJ |

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Update Update - Listing Cycle Expansion for 3-Month SOFR Futures- This Week

† Denotes update to the article

Effective this **Sunday, July 24** (trade date Monday, July 25), the listing cycle for the Three-Month SOFR futures will be expanded on CME Globex as follows:

| Listing Cycle Expansion for 3-Month SOFR Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Current Listing Schedule | New Listing Schedule |
| Three-Month SOFR Futures | SR3 | SS | 39 quarterly months | 4 serial contract months and 41 quarterly months |

**†Please note:** Any contract with at least 4 months to expiration will be 1/4-tick eligible.

This change is currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Update Update - Change to Price Format for Dow Jones Real Estate Futures: Resting Order Eliminations- August 7

† Denotes update to the article

Effective**Sunday, August 7**(trade date Monday, August 8), the price format for Dow Jones Real Estate futures will be changed as follows:

†Please Note:To facilitate this change, customers will be asked to cancel all Good ‘Till Cancel (GTC) and Good ‘Till Date (GTD) orders for these contracts, by the close on Friday, August 5. After 16:00 CT on Friday, August 5, any remaining GT orders on these markets will be removed by the CME Global Command Center (GCC).

| **Change to Price Format for Dow Jones Real Estate Futures** |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | CURRENT TAG 9787-DISPLAYFACTOR | NEW TAG 9787-DISPLAYFACTOR | †CURRENT **TAG 969 - MINPRICEINCREMENT** | †NEW **TAG 969 - MINPRICEINCREMENT** |
| Dow Jones Real Estate Futures | RX | RX | 0.100000000 | 0.010000000 | † 1 | † 10 |

This change is currently available in New Release for customer testing.

These contracts are listed with, and subject to, the rules and regulations of †CBOT.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### Changes to Silver and Copper Weekly Monday and Wednesday Options: Resting Order Eliminations- August 7

Effective**Sunday, August 7**(trade date Monday, August 8), pending regulatory approval, the match algorithm for silver and copper weekly Monday and Wednesday options will be amended as follows:

Please Note:To facilitate this change, customers will be asked to cancel all Good ‘Till Cancel (GTC) and Good ‘Till Date (GTD) orders for these contracts, by the close on Friday, August 5. After 16:00 CT on Friday, August 5, any remaining GT orders on these markets will be removed by the CME Global Command Center (GCC).

| **Changes Silver and Copper Weekly Monday and Wednesday Options: Resting Order Eliminations** |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | CURRENT TAG 1142-MATCHALGORITHM | NEW TAG 1142-MATCHALGORITHM |
| Silver Weekly Monday Option | M1S - M5S | SO (UDS: S1) | K-Split FIFO and C-Pro Rata | F-FIFO |
| Copper Weekly Monday Option | H1M - H5M | 1U (UDS: 2U) |
| Silver Weekly Wednesday Option | W1S-W5S | SO (UDS: S1) |
| Copper Weekly Wednesday Option | H1W - H5W | 1U (UDS: 2U) |

These changes is currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CBOT.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

### New New - Change to Strike Price Listing for Options on Equity Index Futures- August 21

Effective this **Sunday, August 21** (trade date Monday, August 22), the strike price listing rule will be changed for multiple options on Equity Futures on CME Globex and for submission for clearing via CME ClearPort.

| Change to Strike Price Listing for Options on Equity Index Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Current Strike Price Listing | New Strike Price Listing |
| Options on E-mini Standard and Poor's 500 Stock Price Index Futuress | ES | EW | 100 index point integer multiples, when listed: +30% to -50% of the prior day’s settlement price on the underlying future contract. 50 index point integer multiples, 366 days prior to expiry (1 calendar year): +20% to -40% of the prior day’s settlement price on the underlying future contract. 10 index point integer multiples, 186 days prior to expiry (6-months prior to expiration): +10% to -25% of the prior day’s settlement price on the underlying future contract. 5 index point integer multiples, 35 days prior to expiry (or 5 Weeks): +5% to -15% of the prior day’s settlement price on the underlying future contract. Dynamic strike allowed at 5. | Strikes listed 30% of the underlying settlement price above and 80% below the at-the-money strike at 100 index point strike increment when listed. Strikes listed 15% above and 40% below the at-the-money strike at 50 index point strike increment within 366 days to expiration. Strikes listed 10% above and 20% below the at-the-money strike at 10 index point strike increment within 126 days to expiration. Strikes listed 5% above and 10% below the at-the-money strike at 5 index point strike increment within 14 days to expiration. Dynamic strikes in 5 index point strike increments. |
| Monday Weekly Options on E-mini Standard and Poor's 500 Stock Price Index Futures - Week 1-5 (European-Style) | E1A-E5A | EW |
| Tuesday Weekly Options on E-mini Standard and Poor's 500 Stock Price Index Futures - Week 1-5 (European-Style) | E1B-E5B | EW |
| Wednesday Weekly Options on E-mini Standard and Poor's 500 Stock Price Index Futures - Week 1-5 (European-Style) | E1C-E5C | EW |
| Thursday Weekly Options on E-mini Standard and Poor's 500 Stock Price Index Futures - Week 1-5 (European-Style) | E1D-E5D | EW |
| Weekly Options on E-mini Standard and Poor's 500 Stock Price Index Futures - Week 1-5 (European-Style) | EW1-EW4 | EW |
| Options on E-mini Standard and Poor's 500 Stock Price Index Futures - End-of-Month (European-Style) | EW | EW |
| Options on E-mini Standard and Poor's 500 Stock Price Index Futures - Quarterly PM (European-Style) | EYC | CM | Strikes of 100, 200, 1100, 2100, 2200, 3100, 4100, 4200, 5100, 6100, 7100 and 8100 available for each contract month, and in addition permit additional strikes to be created by special request at a multiple of 100 index points | Strikes listed at 100, 200, 1100, 2100, 2200, 3100 ,4100, 4200, 5100, 6100, 7100, and 8100 index points. Dynamic strikes allowed at 100 index point strike increments. |
| Options on Micro E-mini Standard and Poor’s 500 Stock Price Index Futures | MES | EO | 100 index point integer multiples, when listed: +30% to -50% of the prior day’s settlement price on the underlying future contract. 50 index point integer multiples, when listed: +20% to -40% of the prior day’s settlement price on the underlying future contract. 10 index point integer multiples, when the underlying future is the second closest contract: +10% to -25% of the prior day’s settlement price on the underlying future contract. 5 index point integer multiples, 35 days prior to expiry (or 5 Weeks): +5% to -15% of the prior day’s settlement price on the underlying future contract. | Strikes listed 30% of the underlying settlement price above and 80% below the at-the-money strike at 100 index point strike increment when listed. Strikes listed 15% above and 40% below the at-the-money strike at 50 index point strike increment within 366 days to expiration. Strikes listed 10% above and 20% below the at-the-money strike at 10 index point strike increment within 126 days to expiration. Strikes listed 5% above and 10% below the at-the-money strike at 5 index point strike increment within 14 days to expiration. Dynamic strikes in 5 index point strike increments. |
| Weekly Options on Micro E-mini Standard and Poor’s 500 Stock Price Index Futures - Week 1-4 (European-Style) | EX1-EX4 | EO |
| Options on Micro E-mini Standard and Poor’s 500 Stock Price Index Futures - End-of-Month (European-Style) | EX | EO |
| Options on E-mini Standard & Poor's MidCap 400 Stock Price Index Futures | EMD | MC | 5-point intervals within ± 20% previous day’s settlement price of the underlying futures. Once the contract becomes the second nearest cycle month contract, 2.5-point intervals within ± 15 Index points of previous day’s settlement price of the underlying futures. Exercise prices for serial options shall be identical to the exercise prices that are listed for the March quarterly options on the same underlying futures contract. | Strikes listed 15% of the underlying settlement price above and 25% below the at-the-money strike at 100 index point strike increment when listed. Additional strikes listed for 5% of the underlying settlement price above and 10% below the at-the-money strike at 10 index point increment within 14 days to expiration. Dynamic strikes allowed at 5 index point increment. |
| Weekly Options on E-mini Standard & Poor's MidCap 400 Stock Price Index Futures | ME3 | MC |
| Options on E-mini Nasdaq-100 Index Futures | NQ | QZ | 500 index point integer multiples, when listed: +30% to -50% of the prior day’s settlement price on the underlying future contract. 100 index point integer multiples, 186 days prior to expiry: +20% to -40% of the prior day’s settlement price on the underlying future contract. 50 index point integer multiples, 96 days prior to expiry: +10% to -25% of the prior day’s settlement price on the underlying future contract. 10 index point integer multiples, 35 days prior to expiry (or 5 Weeks): +5% to -10% of the prior day’s settlement price on the underlying future contract. Dynamic strike allowed at 10. | Strikes listed 30% of the underlying settlement price above and 80% below the at-the-money strike at 500 index point strike increments when listed. Strikes listed 20% of the underlying settlement price above and 40% below the at-the-money strike at 100 index point strike increments within 96 days to expiration. Strikes listed 10% of the underlying settlement price above and 20% below the at-the-money strike at 50 index point strike increments within 35 days to expiration. Strikes listed 5% of the underlying settlement price above and 10% below the at-the-money strike at 10 index point strike increments within 14 days to expiration. Dynamic strikes allowed at 10 index point strike increment. |
| Monday Weekly Options on E-mini Nasdaq-100 Index Futures - Week 1-5 (European-Style) | Q1A-Q5A | NW |
| Wednesday Weekly Options on E-mini Nasdaq-100 Index Futures - Week 1-5 (European-Style) | Q1C-Q5C | NW |
| Weekly Options on E-mini Nasdaq-100 Index Futures - Week 1-4 (European-Style) | QN1-QN4 | NW |
| Options on E-mini Nasdaq-100 Index Futures - End-of-Month (European-Style) | QNE | NW |
| Options on Micro E-mini Nasdaq-100 Index Futures | MNQ | NE | 100 index point integer multiples, when listed: +30% to -50% of the prior day’s settlement price on the underlying future contract 10 index point integer multiples, when the underlying future is the closest contract: +10% to -20% of the prior day’s settlement price on the underlying future contract | Strikes listed 30% of the underlying settlement price above and 80% below the at-the-money strike at 500 index point strike increments when listed. Strikes listed 20% of the underlying settlement price above and 40% below the at-the-money strike at 100 index point strike increments within 96 days to expiration. Strikes listed 10% of the underlying settlement price above and 20% below the at-the-money strike at 50 index point strike increments within 35 days to expiration. Strikes listed 5% of the underlying settlement price above and 10% below the at-the-money strike at 10 index point strike increments within 14 days to expiration. Dynamic strikes allowed at 10 index point strike increment. |
| Weekly Options on Micro E-mini Nasdaq-100 Index Futures - Week 1-4 (European-Style) | MQ1-MQ4 | NE |
| Options on Micro E-mini Nasdaq-100 Index Futures - End-of-Month (European-Style) | MQE | NE |
| Options on E-mini® Russell 2000® Index Futures | RTO | R4 | 50 index point integer multiples, when listed: -50% to +30% of the prior day’s settlement price on the underlying future contract. 10 index point integer multiples, 186 days prior to expiry: -25% to +10% of the prior day’s settlement price on the underlying future contract. 5 index point integer multiples, 35 days prior to expiry (or 5 Weeks): -15% to +5% of the prior day’s settlement price on the underlying future contract. | Strikes listed 30% of the underlying settlement price above and 80% below the at-the-money strike at 100 index point strike increment when listed. Strikes listed 30% above and 50% below the at-the-money strike at 50 index point strike increment within 96 days to expiration. Strikes listed 10% above and 20% below the at-the-money strike at 10 index point strike increment within 66 days to expiration. Strikes listed 5% above and 10% below the at-the-money strike at 5 index point strike increment within 14 days to expiration. Dynamic strikes in 5 index point strike increments. |
| Monday Weekly Options on E-mini® Russell 2000® Index Futures - Week 1-5 (European-Style) | R1A-R5A | R4 |
| Wednesday Weekly Options on E-mini® Russell 2000® Index Futures - Week 1-5 (European-Style) | R1C-R5C | R4 |
| Weekly Options on E-mini Russell 2000 Index Futures | R1E-R4E | R4 |
| Options on E-mini® Russell 2000® Index Futures - End-of-Month | RTM | R4 |
| Options on E-mini S&P SmallCap 600 Stock Price Index Futures | SMC | 7S | Deferred month: 5-point intervals. Once the contract becomes the second nearest contract, 2.5-point intervals will be available. | Dynamic strikes permitted at 5 index point increments. |
| CBOT E-mini Dow Jones Industrial Average Index ($5 Multiplier) Futures Options | OYM | C9 | 500-point intervals within ± 50% pervious day's settlement price of the underlying futures. 100- point intervals within ± 20% previous day's settlement price of the underlying futures. 50- point intervals within ± 10% previous day's settlement price of the underlying futures for the two nearest quarterly cycle month options. | Strikes listed for 30% of the underlying settlement price above and 50% below the at-the-money strike at 1000 point strike increments when listed. Strikes listed for 10% of the underlying settlement price above and 20% below the at-the-money strike at 100 point strike increments within 35 days to expiration. Strikes listed for 5% of the underlying settlement price and 10% below the at-the-money strike at 50 point strike increments within 14 days to expiration. Dynamic strikes permitted at 50 index point increments. |
| CBOT E-mini Dow Jones Industrial Average Index ($5 Multiplier) Weekly Option - week 1-4 | YM1-YM4 | OL |
| CBOT E-mini Dow Jones Industrial Average Index ($5 Multiplier) End-of-Month Option | EYM | OL |

These options will be available for customer testing in New Release on **Monday, August 8.**

These contracts are listed with, and subject to, the rules and regulations of CME and CBOT.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)

## Events and Announcements

### CME Group DR Datacenter Migration and Test

CME Group is pleased to announce the move and upgrade of our backup datacenter as part of our commitment to the protection of our customers. Last year, we completed the migration of our Disaster Recovery clearing systems, and we are now focused on CME Globex and supporting systems. To ensure customer can connect to our new backup datacenter, CME Group will be holding mock disaster recovery testing on **Saturday, September 10**.

**Please Note:**Customers do not need to test from Disaster Recovery – please plan to stay in your production environment.

Customers must [register](https://www.cmegroup.com/events/2022/dr-testing-for-futures-and-options-markets.html) in advance to participate. Please review the [mock trading script](https://www.cmegroup.com/content/dam/cmegroup/notices/electronic-trading/2022/06/coresitedrmock.pdf) for additional details.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/07/20220718.html#top)
