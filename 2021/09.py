ps = [[int(c) for c in l.strip()] for l in open("../inputs/2021/09.txt").read().strip().splitlines()]
bs, ms = {}, [[(-1,-1) for _ in r] for r in ps]

def fbs(x,y):
    if ms[x][y] != (-1,-1): return ms[x][y]

    lp = (x,y)
    if x > 0 and ps[x-1][y] < ps[x][y]: lp = fbs(x-1,y)
    elif x < len(ps)-1 and ps[x+1][y] < ps[x][y]: lp = fbs(x+1,y)
    elif y > 0 and ps[x][y-1] < ps[x][y]: lp = fbs(x,y-1)
    elif y < len(ps[x])-1 and ps[x][y+1] < ps[x][y]: lp = fbs(x,y+1)

    ms[x][y] = lp
    return lp

for x,r in enumerate(ps):
    for y,c in enumerate(r):
        if c != 9:
            b = fbs(x,y)
            if b not in bs:
                bs[b] = 0
            bs[b] += 1

print(f"Part 1: {sum(ps[x][y] + 1 for x,y in bs)}")
print(f"Part 2: {eval('*'.join(map(str, sorted(bs.values())[-3:])))}")