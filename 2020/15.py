ts = {int(n): i for i,n in enumerate(open("../inputs/2020/15.txt", "r").readline().split(","))}

a1,l = 0,ts.popitem()[0]
for i in range(len(ts), 30000000-1):
    a = i - ts[l] if l in ts else 0
    ts[l],l = i,a
    if i+2 == 2020: a1 = a

print("Part 1:", a1)
print("Part 2:", l)