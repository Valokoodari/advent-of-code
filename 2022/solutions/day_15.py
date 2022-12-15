parse = lambda d: [list(map(int, l[12:].split(","))) for l in d.replace(": closest beacon is at x=", ",").replace(" y=", "").splitlines()]


def part_1(data, y=2_000_000):
    ss, rs = parse(data), []

    for s in ss:
        if abs(y-s[1]) <= (d := abs(s[0]-s[2]) + abs(s[1]-s[3])):
            nrs = [(l := (s[0] - d + abs(y-s[1]), s[0] + d - abs(y-s[1])))]

            for r in rs:
                nrs.extend([r] if r[1] < l[0] or r[0] > l[1] else [x for x in ((r[0], l[0]), (l[1], r[1])) if x[0] <= x[1]])
            rs = nrs

    return sum(b - a for a, b in rs)


def part_2(data, m=4_000_000):
    ss = parse(data)

    for s in ss:
        d = abs(s[0]-s[2]) + abs(s[1]-s[3]) + 1
        for x in range(max(0, -d+s[0]), min(m, d+1+s[0])):
            for y in (s[1]+d-abs(x-s[0]), s[1]-d+abs(x-s[0])):
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
