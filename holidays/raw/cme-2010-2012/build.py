# -*- coding: utf-8 -*-
import json, os

CAP = {
 "2010-new-years":("20100215051652","12/21/2009"),
 "2010-martin-luther-king":("20100331064226","12/21/2009"),
 "2010-presidents-day":("20100215064641","2/3/2010"),
 "2010-good-friday":("20100601111916","4/5/2010"),
 "2010-memorial-day":("20100601094225","5/21/2010"),
 "2010-4th-of-july":("20100602005637","6/1/2010"),
 "2010-labor-day":("20100602005641","3/5/2010"),
 "2010-columbus-day":("20100821133122","6/9/2010"),
 "2010-veterans-day":("20101122094019","10/29/2010"),
 "2010-thanksgiving":("20101122094012","11/19/2010"),
 "2010-christmas":("20101214061238","12/13/2010"),
 "2011-new-years":("20111101143945","12/30/2010"),
 "2011-martin-luther-king":("20111028023429","12/23/2010"),
 "2011-presidents-day":("20111028023516","2/16/2011"),
 "2011-good-friday":("20111028023707","4/21/2011"),
 "2011-memorial-day":("20130930105652","5/24/2011"),
 "2011-4th-of-july":("20111101144054","6/22/2011"),
 "2011-labor-day":("20111101144345","8/31/2011"),
 "2011-columbus-day":("20111101143916","10/3/2011"),
 "2011-veterans-day":("20111111191211","10/18/2011"),
 "2011-thanksgiving":("20111124185246","11/23/2011"),
 "2011-christmas":("20120125020548","12/14/2011"),
 "2012-new-years":("20120125025430","12/5/2011"),
 "2012-martin-luther-king":("20120505161526","1/4/2012"),
 "2012-presidents-day":("20120505161539","2/13/2012"),
 "2012-good-friday":("20120417004247","4/2/2012"),
 "2012-memorial-day":("20120915003714","5/23/2012"),
 "2012-4th-of-july":("20120915003923","6/22/2012"),
 "2012-labor-day":("20120915003437","8/27/2012"),
 "2012-columbus-day":("20120915001514","8/15/2012"),
 "2012-veterans-day":("20120915001444","8/15/2012"),
 "2012-thanksgiving":("20130127223901","10/17/2012"),
 "2012-christmas":("20130414194027","11/14/2012"),
 "2013-new-years":("20120915003225",None),
}
def doc(stem):
    ts,upd = CAP[stem]
    url = "http://www.cmegroup.com/tools-information/holiday-calendar/files/%s.pdf" % stem
    cap = "%s-%s-%sT%s:%s:%sZ" % (ts[0:4],ts[4:6],ts[6:8],ts[8:10],ts[10:12],ts[12:14])
    s = "%s | wayback id_ replay capture %s | raw/cme-2010-2012/docs/%s.pdf" % (url, cap, stem)
    if upd: s += " | CME footer: Last updated %s" % upd
    return s

HOL=[]
def H(date,name,fams):
    HOL.append({"date":date,"name":name,"families":fams})
def F(fam,status,verbatim,stem,close=None,open_=None):
    d={"family":fam,"status":status,"verbatim":verbatim,"document":doc(stem),"tier":"T1"}
    if close: d["close_instant"]=close
    if open_: d["open_instant"]=open_
    return d

