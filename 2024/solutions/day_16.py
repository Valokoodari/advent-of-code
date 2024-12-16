from heapq import heappop, heappush


def solve(data, t = 1):
    s, e, data = (0,0), (0,0), data.splitlines()
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "S":
                s = (r, c)
            if data[r][c] == "E":
                e = (r, c)

    q, vs, m, mm = [(0, s[0], s[1], 0, [s])], {}, -1, set()
    while q:
        l, r, c, d, p = heappop(q)
        if m != -1 and l > m:
            return len(mm)
        if (r, c, d) in vs:
            if t == 1 or vs[(r, c, d)] < l:
                continue
        vs[(r, c, d)] = l
        if (r, c) == e:
            if m == -1:
                m = l
            mm.update(p)
            if t == 1:
                return l
        dr, dc = ((0,1), (1,0), (0,-1), (-1,0))[d]
        if 0 <= (nr := r+dr) < len(data) and 0 <= (nc := c+dc) < len(data[0]) and data[nr][nc] != "#":
            heappush(q, (l+1, nr, nc, d, p+[(nr,nc)]))
        heappush(q, (l+1000, r, c, (d+1)%4, p))
        heappush(q, (l+1000, r, c, (d+3)%4, p))


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 2)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(16, part_1, part_2, False)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
