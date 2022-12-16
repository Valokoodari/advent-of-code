ns = [int(l.strip()) for l in open("../inputs/2020/10.txt", "r").readlines()]

ns.extend([0, max(ns)+3])
ns.sort()

d1 = sum(1 for i in range(0, len(ns)) if ns[i] - ns[i-1] == 1)
a1 = d1 * sum(1 for i in range(0, len(ns)) if ns[i] - ns[i-1] == 3)

p = [*[1], *[0]*(len(ns)-1)]
for i in range(1, len(p)):
    for j in range(0, i):
        if ns[i] - ns[j] <= 3:
            p[i] += p[j]

print("Part 1:", a1)
print("Part 2:", p[-1])