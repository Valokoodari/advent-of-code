parse = lambda x, y: (["".join(s).strip() for s in list(zip(*x[-2::-1]))[1::4]], [[*map(int, l.split()[1::2])] for l in y])

def solve(data, r):
    ss, os = parse(*(p.splitlines() for p in data.split("\n\n")))

    for o in os:
        ss[o[1]-1], ss[o[2]-1] = ss[o[1]-1][:-o[0]], ss[o[2]-1] + ss[o[1]-1][-o[0]:][::r]

    return "".join(s[-1] for s in ss)


def part_1(data):
    return solve(data, -1)

def part_2(data):
    return solve(data, 1)


EX_1 = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def test():
    assert part_1(EX_1) == "CMZ"
    assert part_2(EX_1) == "MCD"


if __name__ == "__main__":
    test()
