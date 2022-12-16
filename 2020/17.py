import itertools as it

def f(d):
    cs = {(x,y,0,0):1 for x,l in enumerate(open("../inputs/2020/17.txt")) for y,c in enumerate(l.strip()) if c == "#"}
    for _ in range(6):
        cc = cs.copy()
        rs = [j for j in range(min([min(t) for t in cs])-1, max([max(t) for t in cs])+2)]
        for c in it.product(*([rs]*d + ([[0]] if d == 3 else []))):
            n = sum([1 for i,j,k,l in it.product(*([[-1, 0, 1]]*d + ([[0]] if d == 3 else []))) if (i,j,k,l) != (0,0,0,0) and (c[0]+i, c[1]+j, c[2]+k, c[3]+l) in cc])
            if (c in cc) and (not 2 <= n <= 3) and (c in cs): cs.pop(c)
            if (c not in cc) and (n == 3) and (c not in cs): cs[c] = 1
    return len(cs)

print("Part 1:", f(3))
print("Part 2:", f(4))