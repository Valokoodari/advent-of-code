ls = [l.strip() for l in open("inputs/17.txt").read().strip().splitlines()]
ta = [tuple(map(int, l.strip()[2:].split(".."))) for l in ls[0][13:].split(",")]

c, vxs = 0, set()
for iv in range(int((ta[0][0]*2)**0.5), ta[0][1]+1):
    p, v = 0, iv
    while True:
        p += v
        v = v - 1 if v > 0 else 0
        if ta[0][0] <= p <= ta[0][1]:
            vxs.add(iv)
            break
        if p > ta[0][1]:
            break

for ivx in vxs:
    for ivy in range(ta[1][0],-ta[1][0]+1):
        p, vx, vy = [0, 0], ivx, ivy
        while True:
            p[0] += vx
            p[1] += vy
            vy -= 1
            vx = vx - 1 if vx > 0 else vx + 1 if vx < 0 else vx
            if ta[0][0] <= p[0] <= ta[0][1] and ta[1][0] <= p[1] <= ta[1][1]:
                c += 1
                break
            if p[0] > ta[0][1] or p[1] < ta[1][0]:
                break

print(f"Part 1: {ta[1][0]*(ta[1][0]+1)//2}")
print(f"Part 2: {c}")