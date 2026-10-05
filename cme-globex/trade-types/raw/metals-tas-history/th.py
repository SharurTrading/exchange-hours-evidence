import sys,json,re
for f in sys.argv[1:]:
    t=open(f).read()
    try:
        i=t.index('{"'); j=t.rindex('}')+1
        d=json.loads(t[i:j])
    except Exception as e:
        print(f,'PARSE FAIL',e); continue
    print('=====',f,'productId',d.get('ProductID'))
    th=d.get('TradingHours',{})
    for r in th.get('vandhr',[]):
        print('  ',r.get('venue'),'|',r.get('hours'))
    tt=d.get('TerminationOfTrading',{})
    for r in tt.get('terminationOfTrading',[]):
        print('   TERM:',r.get('termsOfTrading'))
