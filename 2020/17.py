#!venv/bin/python3
import itertools as it

cs = {(x,y,0,0):1 for x,l in enumerate(open("inputs/17.in")) for y,c in enumerate(l.strip()) if c == "#"}
ds = [-1, 0, 1]

def f(cs, es):
    for _ in range(6):
        cc = cs.copy()
        rs = [j for j in range(min([min(t) for t in cs])-1, max([max(t) for t in cs])+2)]
        for c in it.product(rs, rs, rs, es if es == [0] else rs):
            n = sum([1 for i,j,k,l in it.product(ds, ds, ds, es) if (i,j,k,l) != (0,0,0,0) and (c[0]+i, c[1]+j, c[2]+k, c[3]+l) in cc])
            if (c in cc) and (not 2 <= n <= 3) and (c in cs): cs.pop(c)
            if (c not in cc) and (n == 3) and (c not in cs): cs[c] = 1
    return len(cs)

print("Part 1:", f(cs, [0]))
print("Part 2:", f(cs, ds))