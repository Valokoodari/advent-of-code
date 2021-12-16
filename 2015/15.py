ps = [[int(p) for p in l.split(": ")[1]
       .replace("capacity ", "")
       .replace(" durability ", "")
       .replace(" flavor ", "")
       .replace(" texture ", "")
       .replace(" calories ", "")
       .split(",")]
      for l in open("inputs/15.in").read().strip().splitlines()]

def fl(ps, ts, p2):
    if len(ts)+1 == len(ps):
        ts.append(100-sum(ts))
    if len(ts) == len(ps):
        ss = map(lambda x: x if x > 0 else 0, [sum(p[i] * ts[j] for j, p in enumerate(ps)) for i in range(len(ps[0])-1)])
        return 0 if p2 and sum(p[4] * ts[i] for i, p in enumerate(ps)) != 500 else eval("*".join(map(str, ss)))
    m = 0
    for a in range(1, 101-sum(ts)):
        m = max(fl(ps, ts + [a], p2), m)
    return m

print(f"Part 1: {fl(ps, [], False)}")
print(f"Part 2: {fl(ps, [], True)}")