"""Compare merged ICE rows with manual readings of the freshly captured PDFs."""
from pathlib import Path
from datetime import datetime,timezone
import ast,operator,json,re,hashlib,subprocess
root=Path(__file__).parent
repo=Path('/workspace/exchange-hours-rs')
source=repo/'src/calendar/schedules/holidays/ice_us.rs'
s=source.read_text()
def seconds(expr):
 def number(node):
  if isinstance(node,ast.Expression):return number(node.body)
  if isinstance(node,ast.Constant) and isinstance(node.value,int):return node.value
  if isinstance(node,ast.BinOp) and isinstance(node.op,(ast.Add,ast.Sub,ast.Mult)):
   return {ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul}[type(node.op)](number(node.left),number(node.right))
  raise ValueError(expr)
 return number(ast.parse(expr.strip(),mode='eval'))
def clock(value):return f'{value//3600:02d}:{value//60%60:02d}'
# These values are manual transcriptions/derivations from the captured notice,
# master hours and PCPO table, independent of the Rust constants being checked.
expected={
 'SUGAR_CHRISTMAS_REOPEN_BLOCKS':[('order_entry',-4,'13:30','15:30'),('regular',0,'08:00','13:00')],
 'COFFEE_COCOA_CHRISTMAS_REOPEN_BLOCKS':[('order_entry',-4,'13:35','15:30'),('regular',0,'08:00','13:30')],
 'COTTON_CHRISTMAS_REOPEN_BLOCKS':[('order_entry',-4,'13:35','15:30'),('regular',0,'08:00','14:20')],
 'FCOJ_CHRISTMAS_REOPEN_BLOCKS':[('order_entry',-4,'13:35','15:30'),('regular',0,'08:00','14:00')],
 'COTTON_AFTER_CHRISTMAS_REOPEN_BLOCKS':[('order_entry',-1,'14:50','18:00'),('order_entry',-1,'19:30','21:00'),('regular',-1,'21:00','14:20')]
}
checks=[]
for name,want in expected.items():
 block=re.search(r'static '+name+r': \[ExceptionBlock; \d\] = \[(.*?)\];',s,re.S).group(1)
 actual=[(kind,int(offset),clock(seconds(start)),clock(seconds(end))) for kind,offset,start,end in re.findall(r'ExceptionBlock::(\w+)\(([-\d]+),([^,]+),([^\)]+)\)',block)]
 assert actual==want,(name,actual,want)
 checks.append({'scope':name,'expected':want,'actual':actual,'matches':True})
tables={name:body for name,body in re.findall(r'pub\(crate\) static (\w+): &HolidayTable = holidays! \{(.*?)\n\};',s,re.S)}
for name,blocks in [('SUGAR','SUGAR'),('COFFEE','COFFEE_COCOA'),('COCOA','COFFEE_COCOA'),('COTTON','COTTON'),('ORANGE_JUICE','FCOJ')]:
 row=f'(2026, 12, 28, ReplacementBlocks(&{blocks}_CHRISTMAS_REOPEN_BLOCKS), T1, "IFUS-NOTICE-2026-CHRISTMAS")'
 assert row in tables[name],name
 checks.append({'scope':name,'date':'2026-12-28','matches':True,'row':row})
assert '(2026, 12, 29, ReplacementBlocks(&COTTON_AFTER_CHRISTMAS_REOPEN_BLOCKS), T1, "IFUS-NOTICE-2026-CHRISTMAS")' in tables['COTTON']
for name in ['COFFEE','COCOA','COTTON','ORANGE_JUICE','FANG','DOLLAR_INDEX']:
 row=re.search(r'\(2026, 12, 24, early_close\((.*?)\), T1, "IFUS-NOTICE-2026-CHRISTMAS"\)',tables[name])
 assert row,name
 actual=clock(seconds(row.group(1)));want='13:15' if name in ['FANG','DOLLAR_INDEX'] else '13:05'
 assert actual==want,(name,actual,want)
 checks.append({'scope':name,'date':'2026-12-24','close_ny':actual,'matches':True})
assert not re.search(r'^\s*\(2026, 12, 24,',tables['SUGAR'],re.M)
for name in ['FANG','DOLLAR_INDEX']:
 assert not re.search(r'^\s*\(2026, 12, 28,',tables[name],re.M)
for name,body in tables.items():
 assert re.search(r'\(2026, 12, 25, Closed, T1,',body),name
checks.append({'scope':'all eight tables','date':'2026-12-25','kind':'Closed','matches':True})
for date in [24,28,29]:
 assert f'(2026, 12, {date}, Unsourced, T1, "IFUS-NOTICE-2026-CHRISTMAS")' in tables['VENUE']
checks.append({'scope':'broad venue','dates':['2026-12-24','2026-12-28','2026-12-29'],'kind':'Unsourced','matches':True})
result={'checked_utc':datetime.now(timezone.utc).isoformat(),'crate_head':subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip(),'source':str(source.relative_to(repo)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'all_match':True,'checks':checks,'limitation':'Checks compare published future arrangements and unchanged ordinary boundaries; they do not witness future production trading.'}
(root/'MERGED_DATA_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_match':result['all_match'],'checks':len(checks),'crate_head':result['crate_head'],'checked_utc':result['checked_utc']}))
