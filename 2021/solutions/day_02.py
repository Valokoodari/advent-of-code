def part_1(data):
    h,d = 0,0
    for l in data.splitlines():
        match l.split(" "):
            case ["forward", x]:
                h += int(x)
            case ["down", x]:
                d += int(x)
            case ["up", x]:
                d -= int(x)
    return h * d


def part_2(data):
    h,a,d = 0,0,0
    for l in data.splitlines():
        match l.split(" "):
            case ["forward", x]:
                h += int(x)
                d += a * int(x)
            case ["down", x]:
                a += int(x)
            case ["up", x]:
                a -= int(x)
    return h * d


EX_0 = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 150
    assert part_2(EX_0) == 900


if __name__ == "__main__":
    test()
