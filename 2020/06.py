#!/usr/bin/python3
a1,a2 = 0,0
for g in open("inputs/06.in", "r").read().split("\n\n"):
    cs = {c: g.count(c) for c in g.replace("\n", "")}
    a1 += len(cs)
    a2 += len([v for v in cs.values() if v == len(g.split("\n"))])

print("Part 1:", a1)
print("Part 2:", a2)