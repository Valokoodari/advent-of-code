#!venv/bin/python3
ds = {"e": (-1,1,0), "se": (0,1,-1), "sw": (1,0,-1), "w": (1,-1,0), "nw": (0,-1,1), "ne": (-1,0,1)}
ts = set()

for l in [l.strip() for l in open("inputs/24.in", "r").readlines()]:
    c,i = (0,0,0),0
    while i < len(l):
        m = ds[l[i]] if l[i] == "e" or l[i] == "w" else ds[l[i]+l[i+1]]
        i += 1 if m[2] == 0 else 2
        c = tuple(map(sum, zip(c, m)))

    if c not in ts: ts.add(c)
    else: ts.discard(c)

print("Part 1:", len(ts))

def f(c, ts):
    b = sum([1 for d in ds.values() if tuple(map(sum, zip(c, d))) in ts])
    return 1 if c in ts and b in [1,2] or c not in ts and b == 2 else 0

for l in range(100):
    cs = ts | set(tuple(map(sum, zip(c, d))) for c in ts for d in ds.values())
    ts = set(c for c in cs if f(c, ts))

print("Part 2:", len(ts))