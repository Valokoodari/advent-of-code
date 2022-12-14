def parse(data):
    rs = set()
    for line in data.splitlines():
        xp, yp = 0, 0
        for i, c in enumerate(line.split(" -> ")):
            x, y = map(int, c.split(","))
            if i != 0:
                if x == xp:
                    for sy in range(min(y, yp), max(y, yp) + 1):
                        rs.add((x, sy))
                else:
                    for sx in range(min(x, xp), max(x, xp) + 1):
                        rs.add((sx, y))
            xp, yp = x, y

    return rs


def solve(data, p2=False):
    rs, ss = parse(data), set()
    my = max(y for _, y in rs)

    while True:
        (sx, sy), m = (500, 0), True

        while m:
            m = False
            for dx, dy in ((0, 1), (-1, 1), (1, 1)):
                if (s := (sx + dx, sy + dy)) not in rs and s not in ss and not (p2 and s[1] == my + 2):
                    (sx, sy), m = s, True
                    break

            if (sx, sy) == (500, 0) or sy >= my and not p2:
                return len(ss)

        ss.add((sx, sy))


def part_1(data):
    return solve(data)

def part_2(data):
    return solve(data, True) + 1


EX_0 = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 24
    assert part_2(EX_0) == 93


if __name__ == "__main__":
    test()
