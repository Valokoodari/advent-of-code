def check(ns):
    if ns != (ss := sorted(ns)) and ns != ss[::-1]:
        return False
    p = ns[0]
    for n in ns[1::]:
        if not (0 < abs(n - p) < 4):
            return False
        p = n
    return True


def part_1(data):
    return sum(1 if check([int(n) for n in l.split()]) else 0 for l in data.splitlines())


def part_2(data):
    ans = 0
    for l in data.splitlines():
        if check(ns := [int(n) for n in l.split()]):
            ans += 1
        else:
            for i in range(len(ns)):
                if check(ns[:i:] + ns[i+1::]):
                    ans += 1
                    break
    return ans


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(2, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
