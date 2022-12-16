ls = [l.strip() for l in open("../inputs/2021/03.txt").readlines()]

ms = lambda ns: "".join([max([(i, c.count(i)) for i in set(c)], key=lambda x: x[1] + int(x[0]) * 0.1)[0] for c in list(zip(*ns))])

os,gs = ls[:],ls[:]
for i in range(len(ls[0])):
    mo,mg = ms(os),ms(gs)
    os = [o for o in os if o[i] == mo[i]]
    gs = [g for g in gs if g[i] != mg[i] or len(gs) == 1]

print(f"Part 1: {int(ms(ls),2) * (2**(len(ls[0]))-1 ^ int(ms(ls),2))}")
print(f"Part 2: {int(os[0],2) * int(gs[0],2)}")