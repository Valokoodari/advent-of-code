from collections import deque
from itertools import product

L = 100


def parse(d):
    ms = [l for l in d.splitlines()]
    for r, l in enumerate(ms):
        for c, v in enumerate(l):
            if v == "S":
                s = (r, c)
            elif v == "E":
                e = (r, c)
    return ms, s, e


def bfs(ms, s):
    q, ds = deque([(s, 0)]), [[-1]*len(ms[0]) for _ in range(len(ms))]
    while q:
        (r, c), d = q.popleft()
        if ds[r][c] != -1:
            continue
        ds[r][c] = d
        for dr, dc in ((-1,0),(0,1),(1,0),(0,-1)):
            if 0 <= (nr := r+dr) < len(ms) and 0 <= (nc := c+dc) < len(ms[0]) and ms[nr][nc] != "#":
                q.append(((nr, nc), d+1))
    return ds


def solve(d, t):
    ms, s, e = parse(d)
    fs, fe, ss = bfs(ms, s), bfs(ms, e), []
    for r, c in product(range(len(ms)), range(len(ms[0]))):
        if fs[r][c] == -1:
            continue
        for dr, dc in product(range(-t, t+1), range(-t, t+1)):
            if abs(dr) + abs(dc) <= t and 0 <= (nr := r+dr) < len(ms) and 0 <= (nc := c+dc) < len(ms[0]) and fe[nr][nc] != -1:
                ss.append(fs[e[0]][e[1]] - fs[r][c] - fe[nr][nc] - abs(dr) - abs(dc))
    return sum(1 for s in ss if s >= L)


def part_1(data):
    return solve(data, 2)


def part_2(data):
    return solve(data, 20)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    global L
    l, L = L, 50
    run_tests(20, part_1, part_2, False)
    L = l


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
