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


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(8, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
