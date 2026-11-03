Title: 24-7 Technical Market Functionality - CME Group Client Systems Wiki

URL Source: https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality

Markdown Content:
This topic describes 24/7 technical market functionality for listed derivatives weekend trading at CME Group.

*       *   1.1[CME Globex Maintenance Windows and Market Hours](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#CME-Globex-Maintenance-Windows-and-Market-Hours)
        *   1.1.1[Example 24/7 Futures and Options Schedule](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Example-24%2F7-Futures-and-Options-Schedule)
        *   1.1.2[Saturday Maintenance Window Processing Overview](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Saturday-Maintenance-Window-Processing-Overview)
            *   1.1.2.1[Saturday Shutdown and Startup](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Saturday-Shutdown-and-Startup)
                *   1.1.2.1.1[Shutdown](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Shutdown)
                *   1.1.2.1.2[Startup](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Startup)

    *   1.2[24/7 Maintenance and Trading Schedule Examples](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#24%2F7-Maintenance-and-Trading-Schedule-Examples)
        *   1.2.1[Example 1 - Typical Maintenance and Trading Schedule](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Example-1---Typical-Maintenance-and-Trading-Schedule)
        *   1.2.2[Example 2 - Monday Holiday Trading Schedule](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Example-2---Monday-Holiday-Trading-Schedule)
        *   1.2.3[Example 3 - Friday Holiday Trading Schedule](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Example-3---Friday-Holiday-Trading-Schedule)

*   2[24/7 Supported Functionality](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#24%2F7-Supported-Functionality)
    *   2.1[iLink Order Entry](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#iLink-Order-Entry)
        *   2.1.1[Market Segment Gateway (MSGW)](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Market-Segment-Gateway-(MSGW))
        *   2.1.2[Convenience Gateway (CGW)](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Convenience-Gateway-(CGW))
        *   2.1.3[iLink Session Support Summary](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#iLink-Session-Support-Summary)
        *   2.1.4[Order Entry Service Gateway](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Order-Entry-Service-Gateway)
        *   2.1.5[Good Till (GT) Order Elimination](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Good-Till-(GT)-Order-Elimination)
        *   2.1.6[Credit and Risk Management](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Credit-and-Risk-Management)

    *   2.2[Drop Copy](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Drop-Copy)
        *   2.2.1[Drop Copy MSGW Session](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Drop-Copy-MSGW-Session)
        *   2.2.2[Drop Copy CGW Session](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Drop-Copy-CGW-Session)
        *   2.2.3[Drop Copy Target Session Support Summary](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Drop-Copy-Target-Session-Support-Summary)

    *   2.3[Straight Through Processing](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Straight-Through-Processing)
    *   2.4[Reference Data API](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Reference-Data-API)
        *   2.4.1[Seven Day Trading Indicator](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#Seven-Day-Trading-Indicator)

    *   2.5[CME ClearPort](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#CME-ClearPort)
    *   2.6[CME Direct](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#CME-Direct)
    *   2.7[CME DataMine](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#CME-DataMine)
    *   2.8[FirmSoft](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1553563649/24-7+Technical+Market+Functionality#FirmSoft)

## CME Globex Maintenance Windows and Market Hours

This section outlines the Globex 24/7 maintenance schedule for listed derivatives. Maintenance windows can vary by product and are subject to change; all updates will be communicated via the[Globex Notice](https://www.cmegroup.com/notices.html "https://www.cmegroup.com/notices.html").

### **Example 24/7 Futures and Options****Schedule**

| **Day** | **Type** | **Close/Pause** | **Pre-Open/Open** |
| --- | --- | --- | --- |

| **Day** | **Type** | **Close/Pause** | **Pre-Open/Open** |
| --- | --- | --- | --- |
| Saturday | Extended Maintenance Window | C _lose:_ 2:00 a.m. to 3:45 a.m. CT | * _Pre-open_: 3:45 a.m. to 4:00 a.m. CT * _No cancel_: 3:59:30 a.m. to 4:00:00 a.m. CT * _Open_: 4:00 a.m. CT |
| Monday through Friday | Daily Maintenance Window (with Trade Date roll) | _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT | * _Pre-open:_ 4:01:00 p.m. to 4:01:30 p.m. CT * _No cancel_: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open:_ 4:02:00 p.m. CT |

### Saturday Maintenance Window Processing Overview

The following section outlines Saturday maintenance processing for 24/7 trading.

#### Saturday Shutdown and Startup

##### Shutdown

The following occurs during shutdown:

1.   At the beginning of the maintenance period, client systems receive a [MDP 3.0 - Security Status](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457223126 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457223126").

2.   CME Globex sends the iLink messages for [iLink Execution Report - Elimination](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/716177614 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/716177614") orders.

3.   Client systems experience MDP multicast, TCP iLink, and Drop Copy disconnections. At this point, CME Group recommends that clients and vendors restart their applications and go through their own restart processes to reset their order books.

##### **Startup**

iLink order entry, Drop Copy and market data sequence numbers reset to 1 during the [Saturday startup cycle](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1160019972 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/1160019972"). Client systems re-establish connectivity to the MDP multicast groups and receive the following startup messaging:

1.   The [MDP 3.0 - Market Data Snapshot](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457574196 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457574196") (tag 35-MsgType=W) messages on the Market Recovery feed are deleted for the impacted 24/7 channel. Tag 83-RptSeq for Market by Price (MBP) book updates resets to 1 for each instrument repeating group.

2.   CME Globex disseminates incremental real-time market data for that channel and client systems can process the data. An [MDP 3.0 - Market Data Incremental Refresh](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457226984 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457226984") (tag 35-MsgType=X) message is sent with an empty End of Event indicator if no other information is available. If session statistics are available, they are republished via the normal Incremental Refresh messaging:

    1.   Current session trade volume

    2.   Price levels in the order books

    3.   Highest and lowest trade

3.   [MDP 3.0 - Security Status](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457223126 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457223126") messages containing market states (per instrument group) are sent for the 24/7 channel. Then any instrument states that are different from the instrument group state are sent (e.g., Forbidden/Halted instruments).

Pre-registered administrative information will be removed during the Saturday maintenance window. Clients must re-submit their [iLink Party Details Definition Request](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/715587786 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/715587786") following the pre-open on Saturday.

## 24/7 Maintenance and Trading Schedule Examples

This section provides examples for 24/7 trading.

### Example 1 - Typical Maintenance and Trading Schedule

The following is a maintenance and trading s chedule example for swap-based event contracts. CME Globex communicates the instrument’s open and close messages via the [MDP 3.0 - Security Status](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457223126 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457223126") (35=f).

| **Day** | **Schedule** | **Type** | **Trade Date** | **Notes** |
| --- | --- | --- | --- | --- |

| **Day** | **Schedule** | **Type** | **Trade Date** | **Notes** |
| --- | --- | --- | --- | --- |
| Friday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Monday trade date after open |  |
| Saturday | * _Close_: 2:00 a.m. to 3:45 a.m. CT * _Pre-open_: 3:45 am to 4:00 a.m. CT * _Open_: 4:00 a.m. CT | _Extended maintenance_ | Monday trade date | Sequence numbers are reset. |
| Sunday | Trading session continues | Monday trade date |  |
| Monday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open: 4:02:00 p.m. CT_ | Daily maintenance | Tuesday trade date after open |  |
| Tuesday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open: 4:02:00 p.m. CT_ | Daily maintenance | Wednesday trade date after open |  |
| Wednesday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open: 4:02:00 p.m. CT_ | Daily maintenance | Thursday trade date after open |  |
| Thursday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * Pre-open: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open: 4:02:00 p.m. CT_ | Daily maintenance | Friday trade date after open |  |

### Example 2 - Monday Holiday Trading Schedule

In the below example, Monday is a holiday. Therefore, there is no Monday daily maintenance, and the trade date is Tuesday.

| **Day** | **Schedule** | **Type** | **Trade Date** | **Notes** |
| --- | --- | --- | --- | --- |

| **Day** | **Schedule** | **Type** | **Trade Date** | **Notes** |
| --- | --- | --- | --- | --- |
| Friday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Tuesday trade date after open |  |
| Saturday | * _Close_: 2:00 a.m. to 3:45 a.m. CT * _Pre-open_: 3:46 am to 4:00 a.m. CT * _Open_: 4:00 a.m. CT | _Extended maintenance_ | Tuesday trade date | Sequence numbers are reset. |
| Sunday | Trading session continues | Tuesday trade date |  |
| Monday | **Holiday** - trading session continues * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Tuesday trade date | During the Monday holiday, the market does not close and the trade date does not change. |
| Tuesday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Wednesday trade date after open |  |
| Wednesday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Thursday trade date after open |  |
| Thursday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Friday trade date after open |  |

### Example 3 - Friday Holiday Trading Schedule

In the below example, Friday is a holiday. Therefore, the trade date after the Thursday maintenance is Monday. GT orders that [only support 5-day trading](https://www.cmegroup.com/clearing/files/cryptocurrency-guidelines.pdf "https://www.cmegroup.com/clearing/files/cryptocurrency-guidelines.pdf") will be eliminated Friday at 4:00 p.m. CT. Standard weekday credit limits apply to all Friday trades before 4:00 p.m. CT.

| **Day** | **Schedule** | **Type** | **Trade Date** | **Notes** |
| --- | --- | --- | --- | --- |

| **Day** | **Schedule** | **Type** | **Trade Date** | **Notes** |
| --- | --- | --- | --- | --- |
| Wednesday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Thursday trade date after open |  |
| Thursday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | _Monday_ trade date after open |  |
| Friday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | _Holiday maintenance_ | Monday trade date after open | Due to the Friday holiday, GT orders that [only support 5-day trading](https://www.cmegroup.com/clearing/files/cryptocurrency-guidelines.pdf "https://www.cmegroup.com/clearing/files/cryptocurrency-guidelines.pdf") will be eliminated Friday at 4:00 p.m. CT. Standard weekday credit limits apply to all Friday trades before 4:00 p.m. CT. |
| Saturday | * _Close_: 2:00 a.m. to 3:45 a.m. CT * _Pre-open_: 3:46 am to 4:00 a.m. CT * _Open_: 4:00 a.m. CT | _Extended maintenance_ | Monday trade date | Sequence numbers are reset. |
| Sunday | Trading session continues | Monday trade date |  |
| Monday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Tuesday trade date after open |  |
| Tuesday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Wednesday trade date after open |  |
| Wednesday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Thursday trade date after open |  |
| Thursday | * _Close_: 4:00:00 p.m. to 4:01:00 p.m. CT * _Pre-open_: 4:01:00 p.m. CT to 4:01:30 p.m. CT * No-cancel: 4:01:30 p.m. to 4:02:00 p.m. CT * _Open_: 4:02:00 p.m. CT | Daily maintenance | Friday trade date after open |  |

## 24/7 Supported Functionality

This section outlines supported functionality for 24/7 trading.

## iLink Order Entry

At the beginning of the Saturday extended maintenance window, CME Globex disconnects all clients' sessions, resets sequence numbers, and cancels resting day orders and mass quotes. Pre-registered administrative information will be removed during the Saturday maintenance window. Clients must re-submit their [Party Details Definition](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/714211378/iLink+Binary+Order+Entry+-+Business+Layer#Party-Details-Definition-Messaging "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/714211378/iLink+Binary+Order+Entry+-+Business+Layer#Party-Details-Definition-Messaging") following the pre-open on Saturday.

### Market Segment Gateway (MSGW)

All existing iLink Order Entry functionality is supported. Client systems may leverage existing iLink MSGW sessions.

### Convenience Gateway (CGW)

iLink CGW sessions support 7-day markets.

Clients must have a 7-day-enabled CGW iLink session to support 24/7:

*   7-day CGW sessions will support all Globex futures and options markets, including 24/7 markets.

*   5-day CGW sessions can only submit futures and options orders during the weekday.

### iLink Session Support Summary

| **Session Summary** | **Impact** |
| --- | --- |

| **Session Summary** | **Impact** |
| --- | --- |
| MSGW Session | All MSGW sessions can send orders 24/7 on CME Globex. |
| 5-Day CGW Session | 5-day CGW sessions can only send orders between Sunday 4:05 p.m. and Friday 4:00 p.m. CT. |
| 7-Day CGW Session | 7-day CGW sessions can send orders 24/7 on CME Globex. |

### Order Entry Service Gateway

This section outlines OESGW network IP impacts for MSGW and CGW sessions.

| **Session Type** | **Market Segment OESGW** | **Future IPs** |
| --- | --- | --- |

| **Session Type** | **Market Segment OESGW** | **Future IPs** |
| --- | --- | --- |
| 7-Day MSGW | marketsegment id="4" | More details on the SFTP site is available on[MSGW - SFTP Configuration](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457220437 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457220437"). |
| 7-Day CGW | marketsegment id="2" | View the [Configuration and Connectivity](https://www.cmegroup.com/solutions/market-access/globex/globex-resources.html#sdidcsc "https://www.cmegroup.com/solutions/market-access/globex/globex-resources.html#sdidcsc") (IP and port) details (CME Group Login required). The configuration file will be updated at a later date. |

### Good Till (GT) Order Elimination

If weekend trading is not enabled in CME Globex Credit Controls (GC2), all Good Till (GT) orders will be eliminated at Friday 4:00 p.m. CT. Client systems that do not enable weekend trading are encouraged to cancel all futures and options GT orders before Friday 4:00 p.m. CT.

### Credit and Risk Management

CME Globex Credit Controls (GC2) will support unique GC2 [weekend Limits](https://www.cmegroup.com/tools-information/webhelp/globex-credit-controls/Content/CME-Globex-Credit-Controls-Management.html#weekend "https://www.cmegroup.com/tools-information/webhelp/globex-credit-controls/Content/CME-Globex-Credit-Controls-Management.html#weekend"). Client specified limits may affect weekend GT order cancellation.

For more information see the [CME Clearing & Global Operations Summary of Requirements and Guidelines for 24x7 Clearing](https://www.cmegroup.com/clearing/files/cryptocurrency-guidelines.pdf "https://www.cmegroup.com/clearing/files/cryptocurrency-guidelines.pdf").

## Drop Copy

All existing [Drop Copy 4.0 Service for iLink](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/665190402 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/665190402") functionality is supported. At the beginning of the Saturday extended maintenance window, CME Globex will disconnect all clients' sessions and reset sequence numbers.

### Drop Copy MSGW Session

All Drop Copy MSGW sessions support 24/7 trading.

### Drop Copy CGW Session

Clients must have a 7-day-enabled CGW Drop Copy session to support 24/7:

*   7-day CGW target sessions will support all futures and options markets 24/7 on Globex.

*   5-day CGW target sessions will only be active during the weekday.

5-Day CGW target sessions are not available for connectivity until 14:00 CT on Sundays.

### Drop Copy Target Session Support Summary

| **Session Summary** | **Impact** |
| --- | --- |

| **Session Summary** | **Impact** |
| --- | --- |
| 7-Day CGW target sessions | 7 day CGW target sessions can receive real-time copies of iLink Execution Report and Acknowledgement [From CME Globex to Client System](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457607329 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457607329") of 24/7 activity on CME Globex. |

## Straight Through Processing

[CME Straight Through Processing](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457412452 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457412452") supports trade capture reports for the 24/7 markets.

## Reference Data API

[CME Reference Data API Version 3](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457215780 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457215780") supports 24/7 trading including [CME Reference Data API - CME Globex Trading Hours and Holiday Schedules](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457217339 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457217339") functionality.

An attribute will be added to CME Reference Data API to support 24/7 trading. Clients can use the sevenDayTradingIndicator to identify only 24/7 instruments.

### Seven Day Trading Indicator

| **Endpoint** | **Attribute Name** | **Description** | **Type** | **Filterable** |
| --- | --- | --- | --- | --- |

| **Endpoint** | **Attribute Name** | **Description** | **Type** | **Filterable** |
| --- | --- | --- | --- | --- |
| Instrument | sevenDayTradingIndicator | A yes/no (Y/N) flag that indicates if an instrument is available for 24/7 trading. | String | ![Image 1: image-20260428-165114.png](https://media-cdn.atlassian.com/file/fdaf76c2-33eb-4263-be56-7d482ab36acf/image/cdn?allowAnimated=true&client=5be37d23-060f-47f3-87b1-1790d81c4b5a&collection=contentId-1553563649&height=125&max-age=2592000&mode=full-fit&source=mediaCard&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1YmUzN2QyMy0wNjBmLTQ3ZjMtODdiMS0xNzkwZDgxYzRiNWEiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpjb2xsZWN0aW9uOmNvbnRlbnRJZC0xNTUzNTYzNjQ5IjpbInJlYWQiXX0sImV4cCI6MTc5MzY2NDI0OCwibmJmIjoxNzkzNjYxMzY4LCJodHRwczovL2lkLmF0bGFzc2lhbi5jb20vYXBwQWNjcmVkaXRlZCI6ZmFsc2UsImF1dGhUeXBlIjoidW5hdXRoZW50aWNhdGVkIn0.Xuo7cGsClMhZHT03h0hRDAQzsP8jK8lOM_pE5xmH4cY&width=32#media-blob-url=true&id=fdaf76c2-33eb-4263-be56-7d482ab36acf&clientId=5be37d23-060f-47f3-87b1-1790d81c4b5a&contextId=contentId-1553563649&collection=contentId-1553563649) |

## CME ClearPort

The [CME ClearPort](https://www.cmegroup.com/clearport.html "https://www.cmegroup.com/clearport.html") web-based user interface will support 24/7 trading.

## CME Direct

[CME Direct](https://www.cmegroup.com/solutions/market-access/cme-direct.html "https://www.cmegroup.com/solutions/market-access/cme-direct.html") does not support weekend trading.

## CME DataMine

[CME DataMine](https://www.cmegroup.com/datamine.html "https://www.cmegroup.com/datamine.html") supports futures and options and 24/7 trading.

## FirmSoft

The following table outlines FirmSoft availability.

| **Feature** | **Weekdays** | **Weekends** |
| --- | --- | --- |

| **Feature** | **Weekdays** | **Weekends** |
| --- | --- | --- |
| [FirmSoft](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457216730 "https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457216730") - [Orders](https://www.cmegroup.com/tools-information/webhelp/cmeone-firmsoft/Content/OrdersCard.html "https://www.cmegroup.com/tools-information/webhelp/cmeone-firmsoft/Content/OrdersCard.html") and [Trades](https://www.cmegroup.com/tools-information/webhelp/cmeone-firmsoft/Content/FillsCard.html "https://www.cmegroup.com/tools-information/webhelp/cmeone-firmsoft/Content/FillsCard.html")View | ![Image 2: Check Mark](https://pf-reactions-service.prod-east.frontend.public.atl-paas.net/assets/atlassian/productivityEmojis/check-32px.png) Accessible at: [one.cmegroup.com](https://one.cmegroup.com/login "https://one.cmegroup.com/login") | ![Image 3: Check Mark](https://pf-reactions-service.prod-east.frontend.public.atl-paas.net/assets/atlassian/productivityEmojis/check-32px.png) Accessible at:[https://firmsoftweekend.prod.cmegroup.com/](https://firmsoftweekend.prod.cmegroup.com/ "https://firmsoftweekend.prod.cmegroup.com/") |