# ---------------- 2010 ----------------
s="2010-new-years"
H("2010-01-01","New Year's Day 2010 (Friday)",[
 F("equity_index","closed","CME Group Equity Products / Friday, Jan 1 / “CME Globex is closed”; Sunday, Jan 3 “1700 CT – Regular CME Globex open for trade date Monday, Jan 4”",s,open_="1700 CT (Sun Jan 3, for trade date Mon Jan 4)"),
 F("interest_rates","closed","CME Group Interest Rate Products / Friday, Jan 1 / “CME Globex is closed”; Sunday, Jan 3 “1700 CT – Regular CME Globex open for CME interest rate products for trade date Monday, Jan 4” … “1730 CT – Regular CME Globex open for CBOT financial products for trade date Monday, Jan 4”",s,open_="1700 CT CME interest rate / 1730 CT CBOT financial (Sun Jan 3)"),
 F("fx","closed","CME Group FX Products / Friday, Jan 1 / “CME Globex is closed”; Sunday, Jan 3 “1700 CT – Regular CME Globex open for trade date Monday, Jan 4”",s,open_="1700 CT (Sun Jan 3)"),
 F("energy","closed","NYMEX & COMEX® Products on CME Globex / Friday, Jan 1 / “CME Globex is closed”; Sunday, Jan 3 “1700 CT / 1800 ET – Regular CME Globex open for trade date Monday, Jan 4”",s,open_="1700 CT / 1800 ET (Sun Jan 3)"),
 F("metals","closed","NYMEX & COMEX® Products on CME Globex / Friday, Jan 1 / “CME Globex is closed” (COMEX shares the NYMEX line); Sunday, Jan 3 “1700 CT / 1800 ET – Regular CME Globex open for trade date Monday, Jan 4”",s,open_="1700 CT / 1800 ET (Sun Jan 3)"),
 F("grains","closed","Other CME Group Products on CME Globex / Friday, Jan 1 / “CME Globex is closed”; Sunday, Jan 3 “1800 CT – Regular CME Globex open for CBOT Grains for trade date Monday, Jan 4”",s,open_="1800 CT (Sun Jan 3)"),
 F("livestock","closed","Other CME Group Products on CME Globex / Friday, Jan 1 / “CME Globex is closed”; Sunday, Jan 3 “Exceptions: CME Livestock, TRAKRS and ETFs will remain closed until their regularly scheduled open on Monday”",s,open_="regularly scheduled open on Monday Jan 4"),
])
H("2009-12-31","New Year's 2010 — preceding trade date (Thursday, below the January-2010 floor; recorded for completeness)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Thursday, Dec 31”",s,close="1515 CT"),
 F("interest_rates","normal","“1600 CT – Regular CME Globex close for all CME interest rate and CBOT financial products for trade date Thursday, Dec 31”",s,close="1600 CT"),
 F("fx","normal","“1600 CT – Regular CME Globex close for trade date Thursday, Dec 31”",s,close="1600 CT"),
 F("energy","normal","“1615 CT / 1715 ET – Regular CME Globex close for trade date Thursday, Dec 31”; “Exceptions: NYMEX Brent TAS (BZT, BBT) will close at 1200 CT / 1300 ET”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","“1615 CT / 1715 ET – Regular CME Globex close for trade date Thursday, Dec 31”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / Thursday, Dec 31 / “Regular Close – Per each Product Schedule for trade date Thursday, Dec 31”",s),
 F("livestock","normal","Other CME Group Products / Thursday, Dec 31 / “Regular Close – Per each Product Schedule for trade date Thursday, Dec 31”",s),
])

def monday_holiday(stem, eve_date, hol_date, eve_name, hol_name,
                   eve_equity=("normal","1515 CT","1515 CT – Regular CME Globex close"),
                   ir_eve=("early_close","1515 CT"), fx_eve=("early_close","1515 CT"),
                   nymex_eve=("early_close","1515 CT / 1615 ET"),
                   halts=(("1030 CT","1700 CT"),("1200 CT","1700 CT"),("1200 CT","1700 CT"),("1215 CT / 1315 ET","1700 CT / 1800 ET")),
                   grain_mon=("late_open","1800 CT"), live_mon=("late_open","1700 CT"),
                   eve_v=None, mon_v=None, extra_eve=None, extra_mon=None):
    pass  # rows are written out explicitly below for verbatim fidelity

