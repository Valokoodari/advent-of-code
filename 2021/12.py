rs, ls = {}, [l.strip().split("-") for l in open("../inputs/2021/12.txt").read().strip().splitlines()]
for a,b in ls:
    rs[a] = rs.get(a, []) + [b]
    rs[b] = rs.get(b, []) + [a]

def ffs(c, vs, t, p2):
    if c == "end":
        return 1
    if c.islower() and c in vs:
        if c == "start" or not p2 or t:
            return 0
        t = True
    vs = vs | {c}
    return sum(ffs(b, vs, t, p2) for b in rs[c])

print(f"Part 1: {ffs('start', set(), False, False)}")
print(f"Part 2: {ffs('start', set(), False, True)}")