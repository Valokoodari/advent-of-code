DS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
RS = {
    ".": [[0], [1], [2], [3]],
    "-": [[1, 3], [1], [1, 3], [3]],
    "|": [[0], [0, 2], [2], [0, 2]],
    "/": [[1], [0], [3], [2]],
    "\\": [[3], [2], [1], [0]],
}


def fm(ms, r, c, d):
    q, vs = [(r, c, d)], set()
    while q:
        r, c, d = q.pop()
        if (r, c, d) in vs:
            continue
        vs.add((r, c, d))
        for nd in RS[ms[r][c]][d]:
            nr, nc = r + DS[nd][0], c + DS[nd][1]
            if 0 <= nr < len(ms) and 0 <= nc < len(ms[0]):
                q.append((nr, nc, nd))
    return len({(r, c) for r, c, _ in vs})


def part_1(data):
    return fm(data.splitlines(), 0, 0, 1)


def part_2(data):
    ms, cs = data.splitlines(), []

    for r in range(len(ms)):
        cs.append((r, 0, 1))
        cs.append((r, len(ms[0])-1, 3))
    for c in range(len(ms[0])):
        cs.append((0, c, 2))
        cs.append((len(ms)-1, c, 0))

    return max(fm(ms, *c) for c in cs)


EX_0 = """\
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 46
    assert part_2(EX_0) == 51


if __name__ == "__main__":
    test()
