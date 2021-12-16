a1, d = 0, "".join("{:04b}".format(int(c,16)) for c in open("inputs/16.txt").read().strip())

ts = {
    0: sum,
    1: lambda x: eval("*".join(str(y) for y in x)),
    2: min,
    3: max,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0,
}

def fpp(d):
    global a1
    a1, t, d, l, c = a1+int(d[:3], 2), int(d[3:6], 2), d[6:], "", ""

    if t == 4:
        while c != "0":
            c, l, d = d[0], l+d[1:5], d[5:]
        return (int(l, 2), d)
    else:
        i, d, ns = d[0], d[1:], []
        if i == "0":
            l, d = int(d[:15], 2), d[15:]
            ps, d = d[:l], d[l:]
            while ps:
                x, ps = fpp(ps)
                ns.append(x)
        else:
            l, d = int(d[:11],2), d[11:]
            for _ in range(l):
                x, d = fpp(d)
                ns.append(x)
        return (ts[t](ns), d)

a2 = fpp(d)[0]
print(f"Part 1: {a1}\nPart 2: {fpp(d)[0]}")