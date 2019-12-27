#!/usr/bin/python3
x,y,xs,ys,xr,yr,ha,hb = 0,0,0,0,0,0,{(0,0)},{(0,0)}
d = {'^': (0,1), 'v': (0,-1), '>': (1,0), '<': (-1,0)}
for i,c in enumerate(open("inputs/03.in").readline()):
    x,y = x+d[c][0],y+d[c][1]
    ha.add((x,y))
    if (i&1):
        xs,ys = xs+d[c][0],ys+d[c][1]
        hb.add((xs,ys))
    else:
        xr,yr = xr+d[c][0],yr+d[c][1]
        hb.add((xr,yr))

print(len(ha), len(hb))