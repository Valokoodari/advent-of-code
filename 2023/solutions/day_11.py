def solve(d, e = 2):
    mss = [[c for c in l] for l in d.splitlines()]
    ers = [i for i, l in enumerate(mss) if set(l) == {"."}]
    ecs = [i for i, l in enumerate(zip(*mss)) if set(l) == {"."}]

    ans, ss, e = 0, set(), e - 1
    for r, l in enumerate(mss):
        for c, ch in enumerate(l):
            if ch == ".":
                continue
            dr = e * sum(1 for n in ers if n < r) + r
            dc = e * sum(1 for n in ecs if n < c) + c
            for sr, sc in ss:
                ans += abs(sr-dr) + abs(sc-dc)
            ss.add((dr, dc))

    return ans


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 1000000)


EX_0 = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 374
    assert solve(EX_0, 10) == 1030
    assert solve(EX_0, 100) == 8410


if __name__ == "__main__":
    test()
