from collections import defaultdict


def solve(data, t = 1):
    ms, h, w = [[c for c in r] for r in data.splitlines()], len(data.splitlines()), len(data.splitlines()[0])
    ans, vs = 0, [[False] * w for _ in range(h)]

    for r in range(h):
        for c in range(w):
            if vs[r][c]:
                continue
            a, p, s, q, vs[r][c], ps = 1, 0, 0, [(r, c)], True, defaultdict(set)
            while q:
                y, x = q.pop()
                for dy, dx in (DS := ((-1,0), (0,1), (1,0), (0,-1))):
                    if 0 <= (ny := y+dy) < h and 0 <= (nx := x+dx) < w and ms[ny][nx] == ms[y][x]:
                        if vs[ny][nx]:
                            continue
                        vs[ny][nx], a = True, a+1
                        q.append((ny, nx))
                    else:
                        p += 1
                        if t == 2:
                            ps[(dy, dx)].add((y, x))

            for ss in ps.values():
                vp = set()
                for d in ss:
                    q, s = ([], s) if d in vp else ([d], s+1)
                    while q:
                        if (np := q.pop()) in vp:
                            continue
                        vp.add(np)
                        q.extend((np[0]+dr, np[1]+dc) for dr, dc in DS if (np[0]+dr, np[1]+dc) in ss)
            ans += a * (p if t == 1 else s)
    return ans


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 2)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(12, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
