ns = sorted([int(n) for n in open("inputs/07.in").read().split(",")])

print(f"Part 1: {sum([abs(n - ns[len(ns)//2]) for n in ns])}")
print(f"Part 2: {sum(sum(range(abs(n - sum(ns)//len(ns)) + 1)) for n in ns)}")