#!venv/bin/python3
import re

ls = [re.split(" = ", l.strip()) for l in open("inputs/14.in", "r").readlines()]

mem1,mem2 = {},{}

def w2(m, a, v):
    ar = [""]
    for i,c in enumerate(m):
        ar = [ad+a[i] if c == "0" else ad+"1" for ad in ar]
        if c == "X":
            ar += [ad[:-1]+"0" for ad in ar]
    for ad in ar: mem2[int(ad,2)] = v

m = "X"*36
for l in ls:
    if l[0] == "mask":
        m = l[1]
    else:
        l = [str(bin(int(l[0][4:][:-1])))[2:], str(bin(int(l[1])))[2:]]
        v = (36-len(l[1]))*"0" + l[1]
        a = (36-len(l[0]))*"0" + l[0]

        mem1[int(a,2)] = int("".join([v[i] if m[i] == "X" else m[i] for i in range(len(v))]), 2)
        w2(m, a, int(v,2))

print("Part 1:", sum([v for v in mem1.values()]))
print("Part 2:", sum([v for v in mem2.values()]))