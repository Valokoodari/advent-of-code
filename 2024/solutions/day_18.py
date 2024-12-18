from heapq import heappop, heappush


def fp(ms, ml):
    mx, my = max(m[0] for m in ms), max(m[1] for m in ms)
    gs = [[0]*(mx+1) for _ in range(my+1)]
    for x, y in ms[:ml]:
        gs[y][x] = 1

    q, vs = [(0, 0, 0)], set()
    while q:
        (l, x, y) = heappop(q)
        if x == mx and y == my:
            return l
        if (x, y) in vs:
            continue
        vs.add((x, y))
        for dx, dy in ((-1,0),(0,1),(1,0),(0,-1)):
            if (nx := x+dx) < 0 or nx > mx or (ny := y+dy) < 0 or ny > my or gs[ny][nx] == 1:
                continue
            heappush(q, (l+1, nx, ny))
    return -1


def part_1(data):
    ms = [tuple(map(int, x.split(","))) for x in data.splitlines()]
    return fp(ms, 12 if len(ms) < 1024 else 1024)


def part_2(data):
    ms = [tuple(map(int, x.split(","))) for x in data.splitlines()]

    l, h = 12 if len(ms) < 1024 else 1024, len(ms)-1
    while l < h:
        h, l = (m, l) if fp(ms, m := (l+h)//2) == -1 else (h, m+1)

    return str(ms[l-1][0]) + "," + str(ms[l-1][1])


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(18, part_1, part_2, False)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
