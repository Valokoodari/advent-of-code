from collections import defaultdict


def fc(d, ps):
    dp = defaultdict(int)
    dp[""] = 1
    for i in range(len(d) - 1, -1, -1):
        s = d[i:]
        for p in ps:
            if s.startswith(p):
                dp[s] += dp[s[len(p):]]
    return dp[d]


def part_1(data):
    ps, ds = data.split("\n\n")
    return sum(1 for d in ds.splitlines() if fc(d, ps.split(", ")))


def part_2(data):
    ps, ds = data.split("\n\n")
    return sum(fc(d, ps.split(", ")) for d in ds.splitlines())


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(19, part_1, part_2, False)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
