LS = { "red": 12, "green": 13, "blue": 14 }


def part_1(data):
    ans = 0
    for l in data.splitlines():
        (g, ss), v = l.split(":"), True
        for s in ss.split(";"):
            for c in s.split(","):
                n, c = c.strip().split();
                if LS[c] < int(n):
                    v = False
            if not v:
                break
        ans += int(g.split()[1]) if v else 0
    return ans


def part_2(data):
    ans = 0
    for line in data.splitlines():
        cs = { "red": 0, "green": 0, "blue": 0 }
        _, ss = line.split(":")
        for s in ss.split(";"):
            for c in s.split(","):
                n, c = c.strip().split(" ");
                cs[c] = max(int(n), cs[c])
        ans += cs["red"] * cs["green"] * cs["blue"]
    return ans


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(2, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
