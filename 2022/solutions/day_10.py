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
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

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
