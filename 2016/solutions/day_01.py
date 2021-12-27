DS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def part_1(data):
    ms, d, p = [(m[0], int(m[1:])) for m in data.split(", ")], 0, (0, 0)

    for t, m in ms:
        d = (d + (1 if t == 'R' else -1)) % len(DS)
        p = (p[0] + DS[d][0]*m, p[1] + DS[d][1]*m)

    return sum(map(abs, p))


def part_2(data):
    ms, d, p, ps = [(m[0], int(m[1:])) for m in data.split(", ")], 0, (0,0), {(0,0)}

    for t, m in ms:
        d = (d + (1 if t == 'R' else -1)) % len(DS)
        for _ in range(m):
            p = (p[0] + DS[d][0], p[1] + DS[d][1])
            if p in ps:
                return sum(map(abs, p))
            ps.add(p)
    return -1


def test():
    assert(part_1("R2, L3") == 5)
    assert(part_1("R2, R2, R2") == 2)
    assert(part_1("R5, L5, R5, R3") == 12)

    assert(part_2("R8, R4, R4, R8") == 4)