# --- MLK 2010
s="2010-martin-luther-king"
H("2010-01-15","Martin Luther King Jr. Day 2010 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Jan 15”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, Jan 15”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Jan 15”",s,close="1515 CT"),
 F("energy","early_close","NYMEX, COMEX® and DME Products on CME Globex / “1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Jan 15”",s,close="1515 CT / 1615 ET"),
 F("metals","early_close","NYMEX, COMEX® and DME Products on CME Globex / “1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Jan 15”",s,close="1515 CT / 1615 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Jan 15 for: … CBOT, KCBT and MGEX Grains”; “Note: Modified grain pre-opening between 14:30 – 15:15”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Jan 15 for: • Livestock”",s),
 F("dairy","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Jan 15 for: … • Dairy”",s),
])
H("2010-01-18","Martin Luther King Jr. Day 2010 (Monday)",[
 F("equity_index","modified","Monday, Jan 18 / “1030 CT – Trading halt • Order entry, modification and cancellation allowed”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, Jan 18 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT CME interest rate / 1730 CT CBOT financial"),
 F("fx","modified","Monday, Jan 18 / “1200 CT – Trading halt • Order entry, modification and cancellation allowed”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","NYMEX, COMEX® and DME Products / Monday, Jan 18 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","NYMEX, COMEX® and DME Products / Monday, Jan 18 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Other CME Group Products / Sunday, Jan 17 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT (Mon Jan 18, for trade date Tue Jan 19)"),
 F("livestock","late_open","Other CME Group Products / Sunday, Jan 17 Exceptions: “Dairy, Livestock, GSCI and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT (Mon Jan 18, for trade date Tue Jan 19)"),
 F("dairy","late_open","Other CME Group Products / Sunday, Jan 17 Exceptions: “Dairy, Livestock, GSCI and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])

# --- Presidents 2010
s="2010-presidents-day"
H("2010-02-12","Presidents' Day 2010 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Feb 12”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, Feb 12”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Feb 12”",s,close="1515 CT"),
 F("energy","early_close","“1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Feb 12”",s,close="1515 CT / 1615 ET"),
 F("metals","early_close","“1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Feb 12”",s,close="1515 CT / 1615 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Feb 12 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Feb 12 for: • Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… • Dairy” (Regular Close, Friday, Feb 12)",s),
])
H("2010-02-15","Presidents' Day 2010 (Monday)",[
 F("equity_index","modified","Monday, Feb 15 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("nikkei_225_dollar","modified","CME Group Equity Products / Sunday, Feb 14 “Exception: USD & JY denominated Nikkei will open at their regularly scheduled times of 02:00 & 05:00 Monday morning.”; Monday, Feb 15 “Exception: USD & JY denominated Nikkei will open at their regularly scheduled times of 02:00 & 05:00 Tuesday morning.”",s,open_="02:00 (USD) & 05:00 (JY) Monday morning; likewise Tuesday morning"),
 F("interest_rates","modified","Monday, Feb 15 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Monday, Feb 15 / “1200 CT – Trading halt • Futures: Order entry, modification and cancellation allowed • Options: Only cancellation allowed”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, Feb 15 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, Feb 15 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, Feb 14 Exceptions: “CBOT, KCBT and MGEX Grain Products & CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","late_open","Sunday, Feb 14 Exceptions: “Dairy, Livestock, GSCI and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
 F("dairy","late_open","Sunday, Feb 14 Exceptions: “Dairy, Livestock, GSCI and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])

# --- Good Friday 2010
s="2010-good-friday"
H("2010-04-01","Good Friday 2010 — preceding trade date (Thursday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Thursday, Apr 1”; “1530 CT – Regular CME Globex Open for trade Date Friday, Apr 2”",s,close="1515 CT",open_="1530 CT"),
 F("interest_rates","normal","“1600 CT – Regular CME Globex close for trade date Thursday, Apr 1”; “1700 CT – Regular CME Globex open for CME interest rate products for trade date Friday, Apr 2”; “1730 CT – Regular CME Globex open for CBOT financial products for trade date Friday, Apr 2”",s,close="1600 CT",open_="1700 CT / 1730 CT"),
 F("fx","normal","“1600 CT – Regular CME Globex close for trade date Thursday, Apr 1”; “1700 CT – Regular CME Globex open for trade date Friday, Apr 2”",s,close="1600 CT",open_="1700 CT"),
 F("energy","normal","NYMEX & COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Thursday, Apr 1”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX & COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Thursday, Apr 1”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Thursday, Apr 1 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Thursday, Apr 1 for: • Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… • Domestic Dairy” (Regular Close, Thursday, Apr 1)",s),
])
H("2010-04-02","Good Friday 2010 (Friday)",[
 F("equity_index","early_close","CME Group Equity Products / Friday, Apr 2 / “0815 CT - Early CME Globex close for trade date Friday Apr 2”",s,close="0815 CT"),
 F("interest_rates","early_close","CME Group Interest Rate Products / Friday, Apr 2 / “1015 CT - Early CME Globex close for trade date Friday Apr 2”",s,close="1015 CT"),
 F("fx","early_close","CME Group FX Products / Friday, Apr 2 / “1015 CT - Early CME Globex close for trade date Friday Apr 2”",s,close="1015 CT"),
 F("energy","closed","NYMEX & COMEX® and DME Products / Friday, Apr 2 / “No CME Globex Trading on Good Friday”",s,open_="1700 CT / 1800 ET Sunday Apr 4"),
 F("metals","closed","NYMEX & COMEX® and DME Products / Friday, Apr 2 / “No CME Globex Trading on Good Friday”",s,open_="1700 CT / 1800 ET Sunday Apr 4"),
 F("grains","closed","Other CME Group Products / Friday, Apr 2 / “No CME Globex Trading on Good Friday”; Sunday, Apr 4 “1800 CT – Regular CME Globex open for CBOT, KCBT and MGEX Grain Products & CBOT Ethanol for Trade date Monday April 5”",s,open_="1800 CT Sunday Apr 4"),
 F("livestock","closed","Other CME Group Products / Friday, Apr 2 / “No CME Globex Trading on Good Friday”; Sunday, Apr 4 “Exceptions: Livestock, TRAKRS and ETFs will remain closed until their regularly scheduled open on Monday”",s,open_="regularly scheduled open Monday Apr 5"),
 F("dairy","closed","Other CME Group Products / Friday, Apr 2 / “No CME Globex Trading on Good Friday”",s),
])

# --- Memorial 2010
s="2010-memorial-day"
H("2010-05-28","Memorial Day 2010 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, May 28”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, May 28”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, May 28”",s,close="1515 CT"),
 F("energy","early_close","“1515 CT / 1615 ET – Early CME Globex close for trade date Friday, May 28”",s,close="1515 CT / 1615 ET"),
 F("metals","early_close","“1515 CT / 1615 ET – Early CME Globex close for trade date Friday, May 28”",s,close="1515 CT / 1615 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, May 28 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, May 28 for: Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy” (Regular Close, Friday, May 28)",s),
])
H("2010-05-31","Memorial Day 2010 (Monday)",[
 F("equity_index","modified","Monday, May 31 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, May 31 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Monday, May 31 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, May 31 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, May 31 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, May 30 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","late_open","Sunday, May 30 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSCI and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
 F("dairy","late_open","Sunday, May 30 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSCI and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])

# --- July 4 2010
s="2010-4th-of-july"
H("2010-07-02","Independence Day 2010 (observed Mon Jul 5) — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, July 2”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, July 2”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, July 2”",s,close="1515 CT"),
 F("energy","early_close","“1515 CT / 1615 ET – Early CME Globex close for trade date Friday, July 2”",s,close="1515 CT / 1615 ET"),
 F("metals","early_close","“1515 CT / 1615 ET – Early CME Globex close for trade date Friday, July 2”",s,close="1515 CT / 1615 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday July 2 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … for: • Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… • Dairy”",s),
])
H("2010-07-05","Independence Day 2010 observed (Monday)",[
 F("equity_index","modified","Monday, July 5 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, July 5 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Monday, July 5 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, July 5 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, July 5 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, July 4 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","late_open","Sunday, July 4 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSCI and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
 F("dairy","late_open","Sunday, July 4 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSCI and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])

# --- Labor 2010
s="2010-labor-day"
H("2010-09-03","Labor Day 2010 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Sep 3”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, Sep 3”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Sep 3”",s,close="1515 CT"),
 F("energy","early_close","“1515 CT / 1615 ET –Early CME Globex close for trade date Friday, Sep 3”",s,close="1515 CT / 1615 ET"),
 F("metals","early_close","“1515 CT / 1615 ET –Early CME Globex close for trade date Friday, Sep 3”",s,close="1515 CT / 1615 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Sep 3 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … • Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… • International & Domestic Dairy”",s),
])
H("2010-09-06","Labor Day 2010 (Monday)",[
 F("equity_index","modified","Monday, Sep 6 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, Sep 6 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Monday, Sept 6 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, Sept 6 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, Sept 6 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, Sep 5 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","late_open","Sunday, Sep 5 Exceptions: “Domestic Dairy, Livestock,, GSCI and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
 F("dairy","late_open","Sunday, Sep 5 Exceptions: “Domestic Dairy, Livestock,, GSCI and Weather products will remain closed until 1700 CT on Monday”; Monday, Sep 6 “1200 CT – International Dairy, Real Estate & Forestry products trading halt”",s,open_="1700 CT (domestic dairy)",close="1200 CT (international dairy halt)"),
])

# --- Columbus 2010
s="2010-columbus-day"
H("2010-10-08","Columbus Day 2010 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Oct 8”",s,close="1515 CT"),
 F("interest_rates","early_close","CME Group Interest Products / “1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, Oct 8”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Oct 8”",s,close="1515 CT"),
 F("energy","early_close","“1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Oct 8”",s,close="1515 CT / 1615 ET"),
 F("metals","early_close","“1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Oct 8”",s,close="1515 CT / 1615 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Oct 8 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … • Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… • International & Domestic Dairy”",s),
])
H("2010-10-11","Columbus Day 2010 (Monday) — CME Globex traded a normal session",[
 F("equity_index","normal","Monday, Oct 11 / “1515 CT – Regular CME Globex close for trade date Monday, Oct 11”",s,close="1515 CT",open_="1700 CT Sunday Oct 10"),
 F("interest_rates","normal","Monday, Oct 11 / “1600 CT – Regular CME Globex close for trade date Monday, Oct 11”; Sunday “1700 CT … CME interest rate … 1730 CT … CBOT financial”",s,close="1600 CT",open_="1700 CT / 1730 CT Sunday Oct 10"),
 F("fx","normal","Monday, Oct 11 / “1600 CT – Regular CME Globex close for trade date Monday, Oct 11”",s,close="1600 CT",open_="1700 CT Sunday Oct 10"),
 F("energy","normal","Monday, Oct 11 / “1615 CT / 1715 ET – Regular CME Globex Close for trade date Oct 11”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Sunday Oct 10"),
 F("metals","normal","Monday, Oct 11 / “1615 CT / 1715 ET – Regular CME Globex Close for trade date Oct 11”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Sunday Oct 10"),
 F("grains","normal","Sunday, Oct 10 “1800 CT – Regular CME Globex open for CBOT, KCBT and MGEX Grains and CBOT Ethanol for trade date Monday, Oct 11”; Monday “Per each product schedule – Regular CME Globex close for trade date Monday, Oct 11.”",s,open_="1800 CT Sunday Oct 10"),
 F("livestock","normal","Sunday, Oct 10 “Exceptions: Livestock, Domestic Dairy, TRAKRS and ETFs will remain closed until their regularly scheduled open on Monday” (i.e. their normal Monday open)",s),
 F("dairy","normal","Sunday, Oct 10 “Exceptions: Livestock, Domestic Dairy, TRAKRS and ETFs will remain closed until their regularly scheduled open on Monday”",s),
])

# --- Veterans 2010
s="2010-veterans-day"
H("2010-11-11","Veterans Day 2010 (Thursday) — CME Globex traded a normal session",[
 F("equity_index","normal","Thursday, Nov 11 / “1515 CT – Regular CME Globex close for trade date Thursday, Nov 11”; “1530 CT – Regular CME Globex open for trade date of Friday, Nov 12”",s,close="1515 CT",open_="1530 CT"),
 F("interest_rates","normal","Thursday, Nov 11 / “1600 CT – Regular CME Globex close for all CME interest rate and CBOT financial products for trade date Thursday, Nov 11”; “1700 CT … / 1730 CT … for trade date Friday, Nov 12”",s,close="1600 CT",open_="1700 CT / 1730 CT"),
 F("fx","normal","Thursday, Nov 11 / “1600 CT – Regular CME Globex close for trade date Thursday, Nov 11”; “1700 CT – Regular CME Globex open for trade date Friday, Nov 12”",s,close="1600 CT",open_="1700 CT"),
 F("energy","normal","Thursday, Nov 11 / “1615 CT / 1715 ET – Regular CME Globex close for trade date of Thursday, Nov 11”; “1700 CT / 1800 ET – Regular CME Globex open for trade date Friday, Nov 12”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("metals","normal","Thursday, Nov 11 / “1615 CT / 1715 ET – Regular CME Globex close for trade date of Thursday, Nov 11”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("grains","normal","The document prints no deviation for CBOT/KCBT/MGEX grain products on Veterans Day 2010; all listed groups keep regular hours.",s),
 F("livestock","normal","The document prints no deviation for Livestock on Veterans Day 2010.",s),
])

# --- Thanksgiving 2010
s="2010-thanksgiving"
H("2010-11-24","Thanksgiving 2010 — preceding trade date (Wednesday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Wednesday, Nov 24”; “1530 CT – Regular CME Globex open for trade date Friday, Nov 26”",s,close="1515 CT",open_="1530 CT"),
 F("interest_rates","normal","“1600 CT – Regular CME Globex close for all CME interest rate and CBOT financial products for trade date Wednesday, Nov 24”; “1700 CT … 1730 CT … for trade date Friday, Nov 26”",s,close="1600 CT",open_="1700 CT / 1730 CT"),
 F("fx","normal","“1600 CT – Regular CME Globex close for trade date Wednesday, Nov 24”; “1700 CT – Regular CME Globex open for trade date Friday, Nov 26”",s,close="1600 CT",open_="1700 CT"),
 F("energy","normal","“1615 CT / 1715 ET – Regular CME Globex close for trade date Wednesday, Nov 24”; “1700 CT / 1800 ET – Regular CME Globex open for trade date Friday, Nov 26”; “Exception: NYMEX Softs TAS (CJT, KTT, TTT, and YOT) will remain closed until their regular open on Sunday, November 28”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("metals","normal","“1615 CT / 1715 ET – Regular CME Globex close for trade date Wednesday, Nov 24”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for Agricultural, Real Estate, TRAKRS, ETF, GSCI, Weather, Forestry, CBOT Ethanol and Eurozone HICP for trade date Wednesday, Nov 24”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close - Per each product schedule for Agricultural … for trade date Wednesday, Nov 24”",s),
 F("dairy","normal","Other CME Group Products / Exceptions: “Dairy products will remain closed until their regularly scheduled open on Sunday, Nov 28”",s),
])
H("2010-11-25","Thanksgiving Day 2010 (Thursday)",[
 F("equity_index","modified","Thursday, Nov 25 / “1030 CT – CME Globex trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Thursday, Nov 25 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading”; “1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Thursday, Nov 25 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Thursday, Nov 25 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Thursday, Nov 25 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Other CME Group Products / Exceptions: “CBOT,KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Thursday Nov 25”",s,open_="1800 CT"),
 F("livestock","late_open","Other CME Group Products / Exceptions: “Livestock, GSCI, Lumber, Crude Palm Oil and Weather will remain closed until their open at 1700 CT on Thursday Nov 25.”",s,open_="1700 CT"),
 F("lumber","late_open","Other CME Group Products / Exceptions: “Livestock, GSCI, Lumber, Crude Palm Oil and Weather will remain closed until their open at 1700 CT on Thursday Nov 25.”",s,open_="1700 CT"),
 F("dairy","closed","Other CME Group Products / Exceptions: “Dairy products will remain closed until their regularly scheduled open on Sunday, Nov 28”",s,open_="regularly scheduled open Sunday Nov 28"),
])
H("2010-11-26","Day after Thanksgiving 2010 (Friday)",[
 F("equity_index","early_close","Friday, Nov 26 / “1215 CT – Early CME Globex close for trade date Friday, Nov 26”",s,close="1215 CT"),
 F("interest_rates","early_close","Friday, Nov 26 / “1215 CT – Early CME Globex close for trade date Friday, Nov 26”",s,close="1215 CT"),
 F("fx","early_close","Friday, Nov 26 / “1215 CT – Early CME Globex close for trade date Friday, Nov 26”",s,close="1215 CT"),
 F("energy","early_close","Friday, Nov 26 / “1245 CT / 1345 ET – Early CME Globex Close for trade date Friday, Nov 26”; “Exceptions: TAS contracts close at 12:30 CT / 1330 ET”",s,close="1245 CT / 1345 ET"),
 F("metals","early_close","Friday, Nov 26 / “1245 CT / 1345 ET – Early CME Globex Close for trade date Friday, Nov 26”; “Silver TAS contracts close at 12:25 CT / 13:25 ET”",s,close="1245 CT / 1345 ET"),
 F("grains","early_close","Friday, Nov 26 / “1200 CT – Early CME Globex close for CME Agricultural Futures, CBOT Grain Futures & Options, CBOT Ethanol, KCBT Grain Futures & Options, Forestry, Weather, GSCI and TRAKRS products for trade date Friday, Nov 26”; “1215 CT – Early CME Globex close for ETF, Real Estate & MGEX Grain Products”; “1230 CT – Early CME Globex close for CBOT Mini – Sized Grain Futures”",s,close="1200 CT CBOT/KCBT grain futures & options; 1215 CT MGEX; 1230 CT CBOT mini-sized grain futures"),
 F("livestock","early_close","Friday, Nov 26 / “1200 CT – Early CME Globex close for CME Agricultural Futures …”; “1202 CT – Early CME Globex close for CME Agricultural Options”",s,close="1200 CT futures / 1202 CT options"),
 F("lumber","early_close","Friday, Nov 26 / “1200 CT – Early CME Globex close for … Forestry … for trade date Friday, Nov 26”",s,close="1200 CT"),
 F("dairy","closed","Other CME Group Products / Exceptions: “Dairy products will remain closed until their regularly scheduled open on Sunday, Nov 28”",s),
])

# --- Christmas 2010
s="2010-christmas"
H("2010-12-23","Christmas 2010 — preceding trade date (Thursday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Thursday, Dec 23”",s,close="1515 CT"),
 F("interest_rates","normal","“1600 CT – Regular CME Globex close for all CME interest rate and CBOT financial products for trade date Thursday, Dec 23”",s,close="1600 CT"),
 F("fx","normal","“1600 CT – Regular CME Globex close for trade date Thursday, Dec 23”",s,close="1600 CT"),
 F("energy","normal","“1615 CT / 1715 ET –Regular CME Globex close for trade date Thursday, Dec 23”; “Exception: … Energy TAS contracts will close at 1230 CT / 1330 ET” (the 12/23/2010 revision adds “European Gasoil TAS Contracts will close at 1000 CT / 1100 ET”)",s,close="1615 CT / 1715 ET"),
 F("metals","normal","“1615 CT / 1715 ET –Regular CME Globex close for trade date Thursday, Dec 23”; “Exception: Silver TAS contracts will close at 1125 CT / 1225 ET / Gold TAS Contracts will close at 1130 CT / 1230 ET”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close – per each product schedule for trade date Thursday, Dec 23”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close – per each product schedule for trade date Thursday, Dec 23”",s),
])
H("2010-12-24","Christmas Day 2010 observed (Friday, Dec 24)",[
 F("equity_index","closed","CME Group Equity Products / Friday, Dec 24 / “CME Globex is closed”; Sunday, Dec 26 “1700 CT – Regular CME Globex open for trade date Monday, Dec 27”",s,open_="1700 CT Sunday Dec 26"),
 F("interest_rates","closed","CME Group Interest Rate Products / Friday, Dec 24 / “CME Globex is closed”; Sunday, Dec 26 “1700 CT … CME interest rate … 1730 CT … CBOT financial … for trade date Monday, Dec 27”",s,open_="1700 CT / 1730 CT Sunday Dec 26"),
 F("fx","closed","CME Group FX Products / Friday, Dec 24 / “CME Globex is closed”",s,open_="1700 CT Sunday Dec 26"),
 F("energy","closed","NYMEX, COMEX® and DME Products / Friday, Dec 24 / “CME Globex is closed”",s,open_="1700 CT / 1800 ET Sunday Dec 26"),
 F("metals","closed","NYMEX, COMEX® and DME Products / Friday, Dec 24 / “CME Globex is closed”",s,open_="1700 CT / 1800 ET Sunday Dec 26"),
 F("grains","closed","Other CME Group Products / Friday, Dec 24 / “CME Globex is closed”; Sunday, Dec 26 “1800 CT – Regular CME Globex open for CBOT, KCBT and MGEX Grains for trade date Monday, Dec 27”",s,open_="1800 CT Sunday Dec 26"),
 F("livestock","closed","Other CME Group Products / Friday, Dec 24 / “CME Globex is closed”; “Exceptions: CME Livestock, Lumber, TRAKRS and ETFs will remain closed until their regularly scheduled open on Monday Dec 27”",s,open_="regularly scheduled open Monday Dec 27"),
 F("lumber","closed","Other CME Group Products / “Exceptions: CME Livestock, Lumber, TRAKRS and ETFs will remain closed until their regularly scheduled open on Monday Dec 27”",s,open_="regularly scheduled open Monday Dec 27"),
])

# --- New Year's Eve 2010 (from the 2011 New Year's document)
s="2011-new-years"
H("2010-12-31","New Year's 2011 — New Year's Eve (Friday, Dec 31 2010). New Year's Day 2011 fell on a Saturday; CME published no separate closed day.",[
 F("equity_index","normal","CME Group Equity Products / Friday, Dec 31 / “1515 CT – Regular CME Globex close for trade date Friday, Dec 31”",s,close="1515 CT"),
 F("interest_rates","early_close","CME Group Interest Rate Products / Friday, Dec 31 / “1215 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, Dec 31”",s,close="1215 CT"),
 F("fx","early_close","CME Group FX Products / Friday, Dec 31 / “1215 CT – Early CME Globex close for trade date Friday, Dec 31”",s,close="1215 CT"),
 F("energy","early_close","NYMEX, COMEX® and DME Products / Friday, Dec 31 / “1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Dec 31”",s,close="1515 CT / 1615 ET"),
 F("metals","early_close","NYMEX, COMEX® and DME Products / Friday, Dec 31 / “1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Dec 31”",s,close="1515 CT / 1615 ET"),
 F("grains","early_close","Other CME Group Products / Friday, Dec 31 / “1200 CT Early Close – For each Product for trade date Friday, Dec 31 … CBOT and KCBT Grains … CBOT Ethanol”; “1215 CT Early Close for MGEX products”; “1230 CT Early Close for CBOT MINI Grains”; “Note: Modified grain pre-opening between 1300 – 1515”",s,close="1200 CT CBOT/KCBT grains; 1215 CT MGEX; 1230 CT CBOT mini grains"),
 F("livestock","early_close","Other CME Group Products / Friday, Dec 31 / “1215 CT Early Close for Futures and Options on Forestry, Livestock, & Dairy”",s,close="1215 CT"),
 F("dairy","early_close","Other CME Group Products / Friday, Dec 31 / “1215 CT Early Close for Futures and Options on Forestry, Livestock, & Dairy”",s,close="1215 CT"),
 F("lumber","early_close","Other CME Group Products / Friday, Dec 31 / “1215 CT Early Close for Futures and Options on Forestry, Livestock, & Dairy”",s,close="1215 CT"),
])
H("2011-01-02","New Year's 2011 — Sunday reopen (Jan 2 2011)",[
 F("equity_index","normal","Sunday, Jan 2 / “1700 CT – Regular CME Globex open for trade date Monday, Jan 3”",s,open_="1700 CT"),
 F("interest_rates","normal","Sunday, Jan 2 / “1700 CT – Regular CME Globex open for CME interest rate products for trade date Monday, Jan 3”; “1730 CT – Regular CME Globex open for CBOT financial products for trade date Monday, Jan 3”",s,open_="1700 CT / 1730 CT"),
 F("fx","normal","Sunday, Jan 2 / “1700 CT – Regular CME Globex open for trade date Monday, Jan 3”",s,open_="1700 CT"),
 F("energy","normal","Sunday, Jan 2 / “1700 CT / 1800 ET – Regular CME Globex open for trade date Monday, Jan 3”",s,open_="1700 CT / 1800 ET"),
 F("metals","normal","Sunday, Jan 2 / “1700 CT / 1800 ET – Regular CME Globex open for trade date Monday, Jan 3”",s,open_="1700 CT / 1800 ET"),
 F("grains","normal","Sunday, Jan 2 / “1800 CT – Regular CME Globex open for CBOT, KCBT & MGEX Grains for trade date Monday, Jan 3”",s,open_="1800 CT"),
 F("livestock","normal","Sunday, Jan 2 / “Exceptions: CME Livestock, Lumber, TRAKRS and ETFs will remain closed until their regularly scheduled open on Monday Jan 3”",s),
 F("lumber","normal","Sunday, Jan 2 / “Exceptions: CME Livestock, Lumber, TRAKRS and ETFs will remain closed until their regularly scheduled open on Monday Jan 3”",s),
])
json.dump(HOL,open("part1.json","w"),indent=1,ensure_ascii=False)
print(len(HOL),"entries in part1")
