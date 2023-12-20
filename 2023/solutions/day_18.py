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


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(18, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
