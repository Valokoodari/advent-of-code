from heapq import heappush, heappop

DS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def part_1(data):
    bs = set(tuple(map(int, l.split(","))) for l in data.splitlines())

    return sum(sum((a+d[0], b+d[1], c+d[2]) not in bs for d in DS) for a, b, c in bs)


def part_2(data):
    bs = set(tuple(map(int, l.split(","))) for l in data.splitlines())

    ls = (min(a for a, _, _ in bs)-1, min(b for _, b, _ in bs)-1, min(c for _, _, c in bs)-1)
    hs = (max(a for a, _, _ in bs)+1, max(b for _, b, _ in bs)+1, max(c for _, _, c in bs)+1)

    ans, q, vs = 0, [ls], set()
    while q:
        a, b, c = heappop(q)

        if (a, b, c) in vs:
            continue
        vs.add((a, b, c))

        for d in DS:
            if (x := a+d[0], y := b+d[1], z := c+d[2]) in bs:
                ans += 1
                continue
            if (ls[0] <= x <= hs[0] and ls[1] <= y <= hs[1] and ls[2] <= z <= hs[2]):
                heappush(q, (x, y, z))

    return ans


EX_0 = """\
1,1,1
2,1,1"""

EX_1 = """\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

def test():
    assert EX_0 != ""

    assert part_1(EX_0) == 10
    assert part_1(EX_1) == 64

    assert part_2(EX_0) == 10
    assert part_2(EX_1) == 58


if __name__ == "__main__":
    test()
