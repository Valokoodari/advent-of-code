ls = [l.strip() for l in open("inputs/25.txt").read().strip().splitlines()]
u, a, mx, my = 1, 0, len(ls[0]), len(ls)
es = { (x, y) for y, l in enumerate(ls) for x, c in enumerate(l) if c == ">" }
ss =  { (x, y) for y, l in enumerate(ls) for x, c in enumerate(l) if c == "v" }

while u:
    a, u, nes, nss = a+1, 0, set(), set()
    for c in es:
        nc = ((c[0]+1)%mx, c[1])
        if not (nc in es or nc in ss):
            nes.add(nc)
            u += 1
        else:
            nes.add(c)
    for c in ss:
        nc = (c[0], (c[1]+1)%my)
        if not (nc in nes or nc in ss):
            nss.add(nc)
            u += 1
        else:
            nss.add(c)
    es, ss = nes, nss

print(f"Part 1: {a}")