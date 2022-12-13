from functools import cmp_to_key as ctk
from json import loads as parse
from math import prod


def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            if (r := cmp(a[i], b[i])) != 0:
                return r
        return len(a) - len(b)
    if isinstance(a, int) and isinstance(b, list):
        return cmp([a], b)
    return cmp(a, [b])


def part_1(data):
    ps = [[parse(x) for x in p.splitlines()] for p in data.split("\n\n")]

    return sum(i + 1 for i, p in enumerate(ps) if cmp(*p) < 0)


def part_2(data):
    ps = sorted([parse(l) for l in data.splitlines() if l] + [[[2]]] + [[[6]]], key=ctk(cmp))

    return prod(i + 1 for i, p in enumerate(ps) if p == [[2]] or p == [[6]])


EX_0 = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],[4]]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 13
    assert part_2(EX_0) == 140


if __name__ == "__main__":
    test()
