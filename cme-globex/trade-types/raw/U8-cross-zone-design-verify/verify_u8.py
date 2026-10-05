import datetime as dt
from zoneinfo import ZoneInfo
CHI=ZoneInfo("America/Chicago")
Z={n:ZoneInfo(n) for n in ["Europe/London","Asia/Singapore","Asia/Shanghai","Asia/Hong_Kong","Asia/Tokyo","America/New_York"]}
def delta(day,z):
    noon=dt.datetime.combine(day,dt.time(12,0),tzinfo=CHI)
    return (noon.astimezone(z).utcoffset()-noon.utcoffset()).total_seconds()/3600
days=[dt.date(2010,1,1)+dt.timedelta(days=i) for i in range((dt.date(2030,12,31)-dt.date(2010,1,1)).days+1)]
print("Q1 states 2010-2030:")
for n,z in Z.items(): print("  ",n,sorted({delta(d,z) for d in days}))
# independent: derive chicago clock for each shape via absolute UTC instant, NOT via delta arithmetic
def chi_clock(day,z,hh,mm):
    # local marker time in zone z on the venue's *foreign* civil day corresponding to chicago day
    # build the instant: foreign local hh:mm on the same UTC-ish date; use chicago noon as anchor to find the foreign date
    noon=dt.datetime.combine(day,dt.time(12,0),tzinfo=CHI)
    fdate=noon.astimezone(z).date()
    inst=dt.datetime.combine(fdate,dt.time(hh,mm),tzinfo=z)
    c=inst.astimezone(CHI)
    return c.strftime("%H:%M"), (c.date()-day).days
SH=[("CLL/BZL/HOL/RBL","Europe/London",16,30),("CLS/BZS","Asia/Singapore",16,30),
    ("CLC","Asia/Shanghai",15,0),("GCD","Europe/London",15,2),("HGF","Europe/London",12,35),
    ("DVT/E3T","Europe/London",16,30),("FTC","Asia/Hong_Kong",16,0),
    ("Nikkei BTIC","Asia/Tokyo",15,30),("crypto London","Europe/London",16,0),
    ("crypto APAC","Asia/Hong_Kong",16,0),("6EB start","Europe/London",15,40),
    ("6EB end","Europe/London",16,30),("NY control","America/New_York",16,0)]
wd=[d for d in (dt.date(2026,1,1)+dt.timedelta(days=i) for i in range(365)) if d.weekday()<5]
print("total 2026 weekdays:",len(wd))
print("Q2/Q3 (independent absolute-instant derivation):")
for lab,zn,hh,mm in SH:
    b={}
    for d in wd:
        k=chi_clock(d,Z[zn],hh,mm); b[k]=b.get(k,0)+1
    print("  %-18s %-16s %02d:%02d -> %s"%(lab,zn,hh,mm,", ".join("%s d%+d x%d"%(k[0],k[1],v) for k,v in sorted(b.items()))))
print("2026 misalign UK/US calendar days:", sum(1 for d in (dt.date(2026,1,1)+dt.timedelta(days=i) for i in range(365)) if delta(d,Z["Europe/London"])!=6.0))
print("2026 misalign WEEKdays:", sum(1 for d in wd if delta(d,Z["Europe/London"])!=6.0))
# exact transition instants
def transitions(z,y):
    out=[];prev=None
    t=dt.datetime(y,1,1,tzinfo=dt.timezone.utc)
    end=dt.datetime(y+1,1,1,tzinfo=dt.timezone.utc)
    while t<end:
        off=t.astimezone(z).utcoffset()
        if prev and off!=prev[1]:
            # bisect to the minute
            lo,hi=prev[0],t
            while (hi-lo)>dt.timedelta(minutes=1):
                mid=lo+(hi-lo)/2
                if mid.astimezone(z).utcoffset()==prev[1]: lo=mid
                else: hi=mid
            out.append(hi)
        prev=(t,off); t+=dt.timedelta(hours=1)
    return out
for y in (2026,2027):
    for n,z in (("US",CHI),("UK",Z["Europe/London"])):
        for i in transitions(z,y):
            print("  %s %s exact %s UTC = %s"%(y,n,i.strftime("%Y-%m-%d %H:%M"),i.astimezone(CHI).strftime("%Y-%m-%d %H:%M %Z %a")))
