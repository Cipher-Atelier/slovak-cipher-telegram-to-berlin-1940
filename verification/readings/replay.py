#!/usr/bin/env python3
"""New, read-only replay audit. Does not re-fit keys or certify manuscript truth.
Run from this reading packet: python3 replay.py
"""
from pathlib import Path
import json,csv,hashlib,re,string,sys
P=Path(__file__).resolve().parent
E=P/'evidence' if (P/'evidence').exists() else P/'repro_inventory_core'
REPORT={}
def txt(p):return p.read_text(encoding='utf-8')
def js(p):return json.loads(txt(p))
def sha(b):return hashlib.sha256(b).hexdigest()
def record(topic,**kw):REPORT[topic]={'status':'PASS','scope':'mechanical replay only',**kw}

if sys.flags.optimize:
 raise SystemExit('Run normal Python; assertion checks must remain enabled.')

# Berlin: every position of all three preserved stages.
b=E/'HCP128_Verified_Reading';rows=list(csv.DictReader((b/'key.csv').open()));key={r['cipher']:r['plaintext'] for r in rows if r['plaintext']};states={}
for label in ['initial','heldout_checked','source_checked']:
 c=txt(b/f'ciphertext_{label}.txt').strip();out=''.join(key.get(x,'?') for x in c);assert len(c)==456 and out==txt(b/f'plaintext_{label}.txt').strip();states[label]={'positions':len(c),'unknowns':out.count('?'),'literal_sha256':sha(out.encode())}
record('berlin-1940',states=states,unobserved_cipher_letters=''.join(r['cipher'] for r in rows if not r['plaintext']),equivalent_unused_completions=24)

print(json.dumps(REPORT,ensure_ascii=False,indent=2))
