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

# ================= 2012 =================
s="2012-new-years"
H("2012-01-02","New Year's Day 2012 observed (Monday, Jan 2)",[
 F("equity_index","closed","CME Group Equity Products / Monday, Jan 2 / “New Years Observed – Globex closed”",s,open_="0500 CT Tuesday Jan 3"),
 F("interest_rates","closed","CME Group Interest Rate Products / Monday, Jan 2 / “New Years Observed – Globex closed”",s,open_="0500 CT Tuesday Jan 3"),
 F("fx","closed","CME Group FX Products / Monday, Jan 2 / “New Years Observed – Globex closed”",s,open_="0500 CT Tuesday Jan 3"),
 F("energy","closed","NYMEX, COMEX® and DME Products / Monday, Jan 2 / “1700 CT / 1800 ET – Regular CME Globex open for trade date Tuesday, Jan 3” (no Jan 2 trade date; the Monday evening open is normal)",s,open_="1700 CT / 1800 ET Monday Jan 2"),
 F("metals","closed","NYMEX, COMEX® and DME Products / Monday, Jan 2 / “1700 CT / 1800 ET – Regular CME Globex open for trade date Tuesday, Jan 3”",s,open_="1700 CT / 1800 ET Monday Jan 2"),
 F("grains","closed","Other CME Group Products / Monday, Jan 2 / “New Years Observed – Globex closed”",s,open_="0930 CT Tuesday Jan 3"),
 F("livestock","closed","Other CME Group Products / Monday, Jan 2 / “New Years Observed – Globex closed”",s,open_="0905 CT Tuesday Jan 3"),
 F("dairy","closed","Other CME Group Products / Monday, Jan 2 / “New Years Observed – Globex closed”",s,open_="0905 CT Tuesday Jan 3"),
 F("lumber","closed","Other CME Group Products / Monday, Jan 2 / “New Years Observed – Globex closed”",s,open_="0900 CT Tuesday Jan 3"),
])
H("2012-01-03","Day after New Year's 2012 (Tuesday, Jan 3) — late Globex open",[
 F("equity_index","late_open","Tuesday, Jan 3 / “0500 CT – CME Globex open for trade date Tuesday, Jan 3”; “1515 CT – Regular CME Globex close for trade date Tuesday, Jan 3”",s,open_="0500 CT",close="1515 CT"),
 F("interest_rates","late_open","Tuesday, Jan 3 / “0500 CT – CME Globex open for trade date Tuesday, Jan 3”; “1600 CT – Regular CME Globex close for trade date Tuesday, Jan 3”",s,open_="0500 CT",close="1600 CT"),
 F("fx","late_open","Tuesday, Jan 3 / “0500 CT – Regular CME Globex open for trade date Tuesday, Jan 3”; “1600 CT – Regular CME Globex close for trade date Tuesday, Jan 3”",s,open_="0500 CT",close="1600 CT"),
 F("energy","normal","Tuesday, Jan 3 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Tuesday, Jan 3”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Monday Jan 2"),
 F("metals","normal","Tuesday, Jan 3 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Tuesday, Jan 3”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Monday Jan 2"),
 F("grains","late_open","Other CME Group Products / Tuesday, Jan 3 / “0930 CT CBOT, MGEX & KCBT Futures & Options”; “Regular Close – per each product schedule for trade date Tuesday, Jan 3”",s,open_="0930 CT"),
 F("livestock","late_open","Other CME Group Products / Tuesday, Jan 3 / “0905 CT Livestock Futures & Options”",s,open_="0905 CT"),
 F("dairy","late_open","Other CME Group Products / Tuesday, Jan 3 / “0905 CT Dairy Futures & Options”",s,open_="0905 CT"),
 F("lumber","late_open","Other CME Group Products / Tuesday, Jan 3 / “0900 CT Lumber Futures & Options”",s,open_="0900 CT"),
])
s="2012-martin-luther-king"
H("2012-01-13","Martin Luther King Jr. Day 2012 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Jan 13”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for trade date Friday, Jan 13”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Jan 13”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET –Regular CME Globex close for trade date Friday, Jan 13”; “TAS/TAM Products - Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET –Regular CME Globex close for trade date Friday, Jan 13”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Jan 13 for: … CBOT, KCBT and MGEX Grains”; “Note: Modified grain pre-opening between 14:30 – 15:15”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… Lumber”",s),
])
H("2012-01-16","Martin Luther King Jr. Day 2012 (Monday)",[
 F("equity_index","modified","Monday, Jan 16 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, Jan 16 / “1200 CT –Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("fx","modified","Monday, Jan 16 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, Jan 16 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, Jan 16 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, Jan 15 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","closed","Sunday, Jan 15 Exceptions: “Livestock will remain closed until its scheduled opening 0905 CT on Tuesday”",s,open_="0905 CT Tuesday Jan 17"),
 F("lumber","closed","Sunday, Jan 15 Exceptions: “Lumber will remain closed until its scheduled opening of 0900 CT on Tuesday”",s,open_="0900 CT Tuesday Jan 17"),
 F("dairy","late_open","Sunday, Jan 15 Exceptions: “Dairy, Crude Palm Oil, GSCI, and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])
s="2012-presidents-day"
H("2012-02-17","Presidents' Day 2012 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Feb 17”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for trade date Friday, Feb 17”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Feb 17”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Feb 17”; “TAS/TAM Products - Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Feb 17”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Feb 17 for: … CBOT, KCBT and MGEX Grains”; “Note: Modified grain & juice pre-opening between 14:30 – 15:15”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close … Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… Lumber”",s),
])
H("2012-02-20","Presidents' Day 2012 (Monday)",[
 F("equity_index","modified","Monday, Feb 20 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, Feb 20 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("fx","modified","Monday, Feb 20 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, Feb 20 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, Feb 20 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","Sunday, Feb 19 Exceptions: “CBOT, KCBT and MGEX Grain Products and CBOT Ethanol will remain closed until 1800 CT on Monday”",s,open_="1800 CT"),
 F("livestock","closed","Sunday, Feb 19 Exceptions: “Livestock will remain closed until its scheduled opening 0905 CT on Tuesday”",s,open_="0905 CT Tuesday Feb 21"),
 F("lumber","closed","Sunday, Feb 19 Exceptions: “Lumber will remain closed until its scheduled opening of 0900 CT on Tuesday”",s,open_="0900 CT Tuesday Feb 21"),
 F("dairy","late_open","Sunday, Feb 19 Exceptions: “Dairy, Crude Palm Oil, GSCI, and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])
s="2012-good-friday"
H("2012-04-05","Good Friday 2012 — preceding trade date (Thursday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Thursday, Apr 5”; “1530 CT – Regular CME Globex open for trade date Friday Apr 6”",s,close="1515 CT",open_="1530 CT"),
 F("interest_rates","normal","“1600 CT – Regular CME Globex close for trade date Thursday, Apr 5”; “1700 CT – Regular CME Globex open for trade date Friday, Apr 6”",s,close="1600 CT",open_="1700 CT"),
 F("fx","normal","“1600 CT – Regular CME Globex close for trade date Thursday, Apr 5”; “1700 CT – Regular CME Globex open for trade date Friday, Apr 6”",s,close="1600 CT",open_="1700 CT"),
 F("energy","normal","NYMEX & COMEX® and DME Products / “1615 CT / 1715 ET - Regular CME Globex close for trade date Thursday, Apr 5”; “TAS/TAM Products - Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX & COMEX® and DME Products / “1615 CT / 1715 ET - Regular CME Globex close for trade date Thursday, Apr 5”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Thursday, Apr 5 for: • CBOT, KCBT and MGEX Grains …”",s),
 F("livestock","early_close","Other CME Group Products / Thursday, Apr 5 / “1355 CT – Early Close for Lumber, Dairy and Livestock”",s,close="1355 CT"),
 F("dairy","early_close","Other CME Group Products / Thursday, Apr 5 / “1355 CT – Early Close for Lumber, Dairy and Livestock”",s,close="1355 CT"),
 F("lumber","early_close","Other CME Group Products / Thursday, Apr 5 / “1355 CT – Early Close for Lumber, Dairy and Livestock”",s,close="1355 CT"),
])
H("2012-04-06","Good Friday 2012 (Friday)",[
 F("equity_index","early_close","CME Group Equity Products / Friday, Apr 6 / “0815 CT - Early CME Globex close for trade date Friday Apr 6”",s,close="0815 CT"),
 F("interest_rates","early_close","CME Group Interest Rate Products / Friday, Apr 6 / “1015 CT - Early CME Globex close for trade date Friday Apr 6”",s,close="1015 CT"),
 F("fx","early_close","CME Group FX Products / Friday, Apr 6 / “1015 CT - Early CME Globex close for trade date Friday Apr 6”",s,close="1015 CT"),
 F("energy","closed","NYMEX & COMEX® and DME Products / Friday, Apr 6 / “No CME Globex Trading on Good Friday”",s,open_="1700 CT / 1800 ET Sunday Apr 8"),
 F("metals","closed","NYMEX & COMEX® and DME Products / Friday, Apr 6 / “No CME Globex Trading on Good Friday”",s,open_="1700 CT / 1800 ET Sunday Apr 8"),
 F("grains","closed","Other CME Group Products / Friday, Apr 6 / “No CME Globex Trading on Good Friday”; Sunday, Apr 8 “1800 CT – Regular CME Globex open for CBOT, KCBT and MGEX Grain Products & CBOT Ethanol for Trade date Monday April 9”",s,open_="1800 CT Sunday Apr 8"),
 F("livestock","closed","Other CME Group Products / Friday, Apr 6 / “No CME Globex Trading on Good Friday”; “Exceptions: Livestock & Lumber will remain closed until their regularly scheduled open on Monday”",s,open_="regularly scheduled open Monday Apr 9"),
 F("lumber","closed","Other CME Group Products / “Exceptions: Livestock & Lumber will remain closed until their regularly scheduled open on Monday”",s,open_="regularly scheduled open Monday Apr 9"),
 F("dairy","closed","Other CME Group Products / Friday, Apr 6 / “No CME Globex Trading on Good Friday”",s),
])
s="2012-memorial-day"
H("2012-05-25","Memorial Day 2012 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, May 25”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for trade date Friday, May 25”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, May 25”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, May 25”; “TAS/TAM Products - Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, May 25”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","CBOT, KCBT and MGEX Grain Products on CME Globex (new standalone section from the May-2012 extended grain hours) / Friday, May 25 / “1400 CT – Regular CME Globex close for trade date Friday, May 25”; “Note: Modified grain pre-opening between 14:30 CT – 15:15 CT”",s,close="1400 CT"),
 F("livestock","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, May 25 for: • Livestock”",s),
 F("dairy","normal","Other CME Group Products / “… • Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… • Lumber”",s),
])
H("2012-05-28","Memorial Day 2012 (Monday)",[
 F("equity_index","modified","Monday, May 28 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, May 28 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("fx","modified","Monday, May 28 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, May 28 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, May 28 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","CBOT, KCBT and MGEX Grain Products / Sunday, May 27 “1600 CT - Products will be in a Pre-open until 1900 CT on Monday, May 28”; Monday, May 28 “1900 CT – CME Globex open for trade date Tuesday, May 29”",s,open_="1900 CT (Mon May 28, for trade date Tue May 29)"),
 F("livestock","closed","Other CME Group Products / Sunday, May 27 Exceptions: “Livestock will remain closed until its scheduled opening 0905 CT on Tuesday”",s,open_="0905 CT Tuesday May 29"),
 F("lumber","closed","Other CME Group Products / Sunday, May 27 Exceptions: “Lumber will remain closed until its scheduled opening of 0900 CT on Tuesday”",s,open_="0900 CT Tuesday May 29"),
 F("dairy","late_open","Other CME Group Products / Sunday, May 27 Exceptions: “Dairy, Crude Palm Oil, GSCI, and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])
s="2012-4th-of-july"
H("2012-07-03","Independence Day 2012 — preceding trade date (Tuesday, Jul 3)",[
 F("equity_index","early_close","CME Group Equity Products / Tuesday, July 3 / “1215 CT –Early CME Globex close for trade date Tuesday, July 3”; “1530 CT –Regular CME Globex open for trade date Thursday, July 5”",s,close="1215 CT",open_="1530 CT"),
 F("interest_rates","normal","CME Group Interest Rate Products / Tuesday, July 3 / “1600 CT – Regular CME Globex close for trade date Tuesday, July 3”; “1700 CT – Regular CME Globex open for trade date Thursday, July 5”",s,close="1600 CT",open_="1700 CT"),
 F("fx","normal","CME Group FX Products / Tuesday, July 3 / “1600 CT – Regular CME Globex close for trade date Tuesday, July 3”; “1700 CT – Regular CME Globex open for trade date Thursday, July 5”",s,close="1600 CT",open_="1700 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / Tuesday, July 3 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Tuesday, July 3”; “1700 CT / 1800 ET – Regular CME Globex open for trade date Thursday, July 5”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / Tuesday, July 3 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Tuesday, July 3”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("grains","early_close","CBOT, KCBT and MGEX Grain Products / Tuesday, July 3 / “1200 CT – Early CME Globex close for trade date Tuesday, July 3”; “1215 CT – Early CME Globex close for MGEX grain products for trade date Tuesday, July 3”; “1645 CT - Products will be in a Pre-open until 0930 CT Thursday, July 5”",s,close="1200 CT CBOT/KCBT; 1215 CT MGEX"),
 F("livestock","normal","Other CME Group Products / Tuesday, July 3 / “Regular Close - Per each product schedule for trade date Tuesday, July 3 for: • Livestock …”",s),
 F("dairy","normal","Other CME Group Products / “… • Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… • Lumber”",s),
])
H("2012-07-04","Independence Day 2012 (Wednesday)",[
 F("equity_index","modified","Wednesday, July 4 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Wednesday, July 4 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("fx","modified","Wednesday, July 4 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Wednesday, July 4 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Wednesday, July 4 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","closed","CBOT, KCBT and MGEX Grain Products / Tuesday, July 3 “1645 CT - Products will be in a Pre-open until 0930 CT Thursday, July 5”; Thursday, July 5 “0930 CT – CME Globex open for Thursday, July 5”",s,open_="0930 CT Thursday July 5"),
 F("livestock","closed","Other CME Group Products / Exceptions: “Livestock will remain closed until its scheduled opening 0905 CT on Thursday”",s,open_="0905 CT Thursday July 5"),
 F("lumber","closed","Other CME Group Products / Exceptions: “Lumber will remain closed until its scheduled opening of 0900 CT on Thursday”",s,open_="0900 CT Thursday July 5"),
 F("dairy","late_open","Other CME Group Products / Exceptions: “Dairy, Crude Palm Oil, GSCI, and Weather products will remain closed until 1700 CT on Wednesday”",s,open_="1700 CT"),
])
H("2012-07-05","Day after Independence Day 2012 (Thursday, Jul 5)",[
 F("equity_index","normal","Thursday, July 5 / “1515 CT – Regular CME Globex close for trade date Thursday, July 5”",s,close="1515 CT"),
 F("interest_rates","normal","Thursday, July 5 / “1600 CT – Regular CME Globex close for trade date Thursday, July 5”",s,close="1600 CT"),
 F("fx","normal","Thursday, July 5 / “1600 CT – Regular CME Globex close for trade date Thursday, July 5”",s,close="1600 CT"),
 F("energy","normal","Thursday, July 5 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Thursday, July 5”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","Thursday, July 5 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Thursday, July 5”",s,close="1615 CT / 1715 ET"),
 F("grains","late_open","CBOT, KCBT and MGEX Grain Products / Thursday, July 5 / “0930 CT – CME Globex open for Thursday, July 5”; “Per each product schedule – Regular CME Globex close for trade date Thursday, July 5”",s,open_="0930 CT"),
 F("livestock","late_open","Other CME Group Products / “Livestock will remain closed until its scheduled opening 0905 CT on Thursday”",s,open_="0905 CT"),
 F("lumber","late_open","Other CME Group Products / “Lumber will remain closed until its scheduled opening of 0900 CT on Thursday”",s,open_="0900 CT"),
])
s="2012-labor-day"
H("2012-08-31","Labor Day 2012 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Aug 31”",s,close="1515 CT"),
 F("interest_rates","early_close","“1515 CT – Early CME Globex close for trade date Friday, Aug 31”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Aug 31”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1515 CT / 1615 ET – Early CME Globex Close- Environmental Products”; “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Aug 31”; “TAS/TAM Products – Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET (Environmental Products 1515 CT / 1615 ET)"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Aug 31”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","CBOT, KCBT, MGEX Grain & Agricultural Products / Friday, Aug 31 / “Regular Close - Per each product schedule for trade date Friday, Aug 31”; “Note: Modified pre-opening between 14:30 CT – 15:15 CT”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Aug 31 for: • Livestock …”",s),
 F("dairy","normal","Other CME Group Products / “… • Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… • Lumber”",s),
])
H("2012-09-03","Labor Day 2012 (Monday)",[
 F("equity_index","modified","Monday, Sep 3 / “1030 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Monday, Sep 3 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("fx","modified","Monday, Sep 3 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Monday, Sep 3 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Monday, Sep 3 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","late_open","CBOT, KCBT, MGEX Grain & Agricultural Products / Sunday, Sep 2 “1600 CT - Products will be in a Pre-open until their respective openings on Monday or Tuesday”; Monday, Sep 3 “1900 CT – CME Globex Grain open for trade date Tuesday, Sep 4”",s,open_="1900 CT (Mon Sep 3, for trade date Tue Sep 4)"),
 F("livestock","closed","Other CME Group Products / Exceptions: “Livestock will remain closed until its scheduled opening 0905 CT on Tuesday”",s,open_="0905 CT Tuesday Sep 4"),
 F("lumber","closed","Other CME Group Products / Exceptions: “Lumber will remain closed until its scheduled opening of 0900 CT on Tuesday”",s,open_="0900 CT Tuesday Sep 4"),
 F("dairy","late_open","Other CME Group Products / Exceptions: “Dairy, Crude Palm Oil, GSCI, and Weather products will remain closed until 1700 CT on Monday”",s,open_="1700 CT"),
])
s="2012-columbus-day"
H("2012-10-05","Columbus Day 2012 — preceding trade date (Friday)",[
 F("equity_index","normal","“1515 CT – Regular CME Globex close for trade date Friday, Oct 5”",s,close="1515 CT"),
 F("interest_rates","early_close","CME Group Interest Products / “1515 CT – Early CME Globex close for trade date Friday, Oct 5”",s,close="1515 CT"),
 F("fx","early_close","“1515 CT – Early CME Globex close for trade date Friday, Oct 5”",s,close="1515 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Oct 5”; “TAS/TAM Products - Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / “1615 CT / 1715 ET – Regular CME Globex close for trade date Friday, Oct 5”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","CBOT, KCBT, MGEX Grain & Agricultural Products / Friday, Oct 5 / “Regular Close - Per each product schedule for trade date Friday, Oct 5”; “Note: Modified grain pre-opening between 14:30 CT – 15:15 CT”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Friday, Oct 5 for: • Livestock …”",s),
 F("dairy","normal","Other CME Group Products / “… • Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… • Lumber”",s),
])
H("2012-10-08","Columbus Day 2012 (Monday) — CME Globex traded a normal session",[
 F("equity_index","normal","Monday, Oct 8 / “1515 CT – Regular CME Globex close for trade date Monday, Oct 8”",s,close="1515 CT",open_="1700 CT Sunday Oct 7"),
 F("interest_rates","normal","Monday, Oct 8 / “1600 CT – Regular CME Globex close for trade date Monday, Oct 8”",s,close="1600 CT",open_="1700 CT Sunday Oct 7"),
 F("fx","normal","Monday, Oct 8 / “1600 CT – Regular CME Globex close for trade date Monday, Oct 8”",s,close="1600 CT",open_="1700 CT Sunday Oct 7"),
 F("energy","normal","Monday, Oct 8 / “1615 CT / 1715 ET – Regular CME Globex Close for trade date Oct 8”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Sunday Oct 7"),
 F("metals","normal","Monday, Oct 8 / “1615 CT / 1715 ET – Regular CME Globex Close for trade date Oct 8”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Sunday Oct 7"),
 F("grains","normal","CBOT, KCBT, MGEX Grain & Agricultural Products / Sunday, Oct 7 “1700 CT - Regular CME Globex open for trade date Monday, Oct 8”; Monday, Oct 8 “Regular Trading Hours - Per each product schedule for trade date Monday, Oct 8”",s,open_="1700 CT Sunday Oct 7"),
 F("livestock","normal","Other CME Group Products / Sunday, Oct 7 “Exceptions: Livestock & Lumber will remain closed until their regularly scheduled open on Monday”; Monday “Regular Close - Per each product schedule for trade date Monday, Oct 8”",s),
 F("lumber","normal","Other CME Group Products / Sunday, Oct 7 “Exceptions: Livestock & Lumber will remain closed until their regularly scheduled open on Monday”",s),
])
s="2012-veterans-day"
H("2012-11-12","Veterans Day 2012 observed (Monday, Nov 12) — CME Globex traded a normal session",[
 F("equity_index","normal","Monday, Nov 12 / “1515 CT – Regular CME Globex close for trade date Monday, Nov 12”; Sunday, Nov 11 “1700 CT – Regular CME Globex open for trade date of Monday, Nov 12”",s,close="1515 CT",open_="1700 CT Sunday Nov 11"),
 F("interest_rates","normal","Monday, Nov 12 / “1600 CT – Regular CME Globex close for trade date Monday, Nov 12”",s,close="1600 CT",open_="1700 CT Sunday Nov 11"),
 F("fx","normal","Monday, Nov 12 / “1600 CT – Regular CME Globex close for trade date Monday, Nov 12”",s,close="1600 CT",open_="1700 CT Sunday Nov 11"),
 F("energy","normal","Monday, Nov 12 / “1615 CT / 1715 ET – Regular CME Globex close for trade date of Monday, Nov 12”; “TAS/TAM Products - Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Sunday Nov 11"),
 F("metals","normal","Monday, Nov 12 / “1615 CT / 1715 ET – Regular CME Globex close for trade date of Monday, Nov 12”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Sunday Nov 11"),
 F("grains","normal","CBOT, KCBT, MGEX Grain & Agricultural Products / Sunday, Nov 11 “1700 CT - Regular CME Globex open for trade date Monday, Nov 12”; Monday “Regular Trading Hours - Per each product schedule for trade date Monday, Nov 12”",s,open_="1700 CT Sunday Nov 11"),
 F("livestock","normal","Other CME Group Products / Monday, Nov 12 “Regular Trading Hours - Per each product schedule for trade date Monday, Nov 12”",s),
])
s="2012-thanksgiving"
H("2012-11-21","Thanksgiving 2012 — preceding trade date (Wednesday)",[
 F("equity_index","normal","CME Group Equity Products / Wednesday, Nov 21 / “1615 CT – Regular CME Globex close for trade date Wednesday, Nov 21”; “1700 CT – Regular CME Globex open for trade date Friday, Nov 23”; “Note: USD- Ibovespa Futures will remain closed until their 0515 open on Thursday, Nov 22”",s,close="1615 CT",open_="1700 CT"),
 F("interest_rates","normal","Wednesday, Nov 21 / “1600 CT – Regular CME Globex close for trade date Wednesday, Nov 21”; “1700 CT – Regular CME Globex open for trade date Friday, Nov 23”",s,close="1600 CT",open_="1700 CT"),
 F("fx","normal","Wednesday, Nov 21 / “1600 CT – Regular CME Globex close for trade date Wednesday, Nov 21”; “1700 CT – Regular CME Globex open for trade date Friday, Nov 23”",s,close="1600 CT",open_="1700 CT"),
 F("energy","normal","Wednesday, Nov 21 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Wednesday, Nov 21”; “1700 CT / 1800 ET – Regular CME Globex open for trade date Friday, Nov 23”; “Exception: NYMEX Softs TAS (CJT, KTT, TTT, and YOT) will remain closed until their regular open on Sunday, November 25”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("metals","normal","Wednesday, Nov 21 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Wednesday, Nov 21”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET"),
 F("grains","normal","CBOT, KCBT, MGEX Grain & Agricultural Products / Wednesday, Nov 21 / “Regular Close - Per each product schedule for trade date Wednesday, Nov 21”; “Note: Modified grain pre-opening between 14:30 CT – 16:00 CT”; “1645 CT - Products will be in a Pre-open until 0930 CT Friday, Nov 23”",s),
 F("livestock","normal","Other CME Group Products / “Regular Close - Per each product schedule for trade date Wednesday, Nov 21 for: • Livestock …”",s),
 F("lumber","normal","Other CME Group Products / “… • Lumber”",s),
 F("dairy","normal","Other CME Group Products / “… • Dairy”; Exceptions “Dairy products will remain closed until their regularly scheduled open on Sunday, Nov 25”",s),
])
H("2012-11-22","Thanksgiving Day 2012 (Thursday)",[
 F("equity_index","modified","Thursday, Nov 22 / “1030 CT - Trading halt”; “1700 CT – Equity products resume trading”; “Note: USD- Ibovespa Futures will remain closed until their 0515 open on Friday, Nov 23”",s,close="1030 CT",open_="1700 CT"),
 F("interest_rates","modified","Thursday, Nov 22 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("fx","modified","Thursday, Nov 22 / “1200 CT – Trading halt”; “1700 CT – Halted products resume trading”",s,close="1200 CT",open_="1700 CT"),
 F("energy","modified","Thursday, Nov 22 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("metals","modified","Thursday, Nov 22 / “1215 CT / 1315 ET – Trading halt”; “1700 CT / 1800 ET – Halted products resume trading”",s,close="1215 CT / 1315 ET",open_="1700 CT / 1800 ET"),
 F("grains","closed","CBOT, KCBT, MGEX Grain & Agricultural Products / Wednesday, Nov 21 “1645 CT - Products will be in a Pre-open until 0930 CT Friday, Nov 23”",s,open_="0930 CT Friday Nov 23"),
 F("livestock","late_open","Other CME Group Products / Exceptions: “Livestock, GSCI, Lumber, Crude Palm Oil and Weather will remain closed until their open at 1700 CT on Thursday Nov 22.”",s,open_="1700 CT"),
 F("lumber","late_open","Other CME Group Products / Exceptions: “Livestock, GSCI, Lumber, Crude Palm Oil and Weather will remain closed until their open at 1700 CT on Thursday Nov 22.”",s,open_="1700 CT"),
 F("dairy","closed","Other CME Group Products / Exceptions: “Dairy products will remain closed until their regularly scheduled open on Sunday, Nov 25”",s,open_="regularly scheduled open Sunday Nov 25"),
])
H("2012-11-23","Day after Thanksgiving 2012 (Friday)",[
 F("equity_index","early_close","Friday, Nov 23 / “1215 CT – Early CME Globex close for trade date Friday, Nov 23”",s,close="1215 CT"),
 F("interest_rates","early_close","Friday, Nov 23 / “1215 CT – Early CME Globex close for trade date Friday, Nov 23”",s,close="1215 CT"),
 F("fx","early_close","Friday, Nov 23 / “1215 CT – Early CME Globex close for trade date Friday, Nov 23”",s,close="1215 CT"),
 F("energy","early_close","Friday, Nov 23 / “1245 CT / 1345 ET – Early CME Globex Close for trade date Friday, Nov 23”; “Exceptions: … All Crude, Heating Oil, RBOB & Nat Gas TAS contracts close early at 12:30 CT / 1330 ET”",s,close="1245 CT / 1345 ET"),
 F("metals","early_close","Friday, Nov 23 / “1245 CT / 1345 ET – Early CME Globex Close for trade date Friday, Nov 23”; “Exceptions: • Copper TAS – Early Close 1100 CT / 1200 ET • Silver TAS- Early Close 1125 CT / 1225 ET • Gold TAS – Early Close 1130 CT / 1230 ET”",s,close="1245 CT / 1345 ET"),
 F("grains","early_close","CBOT, KCBT, MGEX Grain & Agricultural Products / Friday, Nov 23 / “0930 CT– CME Globex Grain open for trade date Friday, Nov 23”; “1200 CT– Early CBOT & KCBT close for trade date Friday, Nov 23”; “1215 CT– Early MGEX close”; “1230 CT– Early CBOT Mini – Sized Grain close”",s,open_="0930 CT",close="1200 CT CBOT/KCBT; 1215 CT MGEX; 1230 CT CBOT mini-sized grain"),
 F("livestock","early_close","Other CME Group Products / Friday, Nov 23 / “1215 CT – Early CME Globex close for CME Livestock Futures & Options, Real Estate for trade date Friday Nov 23”",s,close="1215 CT"),
 F("lumber","early_close","Other CME Group Products / Friday, Nov 23 / “1200 CT – Early CME Globex close for Forestry, Weather, Dow Jones UBS ER & GSCI for trade date Friday, Nov 23”; “1202 CT – Early CME Globex close for CME Lumber Options for trade date Friday, Nov 23”",s,close="1200 CT Forestry / 1202 CT Lumber options"),
 F("dairy","closed","Other CME Group Products / Exceptions: “Dairy products will remain closed until their regularly scheduled open on Sunday, Nov 25”",s),
])
s="2012-christmas"
H("2012-12-24","Christmas Eve 2012 (Monday, Dec 24)",[
 F("equity_index","early_close","CME Group Equity Products / Monday, Dec 24 / “1215 CT – Early CME Globex close for trade date Monday, Dec 24”",s,close="1215 CT"),
 F("interest_rates","early_close","CME Group Interest Rate Products / Monday, Dec 24 / “1215 CT – Early CME Globex close for trade date Monday, Dec 24”",s,close="1215 CT"),
 F("fx","early_close","CME Group FX Products / Monday, Dec 24 / “1215 CT – Early CME Globex close for trade date Monday, Dec 24”",s,close="1215 CT"),
 F("energy","early_close","NYMEX, COMEX® and DME Products / Monday, Dec 24 / “1245 CT / 1345 ET – Early CME Globex Close for trade date Monday, Dec 24”; “Exceptions: … All Crude, Heating Oil, RBOB, Nat Gas & Cotton TAS contracts close early at 12:30 CT / 1330 ET”",s,close="1245 CT / 1345 ET"),
 F("metals","early_close","NYMEX, COMEX® and DME Products / Monday, Dec 24 / “1245 CT / 1345 ET – Early CME Globex Close for trade date Monday, Dec 24”; “Exceptions: Copper TAS – Early Close 1100 CT / 1200 ET; Silver TAS- Early Close 1125 CT / 1225 ET; Gold TAS – Early Close 1130 CT / 1230 ET”",s,close="1245 CT / 1345 ET"),
 F("grains","early_close","CBOT, KCBT, MGEX Grain & Agricultural Products / Monday, Dec 24 / “1200 CT – Early CBOT & KCBT close for trade date Monday, Dec 24”; “1215 CT – Early MGEX close”; “1230 CT – Early CBOT Mini – Sized Grain close”",s,close="1200 CT CBOT/KCBT; 1215 CT MGEX; 1230 CT CBOT mini-sized grain"),
 F("livestock","early_close","Other CME Group Products / Monday, Dec 24 / “1215 CT – Early CME Globex close for CME Livestock Futures & Options, Real Estate for trade date Monday, Dec 24”",s,close="1215 CT"),
 F("dairy","early_close","Other CME Group Products / Monday, Dec 24 / “1200 CT – Early CME Globex close for Forestry, Dairy, Crude Palm Oil, Weather, Dow Jones UBS ER and GSCI for trade date Monday, Dec 24”",s,close="1200 CT"),
 F("lumber","early_close","Other CME Group Products / Monday, Dec 24 / “1200 CT – Early CME Globex close for Forestry …”; “1202 CT – Early CME Globex close for CME Lumber Options for trade date Monday, Dec 24”",s,close="1200 CT Forestry / 1202 CT Lumber options"),
])
H("2012-12-25","Christmas Day 2012 (Tuesday, Dec 25)",[
 F("equity_index","closed","CME Group Equity Products / Tuesday, Dec 25 / “Christmas Day Observed – Globex closed”",s,open_="0500 CT Wednesday Dec 26"),
 F("interest_rates","closed","CME Group Interest Rate Products / Tuesday, Dec 25 / “Christmas Day Observed – Globex closed”",s,open_="0500 CT Wednesday Dec 26"),
 F("fx","closed","CME Group FX Products / Tuesday, Dec 25 / “Christmas Day Observed – Globex closed”",s,open_="0500 CT Wednesday Dec 26"),
 F("energy","closed","NYMEX, COMEX® and DME Products / Tuesday, Dec 25 / “Christmas Day Observed – Globex closed”; “1700 CT / 1800 ET – Regular CME Globex open for trade date Wednesday, Dec 26”",s,open_="1700 CT / 1800 ET Tuesday Dec 25"),
 F("metals","closed","NYMEX, COMEX® and DME Products / Tuesday, Dec 25 / “Christmas Day Observed – Globex closed”; “1700 CT / 1800 ET – Regular CME Globex open for trade date Wednesday, Dec 26”",s,open_="1700 CT / 1800 ET Tuesday Dec 25"),
 F("grains","closed","CBOT, KCBT, MGEX Grain & Agricultural Products / Tuesday, Dec 25 / “Christmas Day Observed – Globex closed”",s,open_="0930 CT Wednesday Dec 26"),
 F("livestock","closed","Other CME Group Products / Tuesday, Dec 25 / “Christmas Day Observed – Globex closed”",s,open_="0905 CT Wednesday Dec 26"),
 F("dairy","closed","Other CME Group Products / Tuesday, Dec 25 / “Christmas Day Observed – Globex closed”",s,open_="0905 CT Wednesday Dec 26"),
 F("lumber","closed","Other CME Group Products / Tuesday, Dec 25 / “Christmas Day Observed – Globex closed”",s,open_="0900 CT Wednesday Dec 26"),
])
H("2012-12-26","Day after Christmas 2012 (Wednesday, Dec 26) — late Globex open",[
 F("equity_index","late_open","Wednesday, Dec 26 / “0500 CT – CME Globex open for trade date Wednesday, Dec 26”; “0515 CT – USD Ibovespa futures open for trade date Wednesday, Dec 26”; “1615 CT – Regular CME Globex close for trade date Wednesday, Dec 26” (as printed)",s,open_="0500 CT",close="1615 CT"),
 F("interest_rates","late_open","Wednesday, Dec 26 / “0500 CT – CME Globex open for trade date Wednesday, Dec 26”; “1600 CT – Regular CME Globex close for trade date Wednesday, Dec 26”",s,open_="0500 CT",close="1600 CT"),
 F("fx","late_open","Wednesday, Dec 26 / “0500 CT – CME Globex open for trade date Wednesday, Dec 26”; “1600 CT – Regular CME Globex close for trade date Wednesday, Dec 26”",s,open_="0500 CT",close="1600 CT"),
 F("energy","normal","Wednesday, Dec 26 / “1615 CT / 1715 ET –Regular CME Globex close for trade date Wednesday, Dec 26”; “TAS/TAM Products - Regular Close - Per each product schedule”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Tuesday Dec 25"),
 F("metals","normal","Wednesday, Dec 26 / “1615 CT / 1715 ET –Regular CME Globex close for trade date Wednesday, Dec 26”",s,close="1615 CT / 1715 ET",open_="1700 CT / 1800 ET Tuesday Dec 25"),
 F("grains","late_open","CBOT, KCBT, MGEX Grain & Agricultural Products / Wednesday, Dec 26 / “0700 CT– MGEX Apple Juice open for trade date Wednesday, Dec 26”; “0930 CT – CME Globex Grain open for trade date Wednesday, Dec 26”; “Regular Close – Per each product schedule”",s,open_="0930 CT (MGEX Apple Juice 0700 CT)"),
 F("livestock","late_open","Other CME Group Products / Wednesday, Dec 26 / “0905 CT Livestock Futures & Options”",s,open_="0905 CT"),
 F("dairy","late_open","Other CME Group Products / Wednesday, Dec 26 / “0905 CT Dairy Futures & Options”",s,open_="0905 CT"),
 F("lumber","late_open","Other CME Group Products / Wednesday, Dec 26 / “0900 CT Lumber Futures & Options”",s,open_="0900 CT"),
])
s="2013-new-years"
H("2012-12-31","New Year's Eve 2012 (Monday, Dec 31) — documented in CME's New Year's 2013 schedule",[
 F("equity_index","normal","CME Group Equity Products / Monday, Dec 31 / “1515 CT – Regular CME Globex close for trade date Monday, Dec 31”",s,close="1515 CT"),
 F("interest_rates","normal","CME Group Interest Rate Products / Monday, Dec 31 / “1600 CT – Regular CME Globex close for trade date Monday, Dec 31”",s,close="1600 CT"),
 F("fx","normal","CME Group FX Products / Monday, Dec 31 / “1600 CT – Regular CME Globex close for trade date Monday, Dec 31”",s,close="1600 CT"),
 F("energy","normal","NYMEX, COMEX® and DME Products / Monday, Dec 31 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Monday, Dec 31”",s,close="1615 CT / 1715 ET"),
 F("metals","normal","NYMEX, COMEX® and DME Products / Monday, Dec 31 / “1615 CT / 1715 ET – Regular CME Globex close for trade date Monday, Dec 31”",s,close="1615 CT / 1715 ET"),
 F("grains","normal","CBOT, KCBT, MGEX Grain & Agricultural Products / Monday, Dec 31 / “Regular Close – Per each product schedule for trade date Monday, Dec 31”; “Note: Modified grain pre-opening between 14:30 CT – 16:00 CT”",s),
 F("livestock","normal","Other CME Group Products / Monday, Dec 31 / “Regular Close – Per each Product Schedule for trade date Monday, Dec 31 • Livestock …”",s),
 F("dairy","normal","Other CME Group Products / “… • Dairy”",s),
 F("lumber","normal","Other CME Group Products / “… • Lumber”",s),
])
json.dump(HOL,open("part3.json","w"),indent=1,ensure_ascii=False)
print(len(HOL),"entries in part3")
