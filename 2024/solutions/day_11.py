from collections import Counter


def solve(data, b = 25):
    ns = Counter([int(n) for n in data.split()])
    for _ in range(b):
        nns = Counter()
        for s, c in ns.items():
            if s == 0:
                nns[1] += c
            elif len(str(s)) % 2 == 0:
                nns[int(str(s)[:len(str(s))//2])] += c
                nns[int(str(s)[len(str(s))//2:])] += c
            else:
                nns[s * 2024] += c
        ns = nns
    return sum(ns.values())


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 75)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(11, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
