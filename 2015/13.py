from itertools import permutations

ls = [l.split(",") for l in open("../inputs/2015/13.txt").read().strip()
    .replace(" would gain ", ",")
    .replace(" would lose ", ",-")
    .replace(" happiness units by sitting next to ", ",")
    .replace(".", "")
    .splitlines()]

ps = {}
for l in ls:
    if l[0] not in ps:
        ps[l[0]] = {}
    if l[2] not in ps[l[0]]:
        ps[l[0]][l[2]] = int(l[1])

def fch(ps):
    a = 0
    for p in permutations(ps.keys()):
        h = 0
        for i in range(len(p)):
            h += ps[p[i]][p[(i+1)%len(p)]]
            h += ps[p[i]][p[(i-1)%len(p)]]
        if h > a:
            a = h
    return a

print(f"Part 1: {fch(ps)}")

ps['Me'] = {}
for p in [n for n in ps]:
    ps[p]['Me'] = 0
    ps['Me'][p] = 0

print(f"Part 2: {fch(ps)}")