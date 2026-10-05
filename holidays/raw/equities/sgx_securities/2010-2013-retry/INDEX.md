# sgx_securities 2010-2013 retry (2026-09-30 UTC)

The Wave-D re-check of the 2010-2013 capture gap. The issue's premise "the
marketplace-portal predecessor page was never captured" is corrected: the
`wps/wcm/connect/mp_en/site/trading_on_sgx/securities_market/` family WAS
captured — in May 2009 only. Replays retrieved here:

| capture | page | prints |
|---|---|---|
| 20090514003600 | `securities_trading_hours_and_calendar/2009+public+holidays` | the 2009 Public Holidays table (11 dates; footer "Mar 26, 2008") |
| 20090522132802 | `securities_trading_hours_and_calendar/Securities+Trading+Calendar?` | the trading-sessions grid (9.00am-12.30pm / 2.00pm-5.00pm, Pre-Open 8.30-9.00, Pre-Close 5.00-5.06) and links to only the 2008 and 2009 holiday tables |
| 20090523091800 | `securities_trading_hours_and_calendar/2008+publicholidays` | the 2008 Public Holidays table (11 dates) |

No capture of the family exists after May 2009 (CDX prefix sweep 2026-09-30
UTC), the `wps/portal/sgxweb` securities page's first capture is 2014-08-21,
and a 3 000-urlkey domain-wide sweep of sgx.com 2010-2013 holds no securities
trading-schedule page or annual "Trading Hours, Trading Days and Holidays"
circular. `marketplace.sgx.com` has zero captures 2009-2014. So
2010-01-01..2013-12-31 survives in no operator artifact: the negative stands,
with the record sharpened.
