def parse(d):
    ps = [p.splitlines() for p in d.split("\n\n")]
    ss = [int(x) for x in ps[0][0].split(": ")[1].split()]
    ms = [[[int(x) for x in l.split()] for l in p[1:]] for p in ps[1:]]
    return ss, ms


def part_1(data):
    ss, ms = parse(data)
    for i in range(len(ss)):
        for m in ms:
            for v in m:
                if v[1] <= ss[i] < v[1] + v[2]:
                    ss[i] += v[0] - v[1]
                    break

    return min(ss)


def part_2(data):
    ss, ms = parse(data)
    rs = [(ss[i], ss[i+1] + ss[i] - 1) for i in range(0, len(ss), 2)]

    for p in ms:
        nrs = []
        for v in p:
            crs = []
            for r in rs:
                if not (r[0] >= v[1] + v[2] or r[1] < v[1]):
                    a, b = max(v[1], r[0]), min(v[1] + v[2] - 1, r[1])
                    nrs.append((a + v[0] - v[1], b + v[0] - v[1]))
                    if r[0] < a:
                        crs.append((r[0], a - 1))
                    if r[1] > b:
                        crs.append((b + 1, r[1]))
                else:
                    crs.append(r)
            rs = crs
        rs = crs + nrs

    return min(r[0] for r in rs)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(5, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
