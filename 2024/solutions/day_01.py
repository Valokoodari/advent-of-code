def part_1(data):
    ll, lr = zip(*[(int(l), int(r)) for l, r in [line.split() for line in data.splitlines()]])
    return sum(abs(l - r) for l, r in zip(*[sorted(ll), sorted(lr)]))


def part_2(data):
    ll, lr = zip(*[(int(l), int(r)) for l, r in [line.split() for line in data.splitlines()]])
    return sum(n * lr.count(n) for n in ll)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(1, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
