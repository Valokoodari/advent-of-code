ls = [l.strip().split(" ")[1:] for l in open("inputs/16.in").read().strip().splitlines()]

eq = lambda a, b: a == b
gt = lambda a, b: a > b
lt = lambda a, b: a < b

tt = {
    "children": (3, eq),
    "cats": (7, gt),
    "samoyeds": (2, eq),
    "pomeranians": (3, lt),
    "akitas": (0, eq),
    "vizslas": (0, eq),
    "goldfish": (5, lt),
    "trees": (3, gt),
    "cars": (2, eq),
    "perfumes": (1, eq)
}

ls = {int(l[0][:-1]): {
    l[1][:-1]: int(l[2][:-1]),
    l[3][:-1]: int(l[4][:-1]),
    l[5][:-1]: int(l[6])
} for l in ls}

for i in range(1, len(ls) + 1):
    if all(ls[i][k] == tt[k][0] for k in ls[i]):
        print(f"Part 1: {i}")

for i in range(1, len(ls) + 1):
    if all(tt[k][1](ls[i][k], tt[k][0]) for k in ls[i]):
        print(f"Part 2: {i}")