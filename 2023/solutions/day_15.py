def hash(s):
    v = 0
    for c in s:
        v = (v + ord(c)) * 17 % 256
    return v


def part_1(data):
    return sum(hash(p) for p in data.rstrip().split(","))


def part_2(data):
    bs, ps = [[] for _ in range(256)], data.rstrip().split(",")

    for p in ps:
        if "-" in p:
            for l in bs[hash(p[:-1])]:
                if l[0] == p[:-1]:
                    bs[hash(p[:-1])].remove(l)
                    break
        elif "=" in p:
            i, f = p.split("=")
            for j, (l, _) in enumerate(bs[hash(i)]):
                if l == i:
                    bs[hash(i)][j] = (i, f)
                    break
            else:
                bs[hash(i)].append((i, f))

    return sum((h+1)*(i+1)*int(l[1]) for h, ls in enumerate(bs) for i, l in enumerate(ls))


EX_0 = """\
HASH
"""

EX_1= """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 52
    assert part_1(EX_1) == 1320
    assert part_2(EX_1) == 145


if __name__ == "__main__":
    test()
