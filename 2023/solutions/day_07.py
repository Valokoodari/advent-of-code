parse = lambda d: [({ c: cs.count(c) for c in cs }, b, cs, 0) for cs, b in [l.split() for l in d.splitlines()]]

CS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def sh(x, cs):
    f = 0
    if x[3] == 5 or max(x[0].values()) + x[3] == 5:
        f = 6
    elif max(x[0].values()) + x[3] == 4:
        f = 5
    elif max(x[0].values()) + x[3] == 3:
        f = 3
        if min(x[0].values()) == 2:
            f = 4
    elif max(x[0].values()) + x[3] == 2:
        f = 1
        if list(x[0].values()).count(2) == 2:
            f = 2
    return (f, tuple(cs.index(c) for c in x[2]))


def part_1(data):
    return sum(int(c[1]) * (i + 1) for i, c in enumerate(sorted(parse(data), key=lambda h: sh(h, CS))))


def part_2(data):
    hs = [({ k: v for k, v in c[0].items() if k != "J" }, c[1], c[2], c[0].get("J", 0)) for c in parse(data)]
    return sum(int(c[1]) * (i + 1) for i, c in enumerate(sorted(hs, key=lambda h: sh(h, ["J", *CS]))))


EX_0 = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 6440
    assert part_2(EX_0) == 5905


if __name__ == "__main__":
    test()
