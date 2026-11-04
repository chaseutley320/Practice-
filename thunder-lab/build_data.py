import json,csv
from pathlib import Path
p=Path(__file__).parent/'dist'
raw='''10-24 A Nuggets 102 87
10-26 A Bulls 114 95
10-27 H Hawks 128 104
10-30 H Spurs 105 93
11-01 A Trail_Blazers 137 114
11-02 A Clippers 105 92
11-04 H Magic 102 86
11-06 A Nuggets 122 124
11-08 H Rockets 126 107
11-10 H Warriors 116 127
11-11 H Clippers 134 128
11-13 H Pelicans 106 88
11-15 H Suns 99 83
11-17 H Mavericks 119 121
11-19 A Spurs 104 110
11-20 H Trail_Blazers 109 99
11-25 A Kings 130 109
11-27 A Warriors 105 101
11-29 A Lakers 101 93
12-01 A Rockets 116 119
12-03 H Jazz 133 106
12-05 A Raptors 129 92
12-07 A Pelicans 119 109
12-10 H Mavericks 118 104
12-14 N Rockets 111 96
12-19 A Magic 105 99
12-20 A Heat 104 97
12-23 H Wizards 123 105
12-26 A Pacers 120 114
12-28 A Hornets 106 94
12-29 H Grizzlies 130 106
12-31 H Timberwolves 113 105
01-02 H Clippers 116 98
01-03 H Knicks 117 107
01-05 H Celtics 105 92
01-08 A Cavaliers 122 129
01-10 A Knicks 126 101
01-12 A Wizards 136 95
01-14 A 76ers 118 102
01-16 H Cavaliers 134 114
01-17 A Mavericks 98 106
01-19 H Nets 127 101
01-22 H Jazz 123 114
01-23 H Mavericks 115 121
01-26 A Trail_Blazers 118 108
01-29 A Warriors 109 116
02-01 H Kings 144 110
02-03 H Bucks 125 96
02-05 H Suns 140 109
02-07 H Raptors 121 109
02-08 A Grizzlies 125 112
02-10 H Pelicans 137 101
02-12 H Heat 115 101
02-13 A Timberwolves 101 116
02-21 A Jazz 130 107
02-23 A Timberwolves 130 123
02-24 H Timberwolves 128 131
02-26 A Nets 129 121
02-28 A Hawks 135 119
03-02 A Spurs 146 132
03-03 H Rockets 137 128
03-05 A Grizzlies 120 103
03-07 H Trail_Blazers 107 89
03-09 H Nuggets 127 103
03-10 H Nuggets 127 140
03-12 A Celtics 118 112
03-15 A Pistons 113 107
03-16 A Bucks 121 105
03-19 H 76ers 133 100
03-21 H Hornets 141 106
03-23 A Clippers 103 101
03-25 A Kings 121 105
03-27 H Grizzlies 125 104
03-29 H Pacers 132 111
03-31 H Bulls 145 117
04-02 H Pistons 119 103
04-04 A Rockets 111 125
04-06 H Lakers 99 126
04-08 H Lakers 136 120
04-09 A Suns 125 112
04-11 A Jazz 145 111
04-13 A Pelicans 115 100'''
games=[]
for line in raw.splitlines():
 d,v,o,s,a=line.split();s=int(s);a=int(a)
 games.append(dict(date=('2024-' if int(d[:2])>9 else '2025-')+d,venue={'H':'Home','A':'Away','N':'Neutral'}[v],opponent=o.replace('_',' '),points=s,allowed=a,result='W' if s>a else 'L'))
rows=[['Shai Gilgeous-Alexander',76,34.2,32.7,5,6.4,1.7,1,51.9],['Jalen Williams',69,32.4,21.6,5.3,5.1,1.6,.7,48.4],['Chet Holmgren',32,27.4,15,8,2,.7,2.2,49],['Aaron Wiggins',76,22.9,12,3.9,1.8,.8,.2,48.8],['Isaiah Hartenstein',57,27.9,11.2,10.7,3.8,.8,1.1,58.1],['Isaiah Joe',74,21.7,10.2,2.6,1.6,.6,.1,44],['Luguentz Dort',71,29.2,10.1,4.1,1.6,1.1,.5,43.5],['Cason Wallace',68,27.6,8.4,3.4,2.5,1.8,.5,47.4],['Alex Caruso',54,19.3,7.1,2.9,2.5,1.6,.6,44.6],['Ajay Mitchell',36,16.6,6.5,1.9,1.8,.7,.1,49.5],['Kenrich Williams',69,16.4,6.3,3.5,1.4,.6,.1,48.3],['Jaylin Williams',47,16.7,5.9,5.6,2.6,.5,.6,43.9]]
players=[dict(zip(['name','games','minutes','points','rebounds','assists','steals','blocks','fg'],r)) for r in rows]
assert len(games)==82 and sum(g['result']=='W' for g in games)==68
assert round(sum(g['points'] for g in games)/82,1)==120.5
assert round(sum(g['allowed'] for g in games)/82,1)==107.6
(p/'data.json').write_text(json.dumps(dict(games=games,players=players),indent=2))
for name,data in [('games',games),('players',players)]:
 with (p/(name+'.csv')).open('w') as f:
  w=csv.DictWriter(f,fieldnames=data[0].keys());w.writeheader();w.writerows(data)
print('Verified 82 games, 68 wins, 120.5 PPG, 107.6 opponent PPG; 12 rotation players.')
