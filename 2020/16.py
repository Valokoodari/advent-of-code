import re

ps = open("../inputs/2020/16.txt", "r").read().split("\n\n")
ot = [int(v) for v in ps[1].split("\n")[1].split(",")]
ts = [[int(v) for v in l.split(",")] for l in ps[2].split("\n")[1:]]
fs = {f: [int(v) for v in re.split("-| or ", rs)] for f,rs in [l.split(": ") for l in ps[0].split("\n")]}

a1 = 0
vs = []
for t in ts:
    a = a1
    for v in t:
        found = sum([1 for a,b,c,d in fs.values() if a <= v <= b or c <= v <= d])
        if not found: a1 += v
    if a == a1:
        vs.append(t)

tsv = {}
for ti, t in enumerate(vs):
    tsv[ti] = {}
    for fi in range(len(vs[0])):
        tsv[ti][fi] = []
        for k,v in fs.items():
            if v[0] <= t[fi] <= v[1] or v[2] <= t[fi] <= v[3]:
                valid = True
                for tid,tc in tsv.items():
                    if tid == ti: continue
                    if k not in tc[fi]:
                        valid = False
                if valid:
                    tsv[ti][fi].append(k)

d,fi,sv = [],0,tsv[len(tsv)-1]
while fi < len(tsv[0]):
    if len(sv[fi]) == 1 and fi not in d:
        d.append(fi)
        for i in range(len(sv)):
            if i == fi: continue
            if sv[fi][0] in sv[i]:
                sv[i].remove(sv[fi][0])
        fi = -1
    fi += 1

a2,of = 1,[v[0] for v in sv.values()]
for i in range(len(of)):
    if "departure" in of[i]:
        a2 *= ot[i]

print("Part 1:", a1)
print("Part 2:", a2)