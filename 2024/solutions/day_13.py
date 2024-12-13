def solve(data, o = 0):
    c, ms = 0, [[[int(n.strip()[2:]) for n in l.split(":")[1].split(",")] for l in m.splitlines()] for m in data.split("\n\n")]

    for m in ms:
        m[2] = [m[2][0] + o, m[2][1] + o]
        a = round((m[1][1]*m[2][0]-m[1][0]*m[2][1])/(m[0][0]*m[1][1]-m[1][0]*m[0][1]))
        b = round((-m[0][1]*m[2][0]+m[0][0]*m[2][1])/(m[0][0]*m[1][1]-m[1][0]*m[0][1]))

        if a*m[0][0]+b*m[1][0] == m[2][0] and a*m[0][1]+b*m[1][1] == m[2][1]:
            c += 3 * a + b
    return c


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 10000000000000)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(13, part_1, part_2, False)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
