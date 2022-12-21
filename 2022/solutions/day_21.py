from sympy import symbols, solve


def part_1(data):
    ms = { l[0]: l[1].split() for l in [l.split(": ") for l in data.replace("/", "//").splitlines()] }

    f = lambda x: int(x[0]) if len(x) == 1 else eval(f"{f(ms[x[0]])} {x[1]} {f(ms[x[2]])}")

    return f(ms["root"])


def part_2(data):
    ms = { l[0]: l[1].split() for l in [l.split(": ") for l in data.splitlines()] }
    ms["root"], ms["humn"] = [ms["root"][0], "-", ms["root"][2]], ["x"]

    def f(x):
        if len(x) == 1:
            return int(x[0]) if x[0].isdigit() else x[0]
        else:
            a, b = f(ms[x[0]]), f(ms[x[2]])
            if isinstance(a, int) and isinstance(b, int):
                return eval(f"{a} {x[1].replace('/', '//')} {b}")
            return f"({a} {x[1]} {b})"

    x = symbols("x")
    return solve(eval(f(ms["root"])))[0]


EX_0 = """\
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 152
    assert part_2(EX_0) == 301


if __name__ == "__main__":
    test()
