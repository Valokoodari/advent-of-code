p1,p2,ps,ds = int(1e12),0,[],{}

for l in open("../inputs/2015/09.txt").readlines():
    a,_,b,_,d = l.split()
    if a not in ps:
        ps.append(a)
        ds[a] = {}
    if b not in ps:
        ps.append(b)
        ds[b] = {}
    ds[a][b],ds[b][a] = int(d),int(d)

def search(c, ps, d):
    global p1,p2
    ps.remove(c)
    if len(ps) == 0:
        if d < p1: p1 = d
        if d > p2: p2 = d
        return
    for p in ps:
        search(p, ps[:], d + ds[c][p])

for p in ps:
    search(p, ps[:], 0)

print(f"Part 1: {p1}\nPart 2: {p2}")