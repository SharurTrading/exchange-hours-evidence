Title: 20220801 - CME Group

URL Source: https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html

Markdown Content:
For the latest roadmap of CME Group technology initiatives:

[See the Development Launch Schedule.](https://www.cmegroup.com/globex/develop-to-cme-globex/development-launches.html)

## Critical Updates

### CME Benchmark Administration Premium SBE Schema Update- This Week

Effective this**Sunday, August 7**(trade date Monday, August 8), CME Group will launch a new Simple Binary Encoding (SBE) schema on CME Benchmark Administration Premium channel ID 261. With the introduction of the new SBE schema and streaming CVOL, messaging is expected to increase up to 100 packets per second. The new SBE incremental schema will be sent on:

*   [CME Benchmark Administration Premium - SBE UDP Multicast](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+-+SBE+UDP+Multicast)
*   [CME Benchmark Administration Premium - GCP SBE](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+-+GCP+SBE)

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+SBE+Schema+Update)for additional details.

The new SBE schema is currently available for customer testing in New Release.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### CVOL Live Streaming Launch and SBE Template Migration- This Week

Effective this **Sunday, August 7**(trade date Monday, August 8), CME Group will launch CME Group Volatility Index (CVOL™), Live Streaming and migrate all current CVOL messaging to a new Simple Binary Encoding (SBE) template. With this launch, messaging is expected to increase up to 100 packets per second. A new [republish methodology section](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Streaming+CVOL+Index+Launch+and+SBE+Template+Migration#StreamingCVOLIndexLaunchandSBETemplateMigration-CMEBenchmarkAdministrationPremiumRepublishMethodology) has been added to the Client Impact Assessment.

The CVOL indicator market data messages will be sent on:

*   [CME Benchmark Administration Premium - SBE UDP Multicast](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+-+SBE+UDP+Multicast)
*   [CME Benchmark Administration Premium - GCP SBE](https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+Benchmark+Administration+Premium+-+GCP+SBE)

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Streaming+CVOL+Index+Launch+and+SBE+Template+Migration)for additional details.

These changes are currently available for customer testing in New Release.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### iLink 3 SBE Schema Update- August 28

