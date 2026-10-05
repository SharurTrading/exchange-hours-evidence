import datetime as dt, zoneinfo, collections
CHI = zoneinfo.ZoneInfo("America/Chicago")
def count(zname, h, m, year=2026):
    c = collections.Counter()
    d = dt.date(year,1,1)
    while d.year==year:
        if d.weekday()<=4:
            loc = dt.datetime(d.year,d.month,d.day,h,m,tzinfo=zoneinfo.ZoneInfo(zname))
            ch = loc.astimezone(CHI)
            c[(ch.strftime("%H:%M"),(ch.date()-d).days)] += 1
        d += dt.timedelta(days=1)
    return dict(c)
for nm,z,h,m in [("London 16:30","Europe/London",16,30),("London 15:02","Europe/London",15,2),
                 ("London 12:35","Europe/London",12,35),("London 16:00","Europe/London",16,0),
                 ("London 15:40","Europe/London",15,40),
                 ("SGT 16:30","Asia/Singapore",16,30),("SHA 15:00","Asia/Shanghai",15,0),
                 ("HKG 16:00","Asia/Hong_Kong",16,0),("TYO 15:30","Asia/Tokyo",15,30)]:
    print(nm, count(z,h,m))
# weekday total 2026
wd=sum(1 for n in range(365) if (dt.date(2026,1,1)+dt.timedelta(days=n)).weekday()<=4)
print("weekdays 2026 =", wd)
# US DST 2026 window
print("US 2026 dst:", dt.datetime(2026,3,8,8,tzinfo=dt.timezone.utc).astimezone(CHI).utcoffset(),
      dt.datetime(2026,11,1,8,tzinfo=dt.timezone.utc).astimezone(CHI).utcoffset())
# check GCD 15:02 London values on specific probe dates
LON=zoneinfo.ZoneInfo("Europe/London")
for d in ["2026-10-26","2026-12-07","2027-03-15","2026-07-15"]:
    y,mo,da=map(int,d.split("-"))
    loc=dt.datetime(y,mo,da,15,2,tzinfo=LON)
    print("GCD",d,"->",loc.astimezone(CHI).strftime("%Y-%m-%d %H:%M"))
HK=zoneinfo.ZoneInfo("Asia/Hong_Kong")
for d in ["2026-10-26","2026-12-07"]:
    y,mo,da=map(int,d.split("-"))
    loc=dt.datetime(y,mo,da,16,0,tzinfo=HK)
    print("FTC",d,"->",loc.astimezone(CHI).strftime("%Y-%m-%d %H:%M"))
# UK ever BST while Chicago CST?
bad=[]
d=dt.date(2010,1,1)
while d.year<2031:
    u=dt.datetime(d.year,d.month,d.day,12,tzinfo=dt.timezone.utc)
    if u.astimezone(LON).utcoffset()==dt.timedelta(hours=1) and u.astimezone(CHI).utcoffset()==dt.timedelta(hours=-6):
        bad.append(d)
    d+=dt.timedelta(days=1)
print("UK-BST & US-CST days 2010-2030:", len(bad), bad[:5])
