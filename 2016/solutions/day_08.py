WIDTH, HEIGHT = 50, 6


def fcs(data):
    ps = { (x,y): 0 for x in range(WIDTH) for y in range(HEIGHT) }
    for l in data.splitlines():
        if l[:4] == "rect":
            x, y = map(int, l[5:].split("x"))
            for i in range(x):
                for j in range(y):
                    ps[(i,j)] = 1
        elif l[7:13] == "column":
            x, a = map(int, l[16:].split(" by "))
            ps = { **ps, **{ (k[0], (k[1]+a)%HEIGHT): v for k,v in ps.items() if k[0] == x } }
        elif l[7:10] == "row":
            y, a = map(int, l[13:].split(" by "))
            ps = { **ps, **{ ((k[0]+a)%WIDTH, k[1]): v for k,v in ps.items() if k[1] == y } }
    return ps


def part_1(data):
    return sum(fcs(data).values())


def part_2(data):
    ps = fcs(data)
    return "\n    " + "\n    ".join("".join("#" if ps[(x,y)] else " " for x in range(WIDTH)) for y in range(HEIGHT))


TEST_DATA = """\
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""

def test():
    assert(part_1("rect 3x2") == 6)
    assert(part_1(TEST_DATA) == 6)