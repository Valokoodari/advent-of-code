from types import new_class


ls = [[0 if c == '.' else 1 for c in l] for l in open("inputs/18.in").read().strip().splitlines()]
ls2 = [l[:] for l in ls]

def fco(ls):
    ls[0][0] = 1
    ls[0][len(ls[0])-1] = 1
    ls[len(ls)-1][0] = 1
    ls[len(ls)-1][len(ls[0])-1] = 1
    return ls

ns = [(dx,dy) for dx in range(-1,2) for dy in range(-1,2) if not (dx == 0 and dy == 0)]

for _ in range(100):
    ls2 = fco(ls2)
    nls = [[0]*len(ls[0]) for _ in range(len(ls))]
    nls2 = [[0]*len(ls2[0]) for _ in range(len(ls2))]
    for x in range(len(ls)):
        for y in range(len(ls[0])):
            s = sum(ls[x+dx][y+dy] for dx,dy in ns if 0 <= x+dx < len(ls) and 0 <= y+dy < len(ls[0]))
            if ls[x][y] == 1:
                nls[x][y] = 1 if s in [2,3] else 0
            else:
                nls[x][y] = 1 if s == 3 else 0
            s2 = sum(ls2[x+dx][y+dy] for dx,dy in ns if 0 <= x+dx < len(ls2) and 0 <= y+dy < len(ls2[0]))
            if ls2[x][y] == 1:
                nls2[x][y] = 1 if s2 in [2,3] else 0
            else:
                nls2[x][y] = 1 if s2 == 3 else 0
    ls, ls2 = nls, nls2

print(sum(sum(l) for l in ls))
print(sum(sum(l) for l in fco(ls2)))