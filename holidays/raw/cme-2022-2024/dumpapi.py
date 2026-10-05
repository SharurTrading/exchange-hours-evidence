import json,gzip,sys
def load(f):
    d=open(f,'rb').read()
    try: d=gzip.decompress(d)
    except Exception: pass
    return json.loads(d)
for f in sys.argv[1:]:
    j=load(f); print("=== %s  props=%s" % (f, j['props']))
    for p in j['products']:
        th=p['tradingHours']
        parts=[]
        for s in th['schedules']:
            ev=" ".join("%s %s[td %s]" % (e['eventTime'], e['marketEventType'].upper(), e['tradingDate']) for e in s['events'])
            parts.append("  %s (%s): %s" % (s['eventDate'], s['groupCode'], ev if ev else "(no events)"))
        print(" -- %s [id %s, globex %s, %s]" % (p['name'], p['id'], p.get('globex'), p.get('foi')))
        print("\n".join(parts))
