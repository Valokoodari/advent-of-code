from math import lcm


def parse(d):
    ds, ins = d.replace("(", "").replace(")", "").split("\n\n")
    return ds, { k: v.split(", ") for k, v in [i.split(" = ") for i in ins.splitlines()] }



def f(ds, ins, p, t = 1):
    i = 0
    while True:
        if p == "ZZZ" or p.endswith("Z") and t == 2:
            return i
        p = ins[p][0 if ds[i % len(ds)] == "L" else 1]
        i += 1


def part_1(data):
    ds, ins = parse(data)
    return f(ds, ins, "AAA")


def part_2(data):
    ds, ins = parse(data)
    return lcm(*[f(ds, ins, p, 2) for p in ins if p.endswith("A")])


EX_0 = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

EX_1 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

EX_2 = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 2
    assert part_1(EX_1) == 6
    assert part_2(EX_2) == 6


if __name__ == "__main__":
    test()
