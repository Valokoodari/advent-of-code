parse = lambda d: [({ c: cs.count(c) for c in cs }, b, cs, 0) for cs, b in [l.split() for l in d.splitlines()]]

CS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def sh(x, cs):
    f = 0
    if x[3] == 5 or max(x[0].values()) + x[3] == 5:
        f = 6
    elif max(x[0].values()) + x[3] == 4:
        f = 5
    elif max(x[0].values()) + x[3] == 3:
        f = 3
        if min(x[0].values()) == 2:
            f = 4
    elif max(x[0].values()) + x[3] == 2:
        f = 1
        if list(x[0].values()).count(2) == 2:
            f = 2
    return (f, tuple(cs.index(c) for c in x[2]))


def part_1(data):
    return sum(int(c[1]) * (i + 1) for i, c in enumerate(sorted(parse(data), key=lambda h: sh(h, CS))))


def part_2(data):
    hs = [({ k: v for k, v in c[0].items() if k != "J" }, c[1], c[2], c[0].get("J", 0)) for c in parse(data)]
    return sum(int(c[1]) * (i + 1) for i, c in enumerate(sorted(hs, key=lambda h: sh(h, ["J", *CS]))))


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(7, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
