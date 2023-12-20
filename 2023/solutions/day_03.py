import re


NS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def part_1(data):
    gs = [[c for c in r]for r in data.splitlines()]
    ss = [["." for _ in r] for r in gs]
    for r in range(len(gs)):
        for c in range(len(gs[r])):
            if gs[r][c] != "." and not gs[r][c].isdigit():
                for dr, dc in NS:
                    if 0 <= r+dr < len(gs) and 0 <= c+dc < len(gs[r+dr]) and gs[r+dr][c+dc].isdigit():
                        ss[r+dr][c+dc], pv, nv = gs[r+dr][c+dc], True, True
                        for id in range(1, 3):
                            if nv and gs[r+dr][c+dc-id].isdigit():
                                ss[r+dr][c+dc-id] = gs[r+dr][c+dc-id]
                            else:
                                nv = False
                            if pv and gs[r+dr][c+dc+id].isdigit():
                                ss[r+dr][c+dc+id] = gs[r+dr][c+dc+id]
                            else:
                                pv = False
    return sum(int(n) for n in re.findall(r"\d+", ".".join(["".join(r) for r in ss])))


def part_2(data):
    gs, ans = [[c for c in r]for r in data.splitlines()], 0
    for r in range(len(gs)):
        for c in range(len(gs[r])):
            if gs[r][c] == "*" and not gs[r][c].isdigit():
                vs, nc, m = set(), 0, 1
                for dr, dc in NS:
                    if gs[r+dr][c+dc].isdigit() and (r+dr, c+dc) not in vs:
                        vs.add((r+dr, c+dc))
                        n, nc, pv, nv = gs[r+dr][c+dc], nc + 1, True, True
                        for id in range(1, 3):
                            if nv and gs[r+dr][c+dc-id].isdigit() and (r+dr, c+dc-id) not in vs:
                                vs.add((r+dr, c+dc-id))
                                n = gs[r+dr][c+dc-id] + n
                            else:
                                nv = False
                            if pv and gs[r+dr][c+dc+id].isdigit() and (r+dr, c+dc+id) not in vs:
                                vs.add((r+dr, c+dc+id))
                                n += gs[r+dr][c+dc+id]
                            else:
                                pv = False
                        m *= int(n)
                if nc == 2:
                    ans += m
    return ans


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(3, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
