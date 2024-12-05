from collections import defaultdict


def parse(data):
    rs, us, os = *data.split("\n\n"), defaultdict(list)
    for a, b in [[int(n) for n in l.split("|")] for l in rs.splitlines()]:
        os[a].append(b)
    return os, [[int(n) for n in u.split(",")] for u in us.splitlines()]


def part_1(data):
    rs, us = parse(data)
    return sum(ns[len(ns)//2] if sum(1 if ns[j] in rs and n in rs[ns[j]] else 0 for i,n in enumerate(ns) for j in range(i+1, len(ns))) == 0 else 0 for ns in us)


def part_2(data):
    ans, rs, us = 0, *parse(data)
    for ns in us:
        f, p = False, True
        while p:
            p = False
            for i, n in enumerate(ns):
                for j in range(i+1, len(ns)):
                    if n in rs[ns[j]]:
                        ns[i], ns[j], p, f = ns[j], ns[i], True, True
            if not p and f:
                ans += ns[len(ns)//2]
    return ans


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(5, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
