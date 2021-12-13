ls = [p.splitlines() for p in open("inputs/13.in").read().strip().split("\n\n")]
ns = set(tuple(map(int, l.split(","))) for l in ls[0])
fs = [(l[11],int(l[13:])) for l in ls[1]]

def fps(ns):
    return "\n".join(["".join(["█" if (x,y) in ns else " " for x in range(0, max(x for x,_ in ns)+1)]) for y in range(0, max(y for _,y in ns)+1)])

def ffp(ns, d, p):
    if d == 'x':
        return set(n if n[0] < p else (2*p-n[0], n[1]) for n in ns)
    return set(n if n[1] < p else (n[0], 2*p-n[1]) for n in ns)

ns = ffp(ns, fs[0][0], fs[0][1])
print(f"Part 1: {len(ns)}")

for f in fs[1:]:
    ns = ffp(ns, f[0], f[1])
print(f"Part 2:\n{fps(ns)}")