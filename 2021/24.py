bs = [tuple(int(b.splitlines()[i][5:]) for i in (3,4,14)) for b in open("inputs/24.txt").read().strip().split("inp w\n")[1:]]

ss, a1, a2 = [], [0]*14, [0]*14
for i in range(len(bs)):
    if bs[i][0] == 1:
        ss.append(i)
    else:
        j = ss.pop()
        d = bs[j][2] + bs[i][1]
        if d < 0:
            i, j, d = j, i, -d
        a1[i], a1[j] = 9, 9-d
        a2[j], a2[i] = 1, 1+d

print(f"Part 1: {''.join(map(str, a1))}")
print(f"Part 2: {''.join(map(str, a2))}")