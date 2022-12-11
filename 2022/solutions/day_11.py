from functools import reduce


def parse(data):
    ps, ms = data.split("\n\n"), []
    for p in ps:
        p = p.split("\n")
        ms.append({
            "is": [int(n) for n in p[1][18:].split(", ")],
            "o": eval(f"lambda old: {p[2][19:]}"),
            "t": int(p[3][21:]),
            "tt": int(p[4][29:]),
            "tf": int(p[5][30:]),
            "s": 0
        })

    return ms


def solve(data, p):
    ms = parse(data)
    gcd = reduce(lambda a, b: a * b, [m["t"] for m in ms])

    for _ in range(20 if p == 1 else 10000):
        for m in ms:
            for i in m["is"]:
                m["s"] += 1
                i = m['o'](i) % gcd // (3 if p == 1 else 1)
                ms[m["tt" if i % m["t"] == 0 else "tf"]]["is"].append(i)
            m["is"] = []

    ms.sort(key=lambda m: m["s"], reverse=True)

    return ms[0]["s"] * ms[1]["s"]


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
