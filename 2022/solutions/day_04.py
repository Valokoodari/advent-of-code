parse = lambda x: [[*map(int, l.split(","))] for l in x.replace("-",",").splitlines()]

def part_1(data):
    return sum(1 for l in parse(data) if (l[0] <= l[2] and l[1] >= l[3]) or (l[2] <= l[0] and l[3] >= l[1]))

def part_2(data):
    return sum(1 for l in parse(data) if l[0] <= l[3] and l[1] >= l[2])


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
