def f1(p):
    for r in range(1, len(p)):
        if all(p[:r][-i-1] == p[r:][i] for i in range(min(len(p[:r]), len(p[r:])))):
            return r
    return 0


def f2(p):
    for r in range(1, len(p)):
        d = 0
        for i in range(min(len(p[:r]), len(p[r:]))):
            d += sum(p[:r][-i-1][j] != p[r:][i][j] for j in range(len(p[:r][-i-1])))
            if d > 1:
                break
        if d == 1:
            return r
    return 0


def part_1(data):
    return sum(f1(p)*100 + f1(list(zip(*p))) for p in [p.splitlines() for p in data.split("\n\n")])


def part_2(data):
    return sum(f2(p)*100 + f2(list(zip(*p))) for p in [p.splitlines() for p in data.split("\n\n")])


EX_0 = """\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 405
    assert part_2(EX_0) == 400


if __name__ == "__main__":
    test()
