ls = [int(l.strip().split(" ")[-1])-1 for l in open("inputs/21.txt").read().strip().splitlines()]

d, r = 0, 0
def frd():
    global d,r
    d, r = d+1 if d < 100 else 1, r+1
    return d

t, ps, ss = 0, ls[:], [0, 0]
while all(s < 1000 for s in ss):
    ps[t] = (ps[t] + sum(frd() for _ in range(3))) % 10
    ss[t] += ps[t] + 1
    t = (t + 1) % 2

print(f"Part 1: {min(ss) * r}")

rs = [a+b+c+3 for a in range(3) for b in range(3) for c in range(3)]
ws, gs = [0,0], { (tuple(ls),(0,0),0): 1 }
while gs:
    ps,ss,t = min(gs.keys(), key=lambda x: sum(x[1]))
    c = gs.pop((ps, ss, t))
    for r in rs:
        nps = list(ps)
        nps[t] = (nps[t] + r) % 10
        nss = list(ss)
        nss[t] += nps[t] + 1
        if nss[t] < 21:
            gs[(tuple(nps), tuple(nss), (t+1) % 2)] = gs.get((tuple(nps), tuple(nss), (t+1) % 2), 0) + c
        else:
            ws[t] += c

print(f"Part 2: {max(ws)}")