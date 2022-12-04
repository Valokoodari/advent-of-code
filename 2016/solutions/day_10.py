def parse(data):
    bs, hs, os = {}, {}, {}

    for line in data.replace("output ", "_ 100").splitlines():
        if line.startswith("value"):
            _, value, _, _, _, bot = line.split()
            hs.setdefault(int(bot), []).append(int(value))
        else:
            _, bot, _, _, _, _, low, _, _, _, _, high = line.split()
            bs[int(bot)] = (int(low), int(high))

    for bot in bs:
        hs.setdefault(bot, [])

    return bs, hs, os


def comp(data, c1, c2):
    bs, hs, os = parse(data)

    while any(len(vs) == 2 for vs in hs.values()):
        for b, vs in hs.items():
            if len(vs) == 2:
                l, h = sorted(vs)

                if l == c1 != -1 and h == c2 != -1:
                    return b

                hs[b], (lt, ht) = [], bs[b]

                os[lt] = l if lt >= 1000 else hs[lt].append(l)
                os[ht] = h if ht >= 1000 else hs[ht].append(h)

    return os[1000] * os[1001] * os[1002]


def part_1(data, c1 = 17, c2 = 61):
    return comp(data, c1, c2)

def part_2(data):
    return comp(data, -1, -1)


EX_1 = """\
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""

def test():
    assert(part_1(EX_1, 2, 5) == 2)


if __name__ == "__main__":
    test()
