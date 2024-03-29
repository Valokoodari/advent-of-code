from math import ceil, floor, prod


def sr(t, d):
    return ceil((t + (t**2 - 4*d) ** 0.5) / 2) - floor((t - (t**2 - 4*d) ** 0.5) / 2) - 1


def part_1(data):
    ns = [[int(n) for n in l.split()[1:]] for l in data.splitlines()]
    return prod(sr(*n) for n in list(zip(*ns)))


def part_2(data):
    return sr(*[int(l.split(":")[1]) for l in data.replace(" ", "").splitlines()])


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(6, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
