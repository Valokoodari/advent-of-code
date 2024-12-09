data = open("../inputs/2024/09/input.txt").read().rstrip()


def defraq(fs):
    i = -1
    while i < len(fs) - 1:
        f, l, i = *fs[-i-2], i+1
        if f == -1:
            continue
        for j in range(len(fs)-i-1):
            g, s = fs[j]
            if g == -1 and s >= l:
                fs[j] = (g, s - l)
                fs.insert(j, fs.pop(-i-1))
                fs.insert(-i-1, (-1, l))
                break
    i = 0
    while i < len(fs) - 1:
        if fs[i][0] == -1 and fs[i+1][0] == -1:
            fs[i] = (-1, fs[i][1] + fs[i+1][1])
            fs.pop(i+1)
        else:
            i += 1
    return fs


def highest(fs):
    bs, h = [f for f, l in fs for _ in range(l)], 0
    for i, f in enumerate(bs):
        if f != -1:
            h = i
    return h


fs, i, f = [], 0, False
for c in data:
    n, f = int(c), not f
    if f:
        fs.append((i, n))
        i += 1
    else:
        fs.append((-1, n))

i, h = 0, 0
while h != (h := highest(fs)):
    fs = defraq(fs)
    i += 1

print("Part 3:", h * 100 + i - 1)
