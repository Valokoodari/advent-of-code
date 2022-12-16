ds = [[c for c in [int(i) for i in l.split("\n")[1:]]] for l in open("../inputs/2020/22.txt", "r").read().split("\n\n")]

def p2(d1, d2, g):
    r1,r2,sw = [],[],0

    while d1 and d2:
        if d1 in r1 or d2 in r2:
            sw = 1
            break

        r1.append(d1.copy())
        r2.append(d2.copy())

        c1,c2 = d1.pop(0),d2.pop(0)
        if len(d1) >= c1 and len(d2) >= c2 and g == 2:
            sw,_ = p2(d1[:c1], d2[:c2], 2)
        else:
            sw = 1 if c1 > c2 else 2

        if sw == 1:
            d1 += [c1, c2]
        else:
            d2 += [c2, c1]

    return sw, sum([s*(i+1) for i,s in enumerate(d1[::-1] if sw == 1 else d2[::-1])])

print("Part 1:", p2(ds[0].copy(), ds[1].copy(), 1)[1])
print("Part 2:", p2(ds[0], ds[1], 2)[1])