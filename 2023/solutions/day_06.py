from math import ceil, floor, prod


def sr(t, d):
    return ceil((t + (t**2 - 4*d) ** 0.5) / 2) - floor((t - (t**2 - 4*d) ** 0.5) / 2) - 1


def part_1(data):
    ns = [[int(n) for n in l.split()[1:]] for l in data.splitlines()]
    return prod(sr(*n) for n in list(zip(*ns)))


def part_2(data):
    return sr(*[int(l.split(":")[1]) for l in data.replace(" ", "").splitlines()])


EX_0 = """\
Time:      7  15   30
Distance:  9  40  200
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 288
    # assert part_2(EX_0) == 0


if __name__ == "__main__":
    test()
