f,s,fs,os = 0,0,[],[[int(c) for c in l.strip()] for l in open("inputs/11.in").read().strip().splitlines()]

def ff(os, x, y):
    global fs
    fs[x][y] = 1
    for r,c in [(i,j) for i in range(x-1, x+2) for j in range(y-1, y+2) if 0 <= i < len(os) and 0 <= j < len(os[0]) and (i, j) != (x, y)]:
        os[r][c] += 1
        if not fs[r][c] and os[r][c] > 9:
            ff(os, r, c)

while True:
    fs = [[0] * len(r) for r in os]
    for i,r in enumerate(os):
        for j,c in enumerate(r):
            os[i][j] += 1
            if os[i][j] > 9 and not fs[i][j]:
                ff(os, i, j)
    os = [[0 if c > 9 else c for c in r] for r in os]
    s, c = s+1, sum(sum(r) for r in fs)
    if s <= 100: f += c
    if c == len(os) * len(os[0]):
        break

print(f"Part 1: {f}\nPart 2: {s}")