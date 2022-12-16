ls = [[l[0], int(l[1:])] for l in open("../inputs/2020/12.txt", "r").readlines()]

ms = { "N": [1, 0], "S": [-1, 0], "E": [0, 1], "W": [0, -1] }
ds = { 0: "N", 90: "E", 180: "S", 270: "W" }
rs = { "R": [-1, 1], "L": [1, -1] }

p1,d,p2,wp = [0, 0],90,[0, 0],[1, 10]
for l in ls:
    if l[0] in ms:
        p1 = [p1[i] + ms[l[0]][i] * l[1] for i in range(2)]
        wp = [wp[i] + ms[l[0]][i] * l[1] for i in range(2)]
    if l[0] == "F":
        p1 = [p1[i] + ms[ds[d]][i] * l[1] for i in range(2)]
        p2 = [p2[i] + wp[i] * l[1] for i in range(2)]
    if l[0] in rs:
        d = (d + rs[l[0]][1] * l[1]) % 360
        for i in range(0, l[1]//90):
            wp = [rs[l[0]][0] * wp[1], rs[l[0]][1] * wp[0]]

print("Part 1:", abs(p1[0])+abs(p1[1]))
print("Part 2:", abs(p2[0])+abs(p2[1]))