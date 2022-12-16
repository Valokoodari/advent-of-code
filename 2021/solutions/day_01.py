def solve(d, n):
    ns = [int(l) for l in d.splitlines()]
    return sum(1 for i in range(len(ns)-n) if ns[i] < ns[i+n])


def part_1(data): return solve(data, 1)

def part_2(data): return solve(data, 3)


EX_0 = """\
199
200
208
210
200
207
240
269
260
263"""


def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 7
    assert part_2(EX_0) == 5


if __name__ == "__main__":
    test()
