#!/usr/bin/python3
l = [l.split("\n")[0] for l in open("inputs/08.in", "r").readlines()]

a,b = 0,0
for s in l:
    a += len(s) - len(eval(s))
    b += 2 + s.count("\"") + s.count("\\")

print("Part 1:", a)
print("Part 2:", b)