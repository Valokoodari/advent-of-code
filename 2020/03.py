import re
import math

ls = [re.split("", l)[1:-2] for l in open("../inputs/2020/03.txt", "r").readlines()]

def func(cp, rp):
    a,c = 0,0
    for i in range(0, len(ls), rp):
        if ls[i][c] == "#": a += 1
        c = (c + cp) % len(ls[i])
    return a

print("Part 1:", func(3, 1))
print("Part 2:", math.prod(func(i, 1) for i in range(1,9,2)) * func(1, 2))