def part_1(data):
    cs = [[[int(n) for n in ns.split()] for ns in c[1].split("|")] for c in [l.split(":") for l in data.splitlines()]]
    return sum(int(2 ** (len(set(c[0]) & set(c[1])) - 1)) for c in cs)


def part_2(data):
    cs = {int(c[0].split()[1]): [[int(n) for n in ns.split()] for ns in c[1].split("|")] for c in [l.split(":") for l in data.splitlines()]}
    ss = {c: 0 for c in cs}
    for k, c in cs.items():
        ss[k] += 1
        for i in range(len(set(c[0]) & set(c[1]))):
            ss[k+i+1] += ss[k]
    return sum(ss.values())


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(4, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
