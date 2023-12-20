NS = {
    "|": ((1, 0), (-1, 0)),
    "-": ((0, 1), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
}


def solve(data):
    s, nss, sn = (-1, -1), [[[] for _ in line] for line in data.splitlines()], set()
    for r, line in enumerate(data.splitlines()):
        for c, char in enumerate(line):
            if char == "S":
                s = (r, c)
            if char not in NS:
                continue
            nss[r][c] = [(r+dr, c+dc) for dr, dc in NS[char]]
    for r, ns in enumerate(nss):
        for c, n in enumerate(ns):
            if s in n:
                sn.add((r-s[0], c-s[1]))
                nss[s[0]][s[1]].append((r, c))

    vs, p, l = set([s]), nss[s[0]][s[1]][0], s
    while p != s:
        vs.add(p)
        n = nss[p[0]][p[1]]
        l, p = p, n[1] if n[0] == l else n[0]

    return (vs, s, sn)


def part_1(data):
    return len(solve(data)[0]) // 2


def part_2(data):
    ls, ans = [[c for c in l] for l in data.splitlines()], 0
    vs, s, sn = solve(data)
    for k, v in NS.items():
        if sn == set(v):
            ls[s[0]][s[1]] = k
            break

    for r, cs in enumerate(ls):
        i = False
        for c, ch in enumerate(cs):
            i = not i if (r, c) in vs and ch in "|LJ" else i
            ans += 1 if i and (r, c) not in vs else 0

    return ans


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(10, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)

