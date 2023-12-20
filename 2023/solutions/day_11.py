def solve(d, e = 2):
    mss = [[c for c in l] for l in d.splitlines()]
    ers = [i for i, l in enumerate(mss) if set(l) == {"."}]
    ecs = [i for i, l in enumerate(zip(*mss)) if set(l) == {"."}]

    ans, ss, e = 0, set(), e - 1
    for r, l in enumerate(mss):
        for c, ch in enumerate(l):
            if ch == ".":
                continue
            dr = e * sum(1 for n in ers if n < r) + r
            dc = e * sum(1 for n in ecs if n < c) + c
            ans += sum(abs(sr-dr) + abs(sc-dc) for sr, sc in ss)
            ss.add((dr, dc))

    return ans


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 1000000)


def test(run_tests = None, get_examples = None):
    if not run_tests:
        from solutions.test import run_tests
    if not get_examples:
        from solutions.test import get_examples
    run_tests(11, part_1, part_2)

    EX_0 = get_examples(11)[0]
    assert solve(EX_0, 10) == 1030
    assert solve(EX_0, 100) == 8410


if __name__ == "__main__":
    from test import run_tests, get_examples
    test(run_tests, get_examples)
