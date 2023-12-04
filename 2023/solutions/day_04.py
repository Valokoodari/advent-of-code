def part_1(data):
    cs = [[[int(n) for n in ns.split()] for ns in c[1].split("|")] for c in [l.split(":") for l in data.splitlines()]]
    return sum(int(2 ** (len(set(c[0]) & set(c[1])) - 1)) for c in cs)


def part_2(data):
    cs = {int(c[0].split()[1]): [[int(n) for n in ns.split()] for ns in c[1].split("|")] for c in [l.split(":") for l in data.splitlines()]}
    ss = {c: 0 for c in cs}
    for k, c in cs.items():
        ss[k] += 1
        for i in range(len(set(c[0]) & set(c[1]))):
            ss[k+i+1] += ss[k]
    return sum(ss.values())


EX_0 = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 13
    assert part_2(EX_0) == 30


if __name__ == "__main__":
    test()
