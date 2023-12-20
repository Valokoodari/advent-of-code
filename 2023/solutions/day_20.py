from math import lcm


def solve(data, p=1):
    ms = {}
    for l in data.splitlines():
        n, ds = l.split(" -> ")
        ms[n[1:]] = [n[0], ds.split(", "), False, {}]
    for m in ms:
        for d in ms[m][1]:
            if d in ms:
                ms[d][3][m] = False

    i, ans, ls = 0, { True: 0, False: 1000 }, {}
    rs = list(ms[[m for m in ms if "rx" in ms[m][1]][0]][3].keys()) if p == 2 else []

    while i < 1000 and p == 1 or len(ls) < len(rs) and p == 2:
        i, ss = i + 1, [("roadcaster", False, "b")]
        while ss:
            m, s, o = ss.pop(0)
            if m not in ms:
                continue
            if m in rs and not s and m not in ls:
                ls[m] = i
            if ms[m][0] == "%":
                if s:
                    continue
                ms[m][2] = not ms[m][2]
            elif ms[m][0] == "&":
                ms[m][3][o] = s
                ms[m][2] = not all(ms[m][3].values())
            else:
                ms[m][2] = s
            for d in ms[m][1]:
                ans[ms[m][2]] += 1
                ss.append((d, ms[m][2], m))

    return (ans[True] * ans[False], lcm(*ls.values()))[p-1]


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, 2)


EX_0 = """\
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

EX_1 = """\
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 32000000
    assert part_1(EX_1) == 11687500


if __name__ == "__main__":
    test()
