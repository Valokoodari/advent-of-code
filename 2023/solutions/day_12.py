from functools import cache


@cache
def fs(s, ns, i = 0, hc = 0, c = 0):
    if c == len(ns):
        return 1 if s[i:].count("#") == 0 else 0
    if i == len(s):
        return 1 if len(ns) == (c + 1 if hc == ns[c] else 0) else 0
    if s[i] == "#":
        return fs(s, ns, i + 1, hc + 1, c) if hc < ns[c] else 0

    a = fs(s, ns, i + 1, 0, c + 1) if hc == ns[c] else fs(s, ns, i + 1, 0, c) if hc == 0 else 0
    return a + (0 if s[i] == "." else fs(s, ns, i + 1, hc + 1, c))


def part_1(data):
    ls = [l.split(" ") for l in data.splitlines()]
    ss = [fs(l[0], tuple(int(n) for n in l[1].split(","))) for l in ls]
    return sum(ss)


def part_2(data):
    ls = [l.split(" ") for l in data.splitlines()]
    return sum(fs(l[0] + ("?" + l[0]) * 4, tuple(int(n) for n in l[1].split(",")) * 5) for l in ls)


EX_0 = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 21
    assert part_2(EX_0) == 525152


if __name__ == "__main__":
    test()
