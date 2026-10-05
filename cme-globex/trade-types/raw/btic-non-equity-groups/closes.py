import json,sys
for p in sys.argv[1:]:
    t=open(p).read(); d=json.loads(t[t.index('{"props'):])
    for pr in d.get('products',[]):
        cl=[]
        for s in pr['tradingHours']['schedules']:
            for e in s['events']:
                if e['marketEventType'] in ('closed','paused'):
                    cl.append(f"{s['eventDate']}:{e['marketEventType']}@{e['eventTime']}")
        print(f"{pr['globex']:5s} grp={pr['prodGroup']:3s} | " + ' '.join(cl))
