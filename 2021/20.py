ds = open("inputs/20.txt").read().strip().replace("#","1").replace(".","0").split("\n\n")
es, gs, b = [c for c in ds[0]], [[c for c in r] for r in ds[1].splitlines()], "0"

def fep(gs, b):
    ngs = []
    for x in range(-1, len(gs[0])+1):
        r = []
        for y in range(-1, len(gs)+1):
            r.append(es[int("".join(gs[x+dx][y+dy] if 0 <= x+dx < len(gs) and 0 <= y+dy < len(gs[0]) else b for dx in range(-1,2) for dy in range(-1,2)), 2)])
        ngs.append(r)
    return ngs, es[-1] if b == "1" else es[0]

for _ in range(2):
    gs, b = fep(gs, b)
print(f"Part 1: {sum(sum(1 for x in r if x=='1') for r in gs)}")
for _ in range(48):
    gs, b = fep(gs, b)
print(f"Part 2: {sum(sum(1 for x in r if x=='1') for r in gs)}")