import gzip, json, glob, os, io, zlib
for f in sorted(glob.glob('raw_*.bin')):
    ts=f[4:-4]
    b=open(f,'rb').read()
    data=None
    if b[:2]==b'\x1f\x8b':
        try: data=gzip.decompress(b)
        except Exception as e:
            try: data=zlib.decompressobj(16+zlib.MAX_WBITS).decompress(b)
            except Exception as e2: print(ts,'GZFAIL',e,e2); continue
    else:
        data=b
    open(f'dec_{ts}.json','wb').write(data)
    try:
        j=json.loads(data)
        n=j.get('data',{}).get('list',{}).get('count')
        print(ts, len(data), 'count=', n)
    except Exception as e:
        print(ts, len(data), 'JSONFAIL', str(e)[:80], data[:120])
