def solve(data, l):
    pss, vs = [[0, 0] for _ in range(l)], set()

    for line in data.splitlines():
        d, s = line[0], int(line[1:])

        for _ in range(s):
            pss[0][0] += 1 if d == "R" else -1 if d == "L" else 0
            pss[0][1] += 1 if d == "U" else -1 if d == "D" else 0

            for i in range(1, len(pss)):
                r = abs(pss[i-1][0] - pss[i][0]) + abs(pss[i-1][1] - pss[i][1])
                if r > 2 or r > 1 and (pss[i-1][0] == pss[i][0] or pss[i-1][1] == pss[i][1]):
                    pss[i][0] += 1 if pss[i-1][0] > pss[i][0] else - 1 if pss[i-1][0] < pss[i][0] else 0
                    pss[i][1] += 1 if pss[i-1][1] > pss[i][1] else - 1 if pss[i-1][1] < pss[i][1] else 0

            vs.add(tuple(pss[l-1]))

    return len(vs)


def part_1(data):
    return solve(data, 2)

def part_2(data):
    return solve(data, 10)


EX_0 = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

EX_1 = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

def test():
    assert part_1(EX_0) == 13
    assert part_2(EX_0) == 1
    assert part_2(EX_1) == 36


if __name__ == "__main__":
    test()
