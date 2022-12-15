parse = lambda d: [list(map(int, l[12:].split(","))) for l in d.replace(" y=", "").replace(": closest beacon is at x=", ",").splitlines()]


def part_1(data, y=2_000_000):
    ss, ans = parse(data), 0
    bs = set((s[2], s[3]) for s in ss)

    for x in range(-y*3, y*3+1):
        for s in ss:
            if abs(x-s[0]) + abs(y-s[1]) <= abs(s[0] - s[2]) + abs(s[1] - s[3]):
                ans += 1
                break

    return ans - sum(1 for b in bs if b[1] == y)


def part_2(data, m=4_000_000):
    ss = parse(data)

    for s in ss:
        d = abs(s[0]-s[2]) + abs(s[1]-s[3]) + 1
        for c in range(-d, d+1):
            if 0 <= (x := s[0]+c) <= m:
                for y in (s[1]+d-abs(c), s[1]-d+abs(c)):
                    if 0 <= y <= m:
                        if all(abs(x-s[0]) + abs(y-s[1]) > abs(s[0]-s[2]) + abs(s[1]-s[3]) for s in ss):
                            return x * 4_000_000 + y


EX_0 = """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0, 10) == 26
    assert part_2(EX_0, 20) == 56000011


if __name__ == "__main__":
    test()
