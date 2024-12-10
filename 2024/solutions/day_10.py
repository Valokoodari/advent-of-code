def solve(d, p = 1, ans = 0):
    ms = [[int(c) if c.isnumeric() else 11 for c in line] for line in d.splitlines()]
    ss = [(r, c) for r in range(len(ms)) for c in range(len(ms[0])) if ms[r][c] == 0]

    for r, c in ss: 
        q, es, vs = [(r, c)], set(), [[False]*len(ms[0]) for _ in range(len(ms))]
        while q:
            r, c = q.pop()
            vs[r][c] = True
            if ms[r][c] == 9:
                es.add((r, c))
                ans += 1 if p == 2 else 0
                continue
            for dr, dc in ((-1,0), (0,1), (1,0), (0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < len(ms) and 0 <= nc < len(ms[0]) and ms[nr][nc] == ms[r][c]+1 and (not vs[nr][nc] or p == 2):
                    q.append((nr, nc))
        ans += len(es) if p == 1 else 0
    return ans


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 2)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(10, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
