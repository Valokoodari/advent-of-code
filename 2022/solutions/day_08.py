from itertools import product

def part_1(data):
    ts, vs = [[int(n) for n in l] for l in data.splitlines()], set()

    for x in range(len(ts)):
        hs = [-1]*4
        for y in range(len(ts)):
            for i, (r, c) in enumerate([(x, y), (x, len(ts)-1-y), (y, x), (len(ts)-1-y, x)]):
                if ts[r][c] > hs[i]:
                    vs.add((r, c))
                    hs[i] = ts[r][c]

    return len(vs)


def part_2(data):
    ts = [[int(n) for n in l] for l in data.splitlines()]
    ans, rs = 0, list(zip(*ts))

    for r, c in product(range(1, len(ts)-1), repeat=2):
        s = 1
        for ss in (ts[r][c+1:], ts[r][c-1::-1], rs[c][r+1:], rs[c][r-1::-1]):
            v = 0
            for t in ss:
                v += 1
                if t >= ts[r][c]:
                    break
            s *= v
        ans = max(ans, s)

    return ans


EX_0 = """\
30373
25512
65332
33549
35390"""


def test():
    assert part_1(EX_0) == 21
    assert part_2(EX_0) == 8


if __name__ == "__main__":
    test()
