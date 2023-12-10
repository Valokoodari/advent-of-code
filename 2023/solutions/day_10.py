NS = {
    "|": ((1, 0), (-1, 0)),
    "-": ((0, 1), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
}


def solve(data):
    s, nss, sn = (-1, -1), [[[] for _ in line] for line in data.splitlines()], set()
    for r, line in enumerate(data.splitlines()):
        for c, char in enumerate(line):
            if char == "S":
                s = (r, c)
            if char not in NS:
                continue
            nss[r][c] = [(r+dr, c+dc) for dr, dc in NS[char]]
    for r, ns in enumerate(nss):
        for c, n in enumerate(ns):
            if s in n:
                sn.add((r-s[0], c-s[1]))
                nss[s[0]][s[1]].append((r, c))

    vs, p, l = set([s]), nss[s[0]][s[1]][0], s
    while p != s:
        vs.add(p)
        n = nss[p[0]][p[1]]
        l, p = p, n[1] if n[0] == l else n[0]

    return (vs, s, sn)


def part_1(data):
    return len(solve(data)[0]) // 2


def part_2(data):
    ls, ans = [[c for c in l] for l in data.splitlines()], 0
    vs, s, sn = solve(data)
    for k, v in NS.items():
        if sn == set(v):
            ls[s[0]][s[1]] = k
            break

    for r, cs in enumerate(ls):
        i = False
        for c, ch in enumerate(cs):
            if (r, c) in vs and ch in "|LJ":
                i = not i
            if (r, c) not in vs:
                ans += 1 if i else 0

    return ans


EX_0 = """\
.....
.S-7.
.|.|.
.L-J.
.....
"""

EX_1 = """\
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

EZ_2 = """\
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

EX_3 = """\
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

EX_4 = """\
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

EX_5 = """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

def test():
    assert EX_0 != ""

    assert part_1(EX_0) == 4
    assert part_1(EX_1) == 4
    assert part_1(EZ_2) == 8

    assert part_2(EX_3) == 4
    assert part_2(EX_4) == 8
    assert part_2(EX_5) == 10


if __name__ == "__main__":
    test()
