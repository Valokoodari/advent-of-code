from math import prod


def parse(data):
    return [{
        "is": [int(n) for n in p[1].split(":")[1].split(",")],
        "o": eval(f"lambda old: {p[2].split('=')[-1]}"),
        "t": int(p[3].split()[-1]),
        "tt": int(p[4].split()[-1]),
        "tf": int(p[5].split()[-1]),
        "s": 0
    } for p in [l.splitlines() for l in data.split("\n\n")]]


def solve(data, p):
    ms = parse(data)
    lcm = prod(m["t"] for m in ms)

    for _ in range(20 if p == 1 else 10000):
        for m in ms:
            for i in m["is"]:
                m["s"] += 1
                i = m['o'](i) % lcm // (3 if p == 1 else 1)
                ms[m["tt" if i % m["t"] == 0 else "tf"]]["is"].append(i)
            m["is"] = []

    return prod(sorted(m["s"] for m in ms)[-2:])


def part_1(data):
    return solve(data, 1)

def part_2(data):
    return solve(data, 2)


EX_0 = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

def test():
    assert part_1(EX_0) == 10605
    assert part_2(EX_0) == 2713310158


if __name__ == "__main__":
    test()
