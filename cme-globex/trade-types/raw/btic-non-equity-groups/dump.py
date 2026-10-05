import json,sys,re,html
for p in sys.argv[1:]:
    t=open(p).read()
    try:
        i=t.index('{'); d=json.loads(t[i:])
    except Exception as e:
        print(p,'PARSE FAIL',e); continue
    print('='*8,p.split('/')[-1])
    print('ProductID:',d.get('ProductID'),'| ProductName:',d.get('ProductName'))
    print('ProductCode:',json.dumps(d.get('ProductCode')))
    print('ProductGroup:',d.get('ProductGroup'),'| SubGroup:',d.get('ProductSubGroup'),'| Rulebook:',re.sub('<[^>]+>','',str(d.get('ExchangeRulebook')))[:120])
    for v in d.get('TradingHours',{}).get('vandhr',[]):
        h=html.unescape(re.sub(r'<br\s*/?>',' | ',v['hours'])).replace('\n',' ')
        h=re.sub(r'\s+',' ',h)
        print('  HOURS',v['venue'],'=>',h)
    to=d.get('TerminationOfTrading')
    if to: print('  TERM:',re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',str(to))))[:300])
    tas=d.get('TradeAtMarkerOrTradeAtSettlementRules')
    if tas: print('  TAS/TAM RULES:',re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',str(tas))))[:400])
    u=d.get('Underlying')
    if u: print('  UNDERLYING:',re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',str(u))))[:300])
