ls = [l.strip() for l in open("inputs/17.txt").read().strip().splitlines()]
ta = [tuple(map(int, l.strip()[2:].split(".."))) for l in ls[0][13:].split(",")]

a2 = 0
for ivx in range(int((ta[0][0]*2)**0.5), ta[0][1]+1):
    for ivy in range(ta[1][0],-ta[1][0]+1):
        pos, vx, vy = [0, 0], ivx, ivy
        while True:
            pos[0] += vx
            pos[1] += vy
            vy -= 1
            vx = vx - 1 if vx > 0 else vx + 1 if vx < 0 else vx
            if ta[0][0] <= pos[0] <= ta[0][1] and ta[1][0] <= pos[1] <= ta[1][1]:
                a2 += 1
                break
            if pos[0] > ta[0][1] or pos[1] < ta[1][0]:
                break

print(f"Part 1: {ta[1][0]*(ta[1][0]+1)//2}")
print(f"Part 2: {a2}")
