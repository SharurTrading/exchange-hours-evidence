import json,sys,re
for p in sys.argv[1:]:
    t=open(p).read(); i=t.index('{"props')
    d=json.loads(t[i:])
    for pr in d.get('products',[]):
        print(f"--- {p.split('/')[-1]} id={pr['id']} globex={pr['globex']} grp={pr['prodGroup']} :: {pr['name']}")
        for s in pr['tradingHours']['schedules']:
            evs=' ; '.join(f"{e['marketEventType']}@{e['eventTime']}(td {e['tradingDate']})" for e in s['events'])
            print(f"   {s['eventDate']} [{s['groupCode']}] {evs if evs else '(none)'}")
