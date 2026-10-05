# -*- coding: utf-8 -*-
import json
exec(open("build.py").read().split("HOL=[]")[0])
HOL=[]
def H(date,name,fams): HOL.append({"date":date,"name":name,"families":fams})
def F(fam,status,verbatim,stem,close=None,open_=None):
    d={"family":fam,"status":status,"verbatim":verbatim,"document":doc(stem),"tier":"T1"}
    if close: d["close_instant"]=close
    if open_: d["open_instant"]=open_
    return d

# ================= 2011 =================
s="2011-martin-luther-king"
H("2011-01-14","Martin Luther King Jr. Day 2011 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Jan 14”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, Jan 14”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Jan 14”",s,close="1515 CT"),
 F("energy","early_close","NYMEX, COMEX® and DME Products / “1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Jan 14”",s,close="1515 CT / 1615 ET"),
 F("metals","early_close","NYMEX, COMEX® and DME Products / “1515 CT / 1615 ET – Early CME Globex close for trade date Friday, Jan 14”",s,close="1515 CT / 1615 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Jan 14 for: … ·CBOT, KCBT and MGEX Grains”; “Note: Modified grain pre-opening between 14:30 – 15:15”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … · Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… ·Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… ·Lumber”",s),
])
H("2011-01-17","Martin Luther King Jr. Day 2011 (Monday)",[
 F("equity_index","modified","Monday, Jan 17 / “1030 CT – Trading halt · Order entry, modification and cancellation allowed”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, Jan 17 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Monday, Jan 17 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, Jan 17 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, Jan 17 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, Jan 16 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","late_open","Sunday, Jan 16 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSCI, Lumber and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
 F("dairy","late_open","Sunday, Jan 16 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSCI, Lumber and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
 F("lumber","late_open","Sunday, Jan 16 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSCI, Lumber and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])
s="2011-presidents-day"
H("2011-02-18","Presidents' Day 2011 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Feb 18”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, Feb 18”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Feb 18”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Feb 18” (no early close, unlike 2010)",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Feb 18”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Feb 18 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… Lumber”",s),
])
H("2011-02-21","Presidents' Day 2011 (Monday)",[
 F("equity_index","modified","Monday, Feb 21 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, Feb 21 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Monday, Feb 21 / “1200 CT – Trading halt · Futures: Order entry, modification and cancellation allowed · Options: Only cancellation allowed”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, Feb 21 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, Feb 21 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, Feb 20 Exceptions: “CBOT, KCBT and MGEX Grain Products & CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","late_open","Sunday, Feb 20 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSC, Lumber and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
 F("dairy","late_open","Sunday, Feb 20 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSC, Lumber and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
 F("lumber","late_open","Sunday, Feb 20 Exceptions: “Dairy, Crude Palm Oil, Livestock, GSC, Lumber and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])
s="2011-good-friday"
H("2011-04-21","Good Friday 2011 — preceding trade date (Thursday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Thursday, Apr 21”",s,close="1515 CT"),
 F("interest_rates","normal","“1600 CT – Regular CME Globex close for trade date Thursday, Apr 21”",s,close="1600 CT"),
 F("fx","normal","“1600 CT – Regular CME Globex close for trade date Thursday, Apr 21”",s,close="1600 CT"),
 F("energy","normal","NYMEX & COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Thursday, Apr 21”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX & COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Thursday, Apr 21”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Thursday, Apr 21 for: CBOT, KCBT and MGEX Grains …”",s),
 F("livestock","early_close","Other CME Group Products / Thursday, Apr 21 / “1355 CT – Early Close for Lumber, Dairy and Livestock”",s,close="1355 CT"),
 F("dairy","early_close","Other CME Group Products / Thursday, Apr 21 / “1355 CT – Early Close for Lumber, Dairy and Livestock”",s,close="1355 CT"),
 F("lumber","early_close","Other CME Group Products / Thursday, Apr 21 / “1355 CT – Early Close for Lumber, Dairy and Livestock”",s,close="1355 CT"),
])
H("2011-04-22","Good Friday 2011 (Friday) — full Globex closure, unlike 2010",[
 F("equity_index","closed","CME Group Equity Products / Friday, Apr 22 / “CME Globex is closed”; Sunday, Apr 24 “1700 CT – Regular CME Globex open for trade date Monday, Apr 25”",s,open_="1700 CT Sunday Apr 24"),
 F("interest_rates","closed","CME Group Interest Rate Products / Friday, Apr 22 / “CME Globex is closed”; Sunday, Apr 24 “1700 CT … CME interest rate … 1730 CT … CBOT financial … Monday, Apr 25”",s,open_="1700 CT / 1730 CT Sunday Apr 24"),
 F("fx","closed","CME Group FX Products / Friday, Apr 22 / “CME Globex is closed”",s,open_="1700 CT Sunday Apr 24"),
 F("energy","closed","NYMEX & COMEX® and DME Products / Friday, Apr 22 / “CME Globex is closed”",s,open_="1700 CT / 1800 ET Sunday Apr 24"),
 F("metals","closed","NYMEX & COMEX® and DME Products / Friday, Apr 22 / “CME Globex is closed”",s,open_="1700 CT / 1800 ET Sunday Apr 24"),
 F("grains","closed","Other CME Group Products / Friday, Apr 22 / “CME Globex is closed”; Sunday, Apr 24 “1800 CT – Regular CME Globex open for CBOT, KCBT and MGEX Grain Products & CBOT Ethanol for Trade date Monday April 25”",s,open_="1800 CT Sunday Apr 24"),
 F("livestock","closed","Other CME Group Products / Friday, Apr 22 / “CME Globex is closed”; “Exceptions: Livestock, Lumber, & TRAKRS will remain closed until their regularly scheduled open on Monday”",s,open_="regularly scheduled open Monday Apr 25"),
 F("lumber","closed","Other CME Group Products / “Exceptions: Livestock, Lumber, & TRAKRS will remain closed until their regularly scheduled open on Monday”",s,open_="regularly scheduled open Monday Apr 25"),
 F("dairy","closed","Other CME Group Products / Friday, Apr 22 / “CME Globex is closed”",s),
])
s="2011-memorial-day"
H("2011-05-27","Memorial Day 2011 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, May 27”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, May 27”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, May 27”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, May 27”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, May 27”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, May 27 for: … • CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … • Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… • Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… • Lumber”",s),
])
H("2011-05-30","Memorial Day 2011 (Monday)",[
 F("equity_index","modified","Monday, May 30 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, May 30 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Monday, May 30 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, May 30 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, May 30 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, May 29 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","closed","Sunday, May 29 Exceptions: “Livestock will remain closed until its scheduled opening 0905 CT on Tuesday”",s,open_="0905 CT Tuesday May 31"),
 F("lumber","closed","Sunday, May 29 Exceptions: “Lumber will remain closed until its scheduled opening of 0900 CT on Tuesday”",s,open_="0900 CT Tuesday May 31"),
 F("dairy","late_open","Sunday, May 29 Exceptions: “Dairy, Crude Palm Oil, GSCI, and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])
s="2011-4th-of-july"
H("2011-07-01","Independence Day 2011 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, July 1”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, July 1”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, July 1”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, July 1”; “TAS/TAM Products - Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, July 1”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday July 1 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… Lumber”",s),
])
H("2011-07-04","Independence Day 2011 (Monday)",[
 F("equity_index","modified","Monday, July 4 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, July 4 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Monday, July 4 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, July 4 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, July 4 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, July 3 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","closed","Sunday, July 3 Exceptions: “Livestock will remain closed until its scheduled opening 0905 CT on Tuesday”",s,open_="0905 CT Tuesday July 5"),
 F("lumber","closed","Sunday, July 3 Exceptions: “Lumber will remain closed until its scheduled opening of 0900 CT on Tuesday”",s,open_="0900 CT Tuesday July 5"),
 F("dairy","late_open","Sunday, July 3 Exceptions: “Dairy, Crude Palm Oil, GSCI, and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])
s="2011-labor-day"
H("2011-09-02","Labor Day 2011 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Sep 2”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for all CME interest rate and CBOT financial products for trade date Friday, Sep 2”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Sep 2”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET –Regular CME Globex close for trade date Friday, Sep 2”; “TAS/TAM Products - Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET –Regular CME Globex close for trade date Friday, Sep 2”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Sep 2 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… Lumber”",s),
])
H("2011-09-05","Labor Day 2011 (Monday)",[
 F("equity_index","modified","Monday, Sep 5 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, Sep 5 / “1200 CT – CME interest rate and CBOT financial products trading halt”; “1700 CT – Halted CME interest rate products resume trading / 1730 CT – Halted CBOT financial products resume trading”",s,close="1200 CT",open_="1700 CT / 1730 CT"),
 F("fx","modified","Monday, Sep 5 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, Sep 5 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, Sep 5 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, Sep 4 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","closed","Sunday, Sep 4 Exceptions: “Livestock will remain closed until its scheduled opening 0905 CT on Tuesday”",s,open_="0905 CT Tuesday Sep 6"),
 F("lumber","closed","Sunday, Sep 4 Exceptions: “Lumber will remain closed until its scheduled opening of 0900 CT on Tuesday”",s,open_="0900 CT Tuesday Sep 6"),
 F("dairy","late_open","Sunday, Sep 4 Exceptions: “Dairy, Crude Palm Oil, GSCI, and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])
s="2011-columbus-day"
H("2011-10-07","Columbus Day 2011 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Oct 7”",s,close="1515 CT"),
 F("interest_rates","early_close","CME Group Interest Products / “1515 CT – Early CME Globex close for trade date Friday, Oct 7”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Oct 7”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Oct 7”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Oct 7”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Oct 7 for: … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… Lumber”",s),
])
H("2011-10-10","Columbus Day 2011 (Monday) — CME Globex traded a normal session",[
 F("equity_index","normal","Monday, Oct 10 / “1515 CT – Regular CME Globex close for trade date Monday, Oct 10”",s,close="1515 CT",open_="1700 CT Sunday Oct 9"),
 F("interest_rates","normal","Monday, Oct 10 / “1600 CT – Regular CME Globex close for trade date Monday, Oct 10”",s,close="1600 CT",open_="1700 CT Sunday Oct 9"),
 F("fx","normal","Monday, Oct 10 / “1600 CT – Regular CME Globex close for trade date Monday, Oct 10”",s,close="1600 CT",open_="1700 CT Sunday Oct 9"),
 F("energy","normal","Monday, Oct 10 / “1615 CT / 1715 ET – Regular CME Globex Close for trade date Monday, Oct 10”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Sunday Oct 9"),
 F("metals","normal","Monday, Oct 10 / “1615 CT / 1715 ET – Regular CME Globex Close for trade date Monday, Oct 10”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Sunday Oct 9"),
 F("grains","normal","Sunday, Oct 9 “1800 CT – Regular CME Globex open for CBOT, KCBT and MGEX Grains and CBOT Ethanol for trade date Monday, Oct 10”; Monday “Per each product schedule – Regular CME Globex close for trade date Monday, Oct 10.”",s,open_="1800 CT Sunday Oct 9"),
 F("livestock","normal","Sunday, Oct 9 “Exceptions: Livestock, Lumber & TRAKRS will remain closed until their regularly scheduled open on Monday”",s),
 F("lumber","normal","Sunday, Oct 9 “Exceptions: Livestock, Lumber & TRAKRS will remain closed until their regularly scheduled open on Monday”",s),
])
s="2011-veterans-day"
H("2011-11-11","Veterans Day 2011 (Friday) — CME Globex traded a normal session",[
 F("equity_index","normal","Friday, Nov 11 / “1515 CT – Regular CME Globex close for trade date Friday, Nov 11”; Thursday, Nov 10 “1530 CT – Regular CME Globex open for trade date of Friday, Nov 11”",s,close="1515 CT",open_="1530 CT Thursday Nov 10"),
 F("interest_rates","normal","Friday, Nov 11 / “1600 CT – Regular CME Globex close for trade date Friday, Nov 11”; Thursday, Nov 10 “1700 CT – Regular CME Globex open for trade date Friday, Nov 11”",s,close="1600 CT",open_="1700 CT Thursday Nov 10"),
 F("fx","normal","Friday, Nov 11 / “1600 CT – Regular CME Globex close for trade date Friday, Nov 11”",s,close="1600 CT",open_="1700 CT Thursday Nov 10"),
 F("energy","normal","Friday, Nov 11 / “1615 CT / 1715 ET – Regular CME Globex close for trade date of Friday, Nov 11”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Thursday Nov 10"),
 F("metals","normal","Friday, Nov 11 / “1615 CT / 1715 ET – Regular CME Globex close for trade date of Friday, Nov 11”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Thursday Nov 10"),
 F("grains","normal","Other CME Group Products, including KCBT and MGEX on CME Globex / Friday, Nov 11 “Regular CME Globex Close – Per each product schedule for trade date Friday, Nov 11”",s),
 F("livestock","normal","Other CME Group Products … / Friday, Nov 11 “Regular CME Globex Close – Per each product schedule for trade date Friday, Nov 11”",s),
])
s="2011-thanksgiving"
H("2011-11-23","Thanksgiving 2011 — preceding trade date (Wednesday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Wednesday, Nov 23”; “1530 CT – Regular CME Globex open for trade date Friday, Nov 25”",s,close="1515 CT",open_="1530 CT"),
 F("interest_rates","normal","“1600 CT – Regular CME Globex close for trade date Wednesday, Nov 23”; “1700 CT – Regular CME Globex open for trade date Friday, Nov 25”",s,close="1600 CT",open_="1700 CT"),
 F("fx","normal","“1600 CT – Regular CME Globex close for trade date Wednesday, Nov 23”; “1700 CT – Regular CME Globex open for trade date Friday, Nov 25”",s,close="1600 CT",open_="1700 CT"),
 F("energy","normal","“1615 CT / 1715 ET – Regular CME Globex close for trade date Wednesday, Nov 23”; “1700 CT / 1800 ET – Regular CME Globex open for trade date Friday, Nov 25”; “Exception: NYMEX Softs TAS (CJT, KTT, TTT, and YOT) will remain closed until their regular open on Sunday, November 27”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("metals","normal","“1615 CT / 1715 ET – Regular CME Globex close for trade date Wednesday, Nov 23”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Wednesday, Nov 23 for: … CBOT, KCBT and MGEX Grains & Juice”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … Livestock”",s),
 F("lumber","normal","Other CME Group Products / “… Lumber”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy”; Exceptions “Dairy products will remain closed until their regularly scheduled open on Sunday, Nov 27”",s),
])
H("2011-11-24","Thanksgiving Day 2011 (Thursday)",[
 F("equity_index","modified","Thursday, Nov 24 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Thursday, Nov 24 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("fx","modified","Thursday, Nov 24 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Thursday, Nov 24 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Thursday, Nov 24 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Other CME Group Products / Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Thursday, Nov 24”",s,open_="1800 CT"),
 F("livestock","late_open","Other CME Group Products / Exceptions: “Livestock, GSCI, Lumber, Crude Palm Oil and Weather will remain closed until their open at 1700 CT on Thursday, Nov 24.”",s,open_="1700 CT"),
 F("lumber","late_open","Other CME Group Products / Exceptions: “Livestock, GSCI, Lumber, Crude Palm Oil and Weather will remain closed until their open at 1700 CT on Thursday, Nov 24.”",s,open_="1700 CT"),
 F("dairy","closed","Other CME Group Products / Exceptions: “Dairy products will remain closed until their regularly scheduled open on Sunday, Nov 27”",s,open_="regularly scheduled open Sunday Nov 27"),
])
H("2011-11-25","Day after Thanksgiving 2011 (Friday)",[
 F("equity_index","early_close","Friday, Nov 25 / “1215 CT – Early CME Globex close for trade date Friday, Nov 25”",s,close="1215 CT"),
 F("interest_rates","early_close","Friday, Nov 25 / “1215 CT – Early CME Globex close for trade date Friday, Nov 25”",s,close="1215 CT"),
 F("fx","early_close","Friday, Nov 25 / “1215 CT – Early CME Globex close for trade date Friday, Nov 25”",s,close="1215 CT"),
 F("energy","early_close","Friday, Nov 25 / “1245 CT / 1345 ET – Early CME Globex Close for trade date Friday, Nov 25”; “Exceptions: … All Crude, Heating Oil, RBOB & Nat Gas TAS contracts close early at 12:30 CT / 1330 ET”",s,close="1245 CT / 1345 ET"),
 F("metals","early_close","Friday, Nov 25 / “1245 CT / 1345 ET – Early CME Globex Close for trade date Friday, Nov 25”; “Exceptions: Copper TAS – Early Close 1100 CT / 1200 ET; Silver TAS- Early Close 1125 CT / 1225 ET; Gold TAS – Early Close 1130 CT / 1230 ET”",s,close="1245 CT / 1345 ET"),
 F("grains","early_close","Friday, Nov 25 / “1200 CT – Early CME Globex close for CBOT Grain Futures & Options, CBOT Ethanol, KCBT Grain Futures & Options, Forestry, Weather, Dow Jones UBS ER and GSCI for trade date Friday, Nov 25”; “1215 CT – Early CME Globex close for … MGEX Grain products”; “1230 CT – Early CME Globex close for CBOT Mini – Sized Grain Futures”",s,close="1200 CT CBOT/KCBT; 1215 CT MGEX; 1230 CT CBOT mini-sized grain futures"),
 F("livestock","early_close","Friday, Nov 25 / “1215 CT – Early CME Globex close for CME Livestock Futures & Options, Real Estate & MGEX Grain products for trade date Friday, Nov 25”",s,close="1215 CT"),
 F("lumber","early_close","Friday, Nov 25 / “1200 CT – Early CME Globex close for … Forestry …”; “1202 CT – Early CME Globex close for CME Lumber Options for trade date Friday, Nov 25”",s,close="1200 CT futures (Forestry) / 1202 CT Lumber options"),
 F("dairy","closed","Other CME Group Products / Exceptions: “Dairy products will remain closed until their regularly scheduled open on Sunday, Nov 27”",s),
])
s="2011-christmas"
H("2011-12-23","Christmas 2011 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Dec 23”",s,close="1515 CT"),
 F("interest_rates","normal","“1600 CT – Regular CME Globex close for trade date Friday, Dec 23”",s,close="1600 CT"),
 F("fx","normal","“1600 CT – Regular CME Globex close for trade date Friday, Dec 23”",s,close="1600 CT"),
 F("energy","normal","“1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Dec 23”; “Exceptions: … All Crude, Heating Oil, RBOB & Nat Gas TAS contracts close early at 12:30 CT / 1330 ET”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","“1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Dec 23”; “Exceptions: Copper TAS – Early Close 1100 CT / 1200 ET; Silver TAS- Early Close 1125 CT / 1225 ET; Gold TAS – Early Close 1130 CT / 1230 ET”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close – per each product schedule for trade date Friday, Dec 23 … CBOT, KCBT and MGEX Grains”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close – per each product schedule … Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… Lumber”",s),
])
H("2011-12-26","Christmas Day 2011 observed (Monday, Dec 26)",[
 F("equity_index","closed","CME Group Equity Products / Monday, Dec 26 / “Christmas Day Observed – Globex closed”",s,open_="0500 CT Tuesday Dec 27"),
 F("interest_rates","closed","CME Group Interest Rate Products / Monday, Dec 26 / “Christmas Day Observed – Globex closed”",s,open_="0500 CT Tuesday Dec 27"),
 F("fx","closed","CME Group FX Products / Monday, Dec 26 / “Christmas Day Observed – Globex closed”",s,open_="0500 CT Tuesday Dec 27"),
 F("energy","closed","NYMEX, COMEX® and DME Products / Monday, Dec 26 / “1700 CT / 1800 ET – Regular CME Globex open for trade date Tuesday, Dec 27” (no Dec 26 trade date; the Monday evening open is normal)",s,open_="1700 CT / 1800 ET Monday Dec 26"),
 F("metals","closed","NYMEX, COMEX® and DME Products / Monday, Dec 26 / “1700 CT / 1800 ET – Regular CME Globex open for trade date Tuesday, Dec 27”",s,open_="1700 CT / 1800 ET Monday Dec 26"),
 F("grains","closed","Other CME Group Products / Monday, Dec 26 / “Christmas Day Observed – Globex closed”",s,open_="0930 CT Tuesday Dec 27"),
 F("livestock","closed","Other CME Group Products / Monday, Dec 26 / “Christmas Day Observed – Globex closed”",s,open_="0905 CT Tuesday Dec 27"),
 F("dairy","closed","Other CME Group Products / Monday, Dec 26 / “Christmas Day Observed – Globex closed”",s,open_="0905 CT Tuesday Dec 27"),
 F("lumber","closed","Other CME Group Products / Monday, Dec 26 / “Christmas Day Observed – Globex closed”",s,open_="0900 CT Tuesday Dec 27"),
])
H("2011-12-27","Day after Christmas 2011 (Tuesday, Dec 27) — late Globex open",[
 F("equity_index","late_open","Tuesday, Dec 27 / “0500 CT – CME Globex open for trade date Tuesday, Dec 27”; “1515 CT – Regular CME Globex close for trade date Tuesday, Dec 27”",s,open_="0500 CT",close="1515 CT"),
 F("interest_rates","late_open","Tuesday, Dec 27 / “0500 CT – CME Globex open for trade date Tuesday, Dec 27”; “1600 CT – Regular CME Globex close for trade date Tuesday, Dec 27”",s,open_="0500 CT",close="1600 CT"),
 F("fx","late_open","Tuesday, Dec 27 / “0500 CT – CME Globex open for trade date Tuesday, Dec 27”; “1600 CT – Regular CME Globex close for trade date Tuesday, Dec 27”",s,open_="0500 CT",close="1600 CT"),
 F("energy","normal","Tuesday, Dec 27 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Tuesday, Dec 27”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Monday Dec 26"),
 F("metals","normal","Tuesday, Dec 27 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Tuesday, Dec 27”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Monday Dec 26"),
 F("grains","late_open","Other CME Group Products / Tuesday, Dec 27 / “0930 CT CBOT, MGEX & KCBT Grain Futures & Options”; “Regular Close – per each product schedule for trade date Tuesday, Dec 27”",s,open_="0930 CT"),
 F("livestock","late_open","Other CME Group Products / Tuesday, Dec 27 / “0905 CT Livestock Futures & Options”",s,open_="0905 CT"),
 F("dairy","late_open","Other CME Group Products / Tuesday, Dec 27 / “0905 CT Dairy Futures & Options”",s,open_="0905 CT"),
 F("lumber","late_open","Other CME Group Products / Tuesday, Dec 27 / “0900 CT Lumber Futures & Options”",s,open_="0900 CT"),
])
s="2012-new-years"
H("2011-12-30","New Year's 2012 — New Year's Eve trade date (Friday, Dec 30 2011)",[
 F("equity_index","normal","Friday, Dec 30 / “1515 CT – Regular CME Globex close for trade date Friday, Dec 30”",s,close="1515 CT"),
 F("interest_rates","normal","Friday, Dec 30 / “1600 CT – Regular CME Globex close for trade date Friday, Dec 30”",s,close="1600 CT"),
 F("fx","normal","Friday, Dec 30 / “1600 CT – Regular CME Globex close for trade date Friday, Dec 30”",s,close="1600 CT"),
 F("energy","normal","Friday, Dec 30 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Dec 30”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","Friday, Dec 30 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Dec 30”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / Friday, Dec 30 / “Regular Close – Per each Product Schedule for trade date Friday, Dec 30 … CBOT, KCBT and MGEX Grain”",s),
 F("livestock","normal","Other CME Group Products / “… Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… Lumber”",s),
])
json.dump(HOL,open("part2.json","w"),indent=1,ensure_ascii=False)
print(len(HOL),"entries in part2")
