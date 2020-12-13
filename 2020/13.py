#!venv/bin/python3
from sympy.ntheory.modular import crt
ls = open("inputs/13.in", "r").readlines()

ft,bs = int(ls[0]), { int(r): i for i,r in enumerate(ls[1].split(",")) if r != "x" }

t,a1 = ft,[]
for t in range(ft, ft+sum(bs)):
    for n in [b*(t-ft) for b in bs if t % b == 0]: a1.append(n)

print("Part 1:", a1[0])
print("Part 2:", crt(bs, [-i for i in bs.values()])[0])