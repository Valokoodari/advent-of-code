ls = [l.split(",") for l in open("../inputs/2015/14.txt").read().strip()
    .replace(" can fly ", ",")
    .replace(" km/s for ", ",")
    .replace(" seconds, but then must rest for ", ",")
    .replace(" seconds.", "")
    .splitlines()]
ls = [[l[0], int(l[1]), int(l[2]), int(l[3]), True, 0, 0, 0] for l in ls]

for _ in range(2503):
    for l in ls:
        if (l[5] == l[2] and l[4]) or (l[5] == l[3] and not l[4]):
            l[5],l[4] = 0, not l[4]
        if l[4]:
            l[6] += l[1]
        l[5] += 1
    m = max(ls, key=lambda l: l[6])[6]
    for l in ls:
        if l[6] == m:
            l[7] += 1

print(f"Part 1: {max(ls, key=lambda l: l[6])[6]}")
print(f"Part 2: {max(ls, key=lambda l: l[7])[7]}")