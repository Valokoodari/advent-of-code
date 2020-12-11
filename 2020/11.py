#!/usr/bin/python3
ss = [[c for c in l] for l in open("inputs/11.in", "r").readlines()]
ss = [["."]*(len(ss[0])+2), *[[".", *s, "."] for s in ss], ["."]*(len(ss[0])+2)]

ds = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

def ad(ss, x, y, p):
    if p == 1:
        return sum(1 for d in ds if ss[x+d[0]][y+d[1]] == "#")
    t = 0
    for d in ds:
        for i in range(1, len(ss)):
            if not 0 <= x+d[0]*i < len(ss) or not 0 <= y+d[1]*i < len(ss[x+d[0]*i]): break
            if ss[x+d[0]*i][y+d[1]*i] == "#": t += 1
            if ss[x+d[0]*i][y+d[1]*i] != ".": break
    return t

def sim(ss, p, c):
    while c:
        c,cs = 0,[s.copy() for s in ss]
        for i in range(1, len(ss)-1):
            for j in range(1, len(ss[i])-1):
                if ss[i][j] == "L" and ad(ss, i, j, p) == 0: c,cs[i][j] = c+1,"#"
                if ss[i][j] == "#" and ad(ss, i, j, p) >= 3+p: c,cs[i][j] = c+1,"L"
        ss = cs
    return sum([s.count("#") for s in ss])

print("Part 1:", sim(ss, 1, 1))
print("Part 2:", sim(ss, 2, 1))