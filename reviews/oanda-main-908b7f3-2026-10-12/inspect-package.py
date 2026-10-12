from pathlib import Path
import subprocess,json,os
root=Path('/tmp/oanda-release-main-final')
result=Path('/tmp/oanda-main-final-proof')
env=os.environ.copy();env['CARGO_TARGET_DIR']='/tmp/oanda-release-complete-current/target'
names=subprocess.check_output(['cargo','package','--list','--locked'],cwd=root,env=env,text=True).splitlines()
(result/'package-list.txt').write_text('\n'.join(names)+'\n')
archive=Path('/tmp/oanda-release-complete-current/target/package/exchange-hours-1.1.0')
vcs=json.loads((archive/'.cargo_vcs_info.json').read_text());assert vcs['git']['sha1']=='908b7f33556e3bf363d92089ba49da87bb37cdd4',vcs
same=[];normalized=[];generated=[]
for n in names:
 source=root/('Cargo.toml' if n=='Cargo.toml.orig' else n)
 if not source.exists():generated.append(n)
 elif source.read_bytes()==(archive/n).read_bytes():same.append(n)
 else:normalized.append(n)
assert len(names)==486 and len(same)==483,(len(names),len(same))
assert normalized==['Cargo.lock','Cargo.toml'],normalized
assert generated==['.cargo_vcs_info.json'],generated
bad=[n for n in names if any(n==x or n.startswith(x+'/') for x in ['.github','tools','docs/plans','rust-toolchain.toml','deny.toml','clippy.toml'])];assert not bad,bad
required=['AGENTS.md','RELEASING.md','CHANGELOG.md','README.md','docs/evidence/oanda_china50_cfd.md','docs/evidence/oanda_singapore30_cfd.md','docs/evidence/nasdaq_stockholm.md','docs/evidence/euronext_brussels.md','docs/evidence/euronext_lisbon.md']
assert all(n in names for n in required)
proof={'head':vcs['git']['sha1'],'package_files':len(names),'byte_identical':len(same),'normalized':normalized,'generated':generated,'required_docs_present':True,'forbidden_files_present':bad}
(result/'package-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2))
