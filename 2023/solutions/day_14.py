DS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
CYCLES = 1000000000


def parse(d):
    rs, ws = set(), set()
    for r, row in enumerate(d.splitlines()):
        for c, char in enumerate(row):
            if char == "#":
                ws.add((r, c))
            elif char == "O":
                rs.add((r, c))
    return rs, ws, len(d.splitlines()), len(d.splitlines()[0])


def tilt(rs, ws, h, w, d): # TODO: optimize
    m, (dr, dc) = True, DS[d]
    while m:
        m = False
        for r, c in rs:
            if (r+dr, c+dc) not in ws and (r+dr, c+dc) not in rs and 0 <= r+dr < h and 0 <= c+dc < w:
                rs.remove((r, c))
                rs.add((r+dr, c+dc))
                m = True
    return rs


def part_1(data):
    return sum(len(data.splitlines()) - r[0] for r in tilt(*parse(data), 0))


def part_2(data):
    rs, ws, h, w = parse(data)

    cr, mr, hs = 0, 0, {}
    for i in range(1, CYCLES+1):
        for d in range(len(DS)):
            rs = tilt(rs, ws, h, w, d)
        if tuple(rs) in hs:
            cr, mr = i, hs[tuple(rs)]
            break
        hs[tuple(rs)] = i

    for _ in range((CYCLES - cr) % (cr - mr)):
        for d in range(len(DS)):
            rs = tilt(rs, ws, h, w, d)

    return sum(h - r[0] for r in rs)


EX_0 = """\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 136
    assert part_2(EX_0) == 64


if __name__ == "__main__":
    test()
