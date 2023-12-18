from heapq import heappush, heappop


def solve(d, mn = 1, mx = 3):
    ms = [[int(n) for n in l] for l in d.splitlines()]

    q, vs, cs = [(0, 0, 0, -1)], set(), {}
    while q:
        p, r, c, d = heappop(q)
        if r == len(ms) - 1 and c == len(ms[0]) - 1:
            return p
        if (r, c, d) in vs:
            continue
        vs.add((r, c, d))

        for nd in range(4):
            if nd == d or (nd + 2) % 4 == d:
                continue
            (dr, dc), h = ((-1, 0), (0, 1), (1, 0), (0, -1))[nd], 0
            for i in range(1, mx+1):
                nr, nc = r + dr * i, c + dc * i
                if 0 <= nr < len(ms) and 0 <= nc < len(ms[0]):
                    h += ms[nr][nc]
                    if i >= mn:
                        if (nr, nc, nd) in cs and cs[(nr, nc, nd)] <= p + h:
                            continue
                        cs[(nr, nc, nd)] = p + h
                        heappush(q, (p + h, nr, nc, nd))


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 4, 10)


EX_0 = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

EX_1 = """\
111111111111
999999999991
999999999991
999999999991
999999999991
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 102
    assert part_2(EX_0) == 94
    assert part_2(EX_1) == 71


if __name__ == "__main__":
    test()
