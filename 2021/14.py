ls = [l.strip() for l in open("../inputs/2021/14.txt").read().strip().splitlines()]
ps, rs = {}, {(l[:2]): l[6] for l in ls[2:]}
for i in range(len(ls[0])-1):
    ps[ls[0][i:i+2]] = ps.get(ls[0][i:i+2], 0) + 1

def fa(ps):
    cs = {ls[0][-1]: 1}
    for k, v in ps.items():
        cs[k[0]] = cs.get(k[0], 0) + v
    return max(cs.values()) - min(cs.values())

for i in range(40):
    if i == 10: print(f"Part 1: {fa(ps)}")
    ns = {}
    for k, v in ps.items():
        ns[k[0] + rs[k]] = ns.get(k[0]+rs[k], 0) + v
        ns[rs[k] + k[1]] = ns.get(rs[k]+k[1], 0) + v
    ps = ns

print(f"Part 2: {fa(ps)}")