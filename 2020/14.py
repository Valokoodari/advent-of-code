#!venv/bin/python3
import re

ls = [re.split(" = ", l.strip()) for l in open("inputs/14.in", "r").readlines()]

mem1,mem2,b = {},{},36

def w2(a, v):
    ar = [""]
    for i,c in enumerate(a):
        if c == "X":
            ar = [ad+"0" for ad in ar]
            ar += [ad[:-1]+"1" for ad in ar]
        else:
            ar = [ad+a[i] for ad in ar]
    for ad in ar: mem2[int(ad,2)] = v

m = "X"*36
for l in ls:
    if l[0] == "mask":
        m = l[1]
    else:
        l = [str(bin(int(l[0][4:][:-1])))[2:], str(bin(int(l[1])))[2:]]
        v = (b-len(l[1]))*"0" + l[1]
        a = (b-len(l[0]))*"0" + l[0]

        mem1[int(a,2)] = int("".join([v[i] if m[i] == "X" else m[i] for i in range(len(v))]), 2)
        w2("".join([a[i] if m[i] == "0" else m[i] for i in range(b)]), int(v,2))

print("Part 1:", sum([v for v in mem1.values()]))
print("Part 2:", sum([v for v in mem2.values()]))