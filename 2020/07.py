import re

rs,bs,os = " bags contain | bags?\.| bags?, ",{},{}

a1,a2 = 0,0
for l in [re.split(rs, l) for l in open("../inputs/2020/07.txt", "r").readlines()]:
    bs[l[0]] = {}
    for b in [b.split(" ", 1) for b in l[1:-1]]:
        if b[0] == "no": continue
        bs[l[0]][b[1]] = int(b[0])
        if b[1] == "shiny gold": os[l[0]] = 1

def func(c):
    l = {}
    for b,v in bs.items():
        if c in v: l = {**{b: 1}, **l, **func(b)}
    return l

def add(c):
    return sum([add(b) * v + v for b,v in bs[c].items()])

print("Part 1:", len(func("shiny gold")))
print("Part 2:", add("shiny gold"))