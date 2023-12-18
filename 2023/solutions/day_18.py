DS = { "R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0) }


def solve(dns):
    sr, sc, sd, r, c = 0, 0, 0, 0, 0
    for d, n in dns:
        sr, sc, sd = sr + DS[d][0] * n * c, sc + DS[d][1] * n * r, sd + n
        r, c = r + DS[d][0] * n, c + DS[d][1] * n
    return abs(sr - sc) // 2 + sd // 2 +1


def part_1(data):
    return solve([(d, int(n)) for d, n, _ in [l.split() for l in data.splitlines()]])


def part_2(data):
    return solve([(list(DS)[int(c[-2])], int(c[2:-2], 16)) for c in [l.split()[2] for l in data.splitlines()]])


EX_0 = """\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 62
    assert part_2(EX_0) == 952408144115


if __name__ == "__main__":
    test()
