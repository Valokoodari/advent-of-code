from collections import deque

def parse(data):
    ms, s, e = {}, (-1, -1), (-1, -1)

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
    q, ss = deque([(0, e if p2 else s)]), set()

    while cp := q.popleft():
        if cp[1] in ss:
            continue
        ss.add(cp[1])

        if not p2 and cp[1] == e or p2 and ms[cp[1]] == 0:
            return cp[0]

        for n in [(cp[1][0]+d[0], cp[1][1]+d[1]) for d in ((0, 1), (0, -1), (1, 0), (-1, 0))]:
            if n in ms and ms[cp[1] if p2 else n] - ms[n if p2 else cp[1]] <= 1:
                q.append((cp[0] + 1, n))


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
