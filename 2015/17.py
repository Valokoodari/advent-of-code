from itertools import combinations

cs = [int(l.strip()) for l in open("inputs/17.in").read().strip().splitlines()]
ws = [w for i in range(len(cs)) for w in combinations(cs, i+1) if sum(w) == 150]
m = min([len(com) for com in ws])

print(f"Part 1: {len(ws)}")
print(f"Part 2: {len([com for com in ws if len(com) == m])}")