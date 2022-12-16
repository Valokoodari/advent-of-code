ls = [l.strip() for l in open("../../inputs/2021/15.txt").read().strip().splitlines()]
cs = [[int(c) for c in l] for l in ls]

def fds(cs):
    ts, ms = [(0, (0,0))], [[float('inf') for _ in x] for x in cs]
    while ts:
        ts.sort()
        r,(x,y) = ts.pop(0)
        if x == len(cs)-1 and y == len(cs[0])-1:
            return r
        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
            if 0 <= x+dx < len(cs) and 0 <= y+dy < len(cs[0]):
                nr = r + cs[x+dx][y+dy]
                if nr < ms[x+dx][y+dy]:
                    ms[x+dx][y+dy] = nr
                    ts.append((nr, (x+dx,y+dy)))

print(f"Part 1: {fds(cs)}")

for i,x in enumerate(cs):
    cs[i] = [cs[i][j]+t if cs[i][j]+t < 10 else (cs[i][j]+t)%9 for t in range(5) for j in range(len(x))]
for t in range(1,5):
    for x in cs[:100]:
        cs.append([y+t if y+t < 10 else (y+t)%9 for y in x])
print(f"Part 2: {fds(cs)}")