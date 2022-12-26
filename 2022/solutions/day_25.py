def part_1(data):
    s = 0
    for l in " ".join(data).replace("-", "-1").replace("=", "-2").splitlines():
        n = sum(int(c) * 5 ** i for i, c in enumerate(l.strip().split(" ")[::-1]))
        s += n

    cs = []
    while s > 0:
        match s % 5:
            case b if 0 <= b <= 2:
                cs.append(str(b))
            case b if 3 <= b <= 4:
                cs.append("=" if b == 3 else "-")
                s += 5 - b
        s //= 5

    return "".join(cs[::-1])


EX_0 = """\
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == "2=-1=0"


if __name__ == "__main__":
    test()
