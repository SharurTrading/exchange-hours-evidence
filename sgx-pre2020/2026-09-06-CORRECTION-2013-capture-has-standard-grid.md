# Correction to 2026-09-06-grids-portal-hours-page.json, dead-end 3

That file says the 2013-08-20 portal capture (WB-20130820090335-portal-trading_hours_calendar.html)
"does not carry the standard grid — at that date the page held a holiday trading schedule". WRONG.
The page holds seven per-holiday tables AND, below them, the normal "Trading Hours* for SGX
Derivatives Market" table (Contract Code | T Session | T+1 Session) with, e.g.,
"SGX FTSE China A50 Index Futures | 9.00am to 3.55pm | 4.40pm to 2.00am" and a Notes block stating
the routine conventions. Verified by two refuters and by the orchestrator from the raw bytes
2026-09-06. The contract-sets JSON has it right. A reader who opens the portal-hours JSON first must
not abandon the three carried floor eras on the strength of that sentence.
