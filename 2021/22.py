ls = [l.strip().split(",") for l in open("inputs/22.txt").read().strip().replace(" ", ",").replace("..", ",").replace("x=", "").replace("y=","").replace("z=","").splitlines()]
ls = list(map(lambda l: tuple([l[0] == "on"] + list(map(int, l[1:]))), ls))

def fgi(c0, c1):
    for a,b in ((0,1), (2,3), (4,5)):
        if c1[a] > c0[b] or c1[b] < c0[a]:
            return None
    return (max(c0[0], c1[0]), min(c0[1], c1[1]), max(c0[2], c1[2]), min(c0[3], c1[3]), max(c0[4], c1[4]), min(c0[5], c1[5]))

def fgd(c, i):
    cs = [
        (c[0], i[0]-1, c[2], c[3], c[4], c[5]),
        (i[1]+1, c[1], c[2], c[3], c[4], c[5]),
        (i[0], i[1], c[2], i[2]-1, c[4], c[5]),
        (i[0], i[1], i[3]+1, c[3], c[4], c[5]),
        (i[0], i[1], i[2], i[3], c[4], i[4]-1),
        (i[0], i[1], i[2], i[3], i[5]+1, c[5]),
    ]
    return [x for x in cs if x[0] <= x[1] and x[2] <= x[3] and x[4] <= x[5]]

cs = []
for l in ls:
    ncs = [l[1:]] if l[0] else []
    for c in cs:
        i = fgi(c, l[1:])
        ncs.extend(fgd(c, i) if i else [c])
    cs = ncs

print(f"Part 1: {sum(max(0, min(50,c[1])-max(-50,c[0])+1)*max(0, min(50,c[3])-max(-50,c[2])+1)*max(0, min(50,c[5])-max(-50,c[4])+1) for c in cs)}")
print(f"Part 2: {sum((c[1]-c[0]+1)*(c[3]-c[2]+1)*(c[5]-c[4]+1) for c in cs)}")