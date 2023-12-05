def parse(d):
    ps = d.split("\n\n")
    ss = [int(x) for x in ps[0].split(": ")[1].split()]
    ms = [[[int(x) for x in l.split()] for l in p.splitlines()[1:]] for p in ps[1:]]
    return ss, ms


def part_1(data):
    ss, ms = parse(data)

    ns = []
    for s in ss:
        for m in ms:
            for v in m:
                if v[1] <= s < v[1] + v[2]:
                    s += v[0] - v[1]
                    break
        ns.append(s)

    return min(ns)


def part_2(data):
    ss, ms = parse(data)
    rs = [(ss[i], ss[i+1] + ss[i] - 1) for i in range(0, len(ss), 2)]

    for p in ms:
        nrs = []
        for v in p:
            crs = []
            for r in rs:
                if not (r[0] > v[1] + v[2] - 1 or r[1] < v[1]):
                    a, b = max(v[1], r[0]), min(v[1] + v[2] - 1, r[1])
                    nrs.append((a + v[0] - v[1], b + v[0] - v[1]))
                    if r[0] < a:
                        crs.append((r[0], a - 1))
                    if r[1] > b:
                        crs.append((b + 1, r[1]))
                else:
                    crs.append(r)
            rs = crs
        rs = crs + nrs

    return min(r[0] for r in rs)


EX_0 = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 35
    assert part_2(EX_0) == 46


if __name__ == "__main__":
    test()
