import math

ls = open("../inputs/2020/13.txt", "r").readlines()
ft,bs = int(ls[0]), { int(r): i for i,r in enumerate(ls[1].split(",")) if r != "x" }

a1 = []
for t in range(ft, ft+sum(bs)):
    for n in [b*(t-ft) for b in bs if t % b == 0]: a1.append(n)

t = list(bs.keys())[0]
while True:
    match = [k for k,v in bs.items() if (t+v) % k == 0]
    if len(match) == len(bs): break
    t += math.prod(match)

print("Part 1:", a1[0])
print("Part 2:", t)