To support the upcoming CME Globex enhancements, the iLink 3 SBE schema will be updated to **version 8** starting**Sunday, August 28**.More information regarding these enhancements will be published in the future CME Globex Notices. The [overview of iLink 3 schema updates](https://www.cmegroup.com/confluence/display/EPICSANDBOX/iLink+3+SBE+Schema+Update) is now available.

In order to ease customer development efforts, the new SBE schema files will support[Template Extension](https://www.cmegroup.com/confluence/display/EPICSANDBOX/iLink+3+-+Simple+Binary+Encoding#iLink3SimpleBinaryEncoding-TemplateExtension)for iLink 3 messages sent from client systems to CME Globex until the end of day**Friday, November 18**.Client systems can send iLink 3 messages using schema version 7 or 8; however CME Globex will only send messages using schema version 8.

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

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Event Contracts- September 18

Effective **Sunday,September 18**(trade date Monday, September 19), [event options contracts](https://www.cmegroup.com/markets/event-based-contracts.html)will be listed for trading on CME Globex, pending completion of all regulatory review periods. Event contracts are daily-expiring, cash settled, European Style, options on futures contracts. Event contracts will provide access to some of our most recognized global products, including metals, energy, equities, and foreign currencies.Additionally, non-tradable underlying futures will be listed to support the new event options. Event contracts will be listed on a new MDP 3.0 channel (329 - Event Contracts).

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Event-Based+Contracts)for additional details.

The event contracts are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CME, CBOT, COMEX, and NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### New New - Energy Gasoil Crack Spreads - September 18

Effective **Sunday, September 18** (trade date Monday, September 19), new exchange defined Energy Gasoil Crack spreads will be made available for trading on CME Globex. The new spreads will use a new strategy type (TB) and trade at a reduced tick.

The TB spread is an inter-commodity ratio futures spread allowing the simultaneous purchase (sale) of a distilled product (i.e., Low Sulphur Gasoil) with a corresponding sale (purchase) of the raw product from which it was produced (i.e., Crude Oil).

To support the launch of the Gasoil Crack spreads on**August 28**, tag 6937-Asset for European Low Sulphur Gasoil (100mt) Bullet futures will change from [GLI to 7F](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html?#pccelsgbf).

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Energy+Gasoil+Crack+Spreads+on+CME+Globex) for additional details.

These changes will be available for customer testing in New Release on **Monday, August 8**.

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### iLink 3 Order Cancel and Cancel/Replace Requests by ClOrdID- October 2

Starting **Sunday, October 2** (trade date Monday, October 3), CME Group will begin launching a new risk management feature that allows clients to cancel and modify resting orders using FIX tag 11-ClOrdID, without providing tag 37-OrderID. This feature will be enabled for all CME Group futures and options on futures on CME Globex. It is only available on iLink 3 sessions using the v8 schema. However, iLink 2 sessions are also impacted by this launch.

Prior to each launch weekend, clients must ensure all resting Good Till Cancel (GTC) and Good Till Date (GTD) orders have a unique tag 11-ClOrdID value per SenderComp and market segment. On each launch weekend, any resting GTC/GTD orders will be evaluated for duplicative ClOrdID values per SenderComp and market segment. Orders with duplicate values will be eliminated prior to the open.

Please review the [Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/iLink+3+Order+Cancel+and+Cancel-Replace+Requests+by+ClOrdID) for full technical details and launch schedule.

Certification in AutoCert+ is required to utilize the new Order Cancel and Cancel/Replace Requests by ClOrdID functionality. This change and the new AutoCert+ test suite will be available in New Release for customer testing and certification effective **Monday, August 15**.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

## Product Launches

### Enable Trading At Settlement (TAS) Functionality for Micro Crude Oil Futures- This Week

Effective this **Sunday, August 7** (trade date Monday, August 8), pending completion of all regulatory review periods, Micro Crude Oil TAS will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| Enable Trading At Settlement (TAS) Functionality for Micro Crude Oil Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| Micro Crude Oil TAS | MCT | CT | 382 |

This Micro Crude Oil TAS is currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### S&P Select Industry and PHLX Semiconductor Sector Futures- This Week

Effective this **Sunday, August 7** (trade date Monday, August 8), pending completion of all regulatory review periods, S&P Select Industry and PHLX Semiconductor Sector futures will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

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

These futures are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Listing Cobalt Metal (Fastmarkets) Futures Spreads- This Week

Effective this **Sunday, August 7** (trade date Monday, August 8), the CME will add Cobalt Metal (Fastmarkets) futures spreads for the first 6 contract months on CME Globex.

| **Listing Cobalt Metal (Fastmarkets) Futures Spreads** |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | **Tag 762- SecuritySubType** |
| Cobalt Metal (Fastmarkets) Futures | COB | CA | SP (Standard Calendar Spreads) |

These futures spreads are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of COMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Financially Settled TTF Futures and Options- This Week

Effective this **Sunday, August 7** (trade date Monday, August 8), pending completion of all regulatory review periods, Financially Settled TTF futures and options will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| **Financially Settled TTF Futures and Options** |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| Dutch TTF Natural Gas (USD/MMBtu) Futures | TFU | FD | 386 |
| Dutch TTF Natural Gas (USD/MMBtu) Futures-Style Margined Average Price Option | TFF | T7- OUTS T8- UDS | 387 |
| Dutch TTF Natural Gas (USD/MMBtu) Average Price Option | TFP |

These contracts are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### CBL Carbon Offset Trailing Futures- This Week

Effective this **Sunday,August 7**(trade date Monday, August 8), pending completion of all regulatory review periods, CBL Carbon Offset trailing futures will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| CBL Carbon Offset Trailing Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| CBL Core Global Emissions Offset Trailing (C-GEO-TR) Futures | COT | VX | 380 |
| CBL Nature-Based Global Emissions Offset Trailing (N-GEO-TR) Futures | NOT | VX | 380 |

These CBL Carbon Offset trailing futures are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Lumber Futures and Options on Lumber Futures- This Week

Effective this **Sunday, August 7** (trade date Monday, August 8), pending completion of all regulatory review periods, Lumber Futures and Options on Lumber futures will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| Lumber Futures and Options on Lumber Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | Market Data Channel |
| Lumber Futures | LBR | LU | 316 |
| Options on Lumber Futures | LBR | W3 | 317 |

These contracts are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### New New - WTI Midland (Argus) BALMOs - August 28

Effective **Sunday, August 28** (trade date Monday, August 29) and pending completion of all regulatory review periods, WTI Midland (Argus) BALMOs will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| **WTI Midland (Argus) BALMOs** |
| --- |
| **Product** | **MDP 3.0: tag 6937-Asset** | **iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group** | **Market Data Channel** |
| WTI Midland (Argus) vs. WTI Trade Month BALMO futures | WTB | CC | 382 |
| WTI Midland (Argus) vs. WTI Financial BALMO futures | FFB | CC | 382 |

These WTI Midland (Argus) BALMOs will be available for customer testing in New Release on **Monday, August 8**.

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Listing Spreads on 3-Month SOFR Futures: Resting Order Eliminations- August 28

Effective **Sunday, August 28** (trade date Monday, August 29), †spreads on 3-Month SOFR futures for 1-year average priced bundle future spreads (tag 762-SecuritySubtype=SB) will be listed for trading on CME Globex. With this listing:

*   1-Year SB spreads will be listed with the external instrument name, tag 55-Symbol in MDP 3.0 on specific balanced SB spreads for example 1-Year AB vs. 1-Year AB spreads reflecting PK for example, SR3:SB PK to support non-consecutive 1-Year SB spreads based upon the two nearest quarterly months to expiration.

To facilitate this change, customers will be asked to cancel all Good ‘Till Cancel (GTC) and Good ‘Till Date (GTD) orders for existing 1-year average priced bundle future spreads, by the close on Friday, August 26. After 16:00 CT on Friday, August 26, any remaining GT orders on these markets will be removed by the CME Global Command Center (GCC).

| Listing Spreads on 3-Month SOFR Futures: Resting Order Eliminations |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | TAG 762-SECURITYSUBTYPE | TAG 969 - MINPRICEINCREMENT | MDP 3.0 CHANNEL |
| †3-Month SOFR Strip Spread | SR3 | SS | †SB (Balanced Strip Spread) | 0.100000000 | 312 |

These spreads will be available for customer testing in New Release on **Monday, August 1.**

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### New New - Euro-Denominated Crypto Futures - August 28

Effective **Sunday, August 28** (trade date Monday, August 29), pending completion of all regulatory review periods, Bitcoin Euro and Ether Euro futures will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

| **Euro-Denominated Crypto Futures** |
| --- |
| **Product** | **MDP 3.0: tag 6937-Asset** | **iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group** | **Market Data Channel** |
| Bitcoin Euro futures | BTE | GB | 326 |
| Ether Euro futures | ETE | OE | 326 |

These futures will be available for customer testing in New Release on **Monday, August 15.**

These contracts are listed with, and subject to, the rules and regulations of CME.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### New New - Energy Gasoil Crack Spreads - September 18

Effective **Sunday, September 18** (trade date Monday, September 19), new exchange defined Energy Gasoil Crack spreads will be made available for trading on CME Globex. The new spreads will use a new strategy type (TB) and trade at a reduced tick.

The TB spread is an inter-commodity ratio futures spread allowing the simultaneous purchase (sale) of a distilled product (i.e., Low Sulphur Gasoil) with a corresponding sale (purchase) of the raw product from which it was produced (i.e., Crude Oil).

To support the launch of the Gasoil Crack spreads on**August 28**, tag 6937-Asset for European Low Sulphur Gasoil (100mt) Bullet futures will change from [GLI to 7F](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html?#pccelsgbf).

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Energy+Gasoil+Crack+Spreads+on+CME+Globex) for additional details.

These changes will be available for customer testing in New Release on **Monday, August 8**.

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Event Contracts- September 18

Effective **Sunday,September 18**(trade date Monday, September 19), [event options contracts](https://www.cmegroup.com/markets/event-based-contracts.html)will be listed for trading on CME Globex, pending completion of all regulatory review periods. Event contracts are daily-expiring, cash settled, European Style, options on futures contracts. Event contracts will provide access to some of our most recognized global products, including metals, energy, equities, and foreign currencies.Additionally, non-tradable underlying futures will be listed to support the new event options. Event contracts will be listed on a new MDP 3.0 channel (329 - Event Contracts).

Please review the[Client Impact Assessment](https://www.cmegroup.com/confluence/display/EPICSANDBOX/Event-Based+Contracts)for additional details.

The event contracts are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CME, CBOT, COMEX, and NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Bursa Malaysia Derivatives (BMD) Crude Palm Oil vs East Malaysia Crude Palm Oil Inter-Commodity Futures Spreads- October 2

Effective **Sunday,October 2**(trade date Monday, October 3),and pending final regulatory approval, inter-commodity spreads between Bursa Malaysia Derivatives (BMD)’s Crude Palm Oil vs BMD East Malaysia Crude Palm Oil futures will be made available for trading on CME Globex.

| BURSA MALAYSIA DERIVATIVES (BMD) CRUDE PALM OIL VS EAST MALAYSIA CRUDE PALM OIL INTER-COMMODITY FUTURES SPREADS |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | TAG 762-SECURITYSUBTYPE | Market Data Channel |
| Crude Palm Oil vs East Malaysia Crude Palm Oil Futures | FCPO | BC | IS | 430 |

This change is currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of BMD.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### 30-Year Uniform Mortgage-Backed Security (UMBS) To-Be-Announced (TBA) Futures- October 2

Effective **Sunday, October 2** (trade date Monday, October 3), pending completion of all regulatory review periods, 30-Year Uniform Mortgage-Backed Security (UMBS) To-Be-Announced (TBA) futures will be listed for trading on CME Globex and for submission for clearing via CME ClearPort.

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

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

## Product Changes

### Change to Price Format for Dow Jones Real Estate Futures: Resting Order Eliminations- This Week

Effective this**Sunday, August 7**(trade date Monday, August 8), the price format for Dow Jones Real Estate futures will be changed as follows:

Please Note:To facilitate this change, customers will be asked to cancel all Good ‘Till Cancel (GTC) and Good ‘Till Date (GTD) orders for these contracts, by the close on Friday, August 5. After 16:00 CT on Friday, August 5, any remaining GT orders on these markets will be removed by the CME Global Command Center (GCC).

| **Change to Price Format for Dow Jones Real Estate Futures** |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | CURRENT TAG 9787-DISPLAYFACTOR | NEW TAG 9787-DISPLAYFACTOR | CURRENT **TAG 969 - MINPRICEINCREMENT** | NEW **TAG 969 - MINPRICEINCREMENT** |
| Dow Jones Real Estate Futures | RX | RX | 0.100000000 | 0.010000000 | 1 | 10 |

This change is currently available in New Release for customer testing.

These contracts are listed with, and subject to, the rules and regulations of CBOT.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Changes to Silver and Copper Weekly Monday and Wednesday Options: Resting Order Eliminations- This Week

Effective this**Sunday, August 7**(trade date Monday, August 8), pending regulatory approval, the match algorithm for silver and copper weekly Monday and Wednesday options will be amended as follows:

Please Note:To facilitate this change, customers will be asked to cancel all Good ‘Till Cancel (GTC) and Good ‘Till Date (GTD) orders for these contracts, by the close on Friday, August 5. After 16:00 CT on Friday, August 5, any remaining GT orders on these markets will be removed by the CME Global Command Center (GCC).

| **Changes Silver and Copper Weekly Monday and Wednesday Options: Resting Order Eliminations** |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | CURRENT TAG 1142-MATCHALGORITHM | NEW TAG 1142-MATCHALGORITHM |
| Silver Weekly Monday Option | M1S - M5S | SO (UDS: S1) | K-Split FIFO and C-Pro Rata | F-FIFO |
| Copper Weekly Monday Option | H1M - H5M | 1U (UDS: 2U) |
| Silver Weekly Wednesday Option | W1S-W5S | SO (UDS: S1) |
| Copper Weekly Wednesday Option | H1W - H5W | 1U (UDS: 2U) |

These changes are currently available for customer testing in New Release.

These contracts are listed with, and subject to, the rules and regulations of CBOT.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Change to Strike Price Listing for Options on Equity Index Futures- August 21

Effective **Sunday, August 21** (trade date Monday, August 22), the strike price listing rule will be changed for multiple options on Equity Futures on CME Globex and for submission for clearing via CME ClearPort.

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

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### New New - Temporary Suspension for Trading of Japan C+F Naphtha Crack Spread Futures - August 21

On Friday, July 29, the following contract months were temporarily suspended from trading and clearing until **Sunday, August 21** (trade date Monday, August 22), Japan C&F Naphtha (Platts) Brent Crack Spread futures and Japan C&F Naphtha Dubai (Platts) Crack Spread futures as follows:

| **TEMPORARY SUSPENSION OF Japan C+F Naphtha spread FUTURES** |
| --- |
| **PRODUCT** | **MDP 3.0: TAG 6937-ASSET** | **ILINK: TAG 55-SYMBOL MDP 3.0 TAG 1151 - SECURITY GROUP** | **Suspension of Contract months** |
| Japan C&F Naphtha (Platts) Brent Crack Spread Futures | AJB | RF | January 2023 contract months and beyond |
| Japan C&F Naphtha Dubai (Platts) Crack Spread Futures | JNC | PT | all contract months |

Effective**Sunday, August 21**(trade date Monday, August 22), pending all relevant CFTC regulatory review periods, the Japan C&F Naphtha (Platts) Brent Crack Spread futures and Japan C&F Naphtha Dubai (Platts) Crack Spread futures will resume trading on CME Globex and for clearing via CME ClearPort with the following changes:

*   The settlement conversion factor will be changed from 9 barrels per metric ton to 8.9 barrels per metric ton

The conversion factor change will be applied to contract months starting with the January 2023 and beyond for the Japan C&F Naphtha (Platts) Brent Crack Spread futures contracts. The conversion factor amendment will be applied to all contract months for the Japan C&F Naphtha Dubai (Platts) Crack Spread futures contract.

The suspended contract months have no open interest.

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### New New - CME Globex Product Code Change to European Low Sulphur Gasoil (100mt) Bullet Futures – Resting Order Eliminations - August 28

Effective**Sunday, August 28**(trade date Monday, August 29), for European Low Sulphur Gasoil (100mt) Bullet futures will be changed as follows.

**Please Note**: To facilitate this change, customers are asked to cancel all Good ‘Till Cancel (GTC) and Good ‘Till Date (GTD) orders after the close on **August 26**. After 16:00 CT on August 26, all remaining GT orders for these futures and future spreads will be cancelled or deleted by the CME Global Command Center (GCC).

| **CHANGES TO European Low Sulphur Gasoil (100mt) Bullet Futures** |
| --- |
| **PRODUCT** | **CUIRRENT MDP 3.0: TAG 6937-ASSET** | **NEW MDP 3.0: TAG 6937-ASSET** | **MDP 3.0 TAG 1151 - SECURITY GROUP** |
| European Low Sulphur Gasoil (100mt) Bullet Futures | GLI | 7F | OP |

This change will be made available for customer testing in New Release on **Monday, August 8**.

These contracts are listed with, and subject to, the rules and regulations of NYMEX.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

### Changes to Bursa Malaysia Derivatives (BMD) Gold Futures- September 18

Effective**Sunday, September 18**(trade date Monday, September 19), and pending final regulatory approval, the Bursa Malaysia Derivatives (BMD) Gold futures security definition (tag 35-MsgType=d) message will be amended as follows:

*   Change to tag 996-UnitOfMeasure
*   Change to tag 1147-UnitOfMeasureQty
*   Change to tag 969-MinPriceIncrement
*   Afternoon Trading Session Hours

| Changes to Bursa Malaysia Derivatives (BMD) Gold Futures |
| --- |
| Product | MDP 3.0: tag 6937-Asset | iLink: tag 55-Symbol MDP 3.0 tag 1151 - Security Group | CURRENT Tag 996-Unitofmeasure | NEW Tag 996-Unitofmeasure | CURRENT Tag 1147-UnitofmeasureQty | NEW Tag 1147-UnitofmeasureQty | CURRENT Tag 969-Minpriceincrement | NEW Tag 969-Minpriceincrement |
| Bursa Malaysia Derivatives Gold Futures | FGLD | BG | GRAMS | TRYOZ | 100 | 40 | .05 | .10 |

| **New Afternoon Trading Session** |
| --- |
|  | **Current** **Monday - Friday Afternoon Trading Session** | **New** **Monday – Friday Afternoon Trading Session** |
| Afternoon Trading Session Hours | 1430 hours – 1830 hours (Malaysia time) | 1430 hours – 1730 hours (Malaysia time) |

This change will be made available for customer testing in New Release on **Monday, August 1**.

These contracts are listed with, and subject to, the rules and regulations of BMD.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)

## Events and Announcements

### CME Group DR Datacenter Migration and Test

CME Group is pleased to announce the move and upgrade of our backup datacenter as part of our commitment to the protection of our customers. Last year, we completed the migration of our Disaster Recovery clearing systems, and we are now focused on CME Globex and supporting systems. To ensure customer can connect to our new backup datacenter, CME Group will be holding mock disaster recovery testing on **Saturday, September 10, at 9 a.m. Eastern Time (ET)**.

**Please Note:**Customers do not need to test from Disaster Recovery – please plan to stay in your production environment.

Customers must [register](https://www.cmegroup.com/events/2022/dr-testing-for-futures-and-options-markets.html) in advance to participate. Please review the [mock trading script](https://www.cmegroup.com/content/dam/cmegroup/notices/electronic-trading/2022/06/coresitedrmock.pdf) for additional details.

[Back to Top](https://www.cmegroup.com/notices/electronic-trading/2022/08/20220801.html#top)
