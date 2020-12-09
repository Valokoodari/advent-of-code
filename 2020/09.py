#!/usr/bin/python3
import itertools as it;

ns = [int(l.strip()) for l in open("inputs/09.in", "r").readlines()]

def p1():
    for i in range(0, len(ns)-25):
        if ns[i+25] not in [a+b for a,b in it.combinations(ns[i:25+i], 2)]:
            return ns[i+25]

def p2(n):
    for i in range(0, len(ns)-1):
        for j in range(0, len(ns)-i):
            r = ns[i:i+j]
            if sum(r) == n:
                return min(r) + max(r)

print("Part 1:", p1())
print("Part 2:", p2(p1()))