def calc(r, ns, t, i, p):
    return r == t if i == len(ns) else calc(r+ns[i], ns, t, i+1, p) or calc(r*ns[i], ns, t, i+1, p) or (p == 2 and calc(int(str(r)+str(ns[i])), ns, t, i+1, p))


def solve(d, p = 1):
    ans = 0
    for l in d.splitlines():
        t, *ns = [int(n) for n in l.replace(":","").split()]
        ans += t if calc(ns[0], ns, t, 1, p) else 0
    return ans


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 2)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(7, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
