def comp(data):
    x, cs = 1, []

    for c in data.splitlines():
        match c.split():
            case ["noop"]:
                cs.append(x)
            case ["addx", n]:
                cs += [x]*2
                x += int(n)

    return cs


def part_1(data):
    cs = comp(data)
    return sum(i * cs[i-1] for i in range(20, 221, 40))


def part_2(data):
    cs, ans = comp(data), ""

    for r in range(6):
        ans += "\n    "
        for c in range(40):
            ans += "█" if cs[r * 40 + c] in [c - 1, c, c + 1] else " "

    return ans


EX_0 = """\
noop
addx 3
addx -5"""

EX_1 = """\
addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4
noop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1
addx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21
addx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5
noop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop
addx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1
noop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2
noop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9
addx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop
addx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3
addx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9
noop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15
addx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop
noop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop"""

def test():
    assert part_1(EX_1) == 13140

    assert part_2(EX_1) == """
    ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  
    ███   ███   ███   ███   ███   ███   ███ 
    ████    ████    ████    ████    ████    
    █████     █████     █████     █████     
    ██████      ██████      ██████      ████
    ███████       ███████       ███████     """


if __name__ == "__main__":
    test()
