ls = [l.strip() for l in open("inputs/17.txt").read().strip().splitlines()]
ta = [list(map(int, l.strip()[2:].split(".."))) for l in ls[0][13:].split(",")]

a1, a2 = 0, 0
for ivx in range(max(ta[0])+1):
    for ivy in range(min(ta[1]),max(ta[0])+1):
        my, pos = 0, [0, 0]
        vx, vy = ivx, ivy
        while True:
            pos[0] += vx
            pos[1] += vy
            my = max(my, pos[1])
            vy -= 1
            vx = vx - 1 if vx > 0 else vx + 1 if vx < 0 else vx
            if min(ta[0]) <= pos[0] <= max(ta[0]) and min(ta[1]) <= pos[1] <= max(ta[1]):
                a1, a2 = max(a1, my), a2 + 1
                break
            if pos[0] > max(ta[0]) or pos[1] < min(ta[1]):
                break

print(f"Part 1: {a1}\nPart 2: {a2}")
