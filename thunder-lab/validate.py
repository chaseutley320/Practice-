import json,csv
from pathlib import Path
p=Path(__file__).parent/'dist'
d=json.loads((p/'data.json').read_text());g=d['games']
assert len(g)==82
assert len({r['date'] for r in g})==82
assert [r['date'] for r in g]==sorted(r['date'] for r in g)
assert sum(r['result']=='W' for r in g)==68
assert sum(r['venue']=='Home' for r in g)==41
assert sum(r['venue']=='Away' for r in g)==40
assert all((r['points']>r['allowed'])==(r['result']=='W') for r in g)
assert round(sum(r['points'] for r in g)/82,1)==120.5
assert round(sum(r['allowed'] for r in g)/82,1)==107.6
assert len(d['players'])==12
for kind in ['games','players']:
 rows=list(csv.DictReader((p/(kind+'.csv')).open()))
 assert len(rows)==len(d[kind])
print('PASS: counts, dates, venues, results, scoring averages and CSV lengths')

assert sum(r['venue']=='Neutral' for r in g)==1
