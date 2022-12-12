from heapq import heappush, heappop


def parse(data):
    ms, s, e = {}, None, None

    for r, l in enumerate(data.splitlines()):
        for c, h in enumerate(l):
            ms[(r, c)] = ord("a" if h == "S" else "z" if h == "E" else h) - ord("a")
            if h == "S":
                s = (r, c)
            elif h == "E":
                e = (r, c)

    return ms, s, e


def solve(data, p2=False):
    ms, s, e = parse(data)
    q, ss = [(0, e if p2 else s)], set()

    while q:
        c, p = heappop(q)

        if p in ss:
            continue
        ss.add(p)

        if not p2 and p == e or p2 and ms[p] == 0:
            return c

        for n in [(p[0]+d[0], p[1]+d[1]) for d in ((0, 1), (0, -1), (1, 0), (-1, 0))]:
            if n in ms and ms[p if p2 else n] - ms[n if p2 else p] <= 1:
                heappush(q, (c + 1, n))

    return -1


def part_1(data):
    return solve(data)

def part_2(data):
    return solve(data, True)


EX_0 = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 31
    assert part_2(EX_0) == 29


if __name__ == "__main__":
    test()
