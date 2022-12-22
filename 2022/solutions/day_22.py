DS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def part_1(data):
    ts = { (r, c): 0 if s == "." else 1 for r, l in enumerate(data.splitlines()[:-2]) for c, s in enumerate(l) if s in "#." }
    ns = [int(n) if n.isdigit() else n for n in data.splitlines()[-1].replace("R", " R ").replace("L", " L ").split()]

    (r, c), d = list(ts.keys())[0], 0
    for n in ns:
        if isinstance(n, str):
            d = (d + (1 if n == "R" else -1)) % 4
        else:
            for _ in range(n):
                nr, nc = r + DS[d][0], c + DS[d][1]
                if (nr, nc) not in ts:
                    nr = min(tr for tr, tc in ts if tc == c) if d == 1 else max(tr for tr, tc in ts if tc == c) if d == 3 else r
                    nc = min(tc for tr, tc in ts if tr == r) if d == 0 else max(tc for tr, tc in ts if tr == r) if d == 2 else c
                if ts[(nr, nc)] == 0:
                    r, c = nr, nc
                else:
                    break

    return 1000 * (r+1) + 4 * (c+1) + d


def part_2(data):
    ts = { (r, c): 0 if s == "." else 1 for r, l in enumerate(data.splitlines()[:-2]) for c, s in enumerate(l) if s in "#." }
    ns = [int(n) if n.isdigit() else n for n  in data.splitlines()[-1].replace("R", " R ").replace("L", " L ").split()]

    (r, c), d = list(ts.keys())[0], 0
    for n in ns:
        if isinstance(n, str):
            d = (d + (1 if n == "R" else -1)) % 4
        else:
            for _ in range(n):
                nr, nc, nd = r + DS[d][0], c + DS[d][1], d
                if ts.get((nr, nc), -1) == 1:
                    break
                if (nr, nc) not in ts:
                    nd, nr, nc = d, r, c
                    if 0 <= r < 50 and 50 <= c < 100:
                        if d == 2:
                            nd, nr, nc = 0, 149 - r, 0
                        if d == 3:
                            nd, nr, nc = 0, c + 100, 0
                    elif 0 <= r < 50 and 100 <= c < 150:
                        if d == 0:
                            nd, nr, nc = 2, 149 - r, 99
                        if d == 1:
                            nd, nr, nc = 2, c - 50, 99
                        if d == 3:
                            nr, nc = 199, c - 100
                    elif 50 <= r < 100 and 50 <= c < 100:
                        if d == 0:
                            nd, nr, nc = 3, 49, r + 50
                        if d == 2:
                            nd, nr, nc = 1, 100, r - 50
                    elif 100 <= r < 150 and 0 <= c < 50:
                        if d == 2:
                            nd, nr, nc = 0, 149 - r, 50
                        if d == 3:
                            nd, nr, nc = 0, c + 50, 50
                    elif 100 <= r < 150 and 50 <= c < 100:
                        if d == 0:
                            nd, nr, nc = 2, 149 - r, 149
                        if d == 1: 
                            nd, nr, nc = 2, c + 100, 49
                    elif 150 <= r < 200 and 0 <= c < 50:
                        if d == 0:
                            nd, nr, nc = 3, 149, r - 100
                        if d == 1:
                            nr, nc = 0, c + 100
                        if d == 2:
                            nd, nr, nc = 1, 0, r - 100
                if ts.get((nr, nc), -1) == 0:
                    r, c, d = nr, nc, nd

    return 1000 * (r+1) + 4 * (c+1) + d


EX_0 = """\
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 6032
    assert part_2(EX_0) == 5031


if __name__ == "__main__":
    test()
