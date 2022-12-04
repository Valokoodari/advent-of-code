parse = lambda x: [[[*map(int, r.split("-"))] for r in l.split(",")] for l in x.splitlines()]

def part_1(data):
    return sum(1 for l in parse(data) if (l[0][0] >= l[1][0] and l[0][1] <= l[1][1]) or (l[1][0] >= l[0][0] and l[1][1] <= l[0][1]))

def part_2(data):
    return sum(1 for l in parse(data) if l[0][0] <= l[1][1] and l[0][1] >= l[1][0])


EX_1 = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def test():
    assert(part_1(EX_1) == 2)
    assert(part_2(EX_1) == 4)


if __name__ == "__main__":
    test()
