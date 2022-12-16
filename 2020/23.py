cs = [int(c) for c in open("../inputs/2020/23.txt", "r").readline().strip()]

def f(cs, ts):
    p,cc = {n: cs[(i+1)%len(cs)] for i,n in enumerate(cs)},cs[-1]

    for _ in range(ts):
        cc,dc = p[cc],p[cc]-1 if p[cc]-1 > 0 else max(p.keys())
        hc,p[cc] = [p[cc], p[p[cc]], p[p[p[cc]]]],p[p[p[p[cc]]]]

        while dc in hc:
            dc -= 1
            if dc < 1:
                dc = max(p.keys())
        p[dc],p[hc[-1]] = hc[0],p[dc]

    a,n = [],1
    for _ in range(8):
        n = p[n]
        a.append(str(n))
    return "".join(a), p[1] * p[p[1]]

print("Part 1:", f(cs.copy(), 100)[0])
print("Part 2:", f(cs.copy() + [i for i in range(10, 1000001)], 10000000)[1])