import re

l = [re.split("[- :\n]", l) for l in open("../inputs/2020/02.txt", "r").readlines()]

a,b = 0,0
for p in l:
    if int(p[0]) <= p[4].count(p[2]) <= int(p[1]): a += 1
    if (p[4][int(p[0])-1] == p[2]) ^ (p[4][int(p[1])-1] == p[2]): b += 1

print("Part 1:", a)
print("Part 2:", b)