#!/usr/bin/python3
ls = [l.strip() for l in open("inputs/05.in", "r").readlines()]

tb = { "F": "0", "B": "1", "L": "0", "R": "1" }

ss,a = [],0
for l in ls:
    for k,v in tb.items():
        l = l.replace(k, v)
    ss.append(int(l[:-3],2)*8 + int(l[7:], 2))
print("Part 1:", max(ss))

ss.sort()
for i in range(len(ss)-1):
    if ss[i]+2 == ss[i+1]:
        print("Part 2:", ss[i]+1)