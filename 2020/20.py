#!venv/bin/python3
import math

rt = lambda t: list(zip(*t[::-1]))
fh = lambda t: [r[::-1] for r in t]
ch = lambda t1,t2: "".join(t1[9]) == "".join(t2[0])
cv = lambda t1,t2: ch(rt(t1), rt(t2))

## Parsing
ts = {int(l[0][5:-1]): [[c for c in l[i]] for i in range(1, len(l))] for l in [l.strip().split("\n") for l in open("inputs/20.in", "r").read().split("\n\n")]}

# Part 1
ns = {}
for key,tile in ts.items():
    fits = []
    for k,t in ts.items():
        if key == k: continue
        for i in range(4):
            for j in range(4):
                t = rt(t)
                if ch(t, tile) or ch(fh(t), tile) and k not in fits:
                    fits.append(k)
            tile = rt(tile)
    ns[key] = fits

cs = [k for k,v in ns.items() if len(v) == 2]
es = [k for k,v in ns.items() if len(v) == 3]
ms = [k for k,v in ns.items() if len(v) == 4]

print("Part 1:", math.prod(cs))

# Part 2

## Find the es
def ne(used, ti):
    used.append(ti)
    n = ns[ti]
    for t in n:
        if t not in used and t in es:
            ne(used, t)
        if t not in used and t in cs:
            used.append(t)

ees = []
for c in cs:
    for ti in ns[c]:
        used = [c]
        ne(used, ti)
        if used not in ees and used[::-1] not in ees:
            ees.append(used)


## Build the grid
grid = [[0]*12 for _ in range(12)]

## Manually build the edges
# for e in ees: print(e)
for i,t in enumerate(ees[0]):
    grid[i][0] = t
for i,t in enumerate(ees[1]):
    grid[0][i] = t
for i,t in enumerate(ees[3]):
    grid[11][i] = t
for i,t in enumerate(ees[2]):
    grid[i][11] = t

## Fill the grid
used = []
while 0 in [n for i in range(12) for n in grid[i]]:
    for k in ms:
        t = ts[k]
        for i in range(1,11):
            for j in range(1,11):
                ps = [grid[i-1][j], grid[i][j-1], grid[i][j+1], grid[i+1][j]]
                if sum(ps) == 0: continue

                s1 = sum([1 for g in ps if g == 0])
                s2 = sum([1 for g in ps if g in ns[k]])

                if ((s1 == 0 and s2 == 4) or (s1 == 1 and s2 == 3) or (s1 == 2 and s2 == 2)) and k not in used:
                    used.append(k)
                    grid[i][j] = k

photo = [[ts[n] for n in row] for row in grid]

## Orient the first piece (manual)
photo[0][0] = rt(rt(fh(photo[0][0])))

## Orient the first row
for c in range(2, 12):
    l = photo[0][c-1]

    if cv(l, photo[0][c]): continue

    for i in range(4):
        photo[0][c] = rt(photo[0][c])
        if cv(l, photo[0][c]):
            break
    if cv(l, photo[0][c]): continue
    
    photo[0][c] = fh(photo[0][c])
    for i in range(4):
        photo[0][c] = rt(photo[0][c])
        if cv(l, photo[0][c]):
            break

## Orient other rows
for r in range(1, 12):
    for c in range(12):
        u = photo[r-1][c]

        if ch(u, photo[r][c]): continue

        for i in range(4):
            photo[r][c] = rt(photo[r][c])
            if ch(u, photo[r][c]):
                break
        
        if ch(u, photo[r][c]): continue

        photo[r][c] = fh(photo[r][c])
        for i in range(4):
            photo[r][c] = rt(photo[r][c])
            if ch(u, photo[r][c]):
                break

## Combine the picture
pic = ["".join(["".join(t[r][1:-1]) for t in p]) for p in photo for r in range(1, 9)]

## Find all of the monsters
MS = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")
mps = [(i,j) for i in range(len(MS)) for j in range(len(MS[i])) if MS[i][j] == "#"]

mons = 0
for i in range(2):
    for i in range(4):
        mons += sum([1 for i in range(len(pic)-len(MS)+1) for j in range(len(pic[i])-len(MS[0])+1) if sum([1 for a,b in mps if pic[i+a][j+b] == "#"]) == len(mps)])
        pic = rt(pic)
    pic = fh(pic)

print("Part 2:", sum([r.count("#") for r in pic]) - len(mps)*mons)