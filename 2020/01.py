import itertools as it, math

ns = list(map(int, open("../inputs/2020/01.txt", "r").readlines()))

def func(n):
    for a in it.combinations(ns, n):
        if sum(a) == 2020: return math.prod(a)

print("Part 1:", func(2))
print("Part 2:", func(3))