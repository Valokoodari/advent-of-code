TEST_DATA = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def parse(data):
    return [[int(n) for n in e.split("\n")] for e in data.split("\n\n")]


def part_1(data):
    return max([sum(l) for l in parse(data)])


def part_2(data):
    return sum(sorted([sum(l) for l in parse(data)])[-3:])


def test():
    assert part_1(TEST_DATA) == 24000
    assert part_2(TEST_DATA) == 45000
