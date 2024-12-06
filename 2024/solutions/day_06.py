DS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def parse(data):
    ws, p = set(), (0, 0)
    for r, l in enumerate(data.splitlines()):
        for c, w in enumerate(l):
            if w == "#":
                ws.add((r, c))
            if w == "^":
                p = (r, c)
    return ws, p, (len(data.splitlines()), len(data.splitlines()[0]))


def walk(ws, p, s):
    vs, d = set(), 0
    while True:
        cp, p = p, (p[0] + DS[d][0], p[1] + DS[d][1])
        if p in ws:
            p, d = cp, (d + 1) % 4
            continue
        if p[0] < 0 or p[1] < 0 or p[0] >= s[0] or p[1] >= s[1]:
            return set(p[:2] for p in vs), -1
        if (p[0], p[1], d) in vs:
            break
        vs.add((p[0], p[1], d))
    return set(p[:2] for p in vs), 0


def part_1(data):
    return len(walk(*parse(data))[0])


def part_2(data):
    ans, ws, p, s = 0, *parse(data)
    for o in walk(ws, p, s)[0]:
        if walk(ws.union({o}), p, s)[1] == 0:
            ans += 1
    return ans


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(6, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
