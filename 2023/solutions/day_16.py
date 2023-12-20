DS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
RS = {
    ".": [[0], [1], [2], [3]],
    "-": [[1, 3], [1], [1, 3], [3]],
    "|": [[0], [0, 2], [2], [0, 2]],
    "/": [[1], [0], [3], [2]],
    "\\": [[3], [2], [1], [0]],
}


def fm(ms, r, c, d):
    q, vs = [(r, c, d)], set()
    while q:
        if (s := q.pop()) in vs:
            continue
        vs.add(s)
        for nd in RS[ms[s[0]][s[1]]][s[2]]:
            if 0 <= s[0] + DS[nd][0] < len(ms) and 0 <= s[1] + DS[nd][1] < len(ms[0]):
                q.append((s[0] + DS[nd][0], s[1] + DS[nd][1], nd))
    return len({(r, c) for r, c, _ in vs})


def part_1(data):
    return fm(data.splitlines(), 0, 0, 1)


def part_2(data):
    ms, cs = data.splitlines(), []
    for r in range(len(ms)):
        cs.append((r, 0, 1))
        cs.append((r, len(ms[0])-1, 3))
    for c in range(len(ms[0])):
        cs.append((0, c, 2))
        cs.append((len(ms)-1, c, 0))
    return max(fm(ms, *c) for c in cs)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(16, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
