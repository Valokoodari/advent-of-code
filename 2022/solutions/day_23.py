from collections import deque

NS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
DS = (
    ((0, -1), ((-1, -1), (0, -1), (1, -1))),
    ((0, 1), ((-1, 1), (0, 1), (1, 1))),
    ((-1, 0), ((-1, -1), (-1, 0), (-1, 1))),
    ((1, 0), ((1, -1), (1, 0), (1, 1)))
)


def sim(data, p=1):
    es = set((x, y) for y, l in enumerate(data.splitlines()) for x, c in enumerate(l) if c == "#")

    r, m, ds = 0, True, deque(DS)
    while r < 10 or (m and p == 2):
        cs, nps, m, r = {}, {}, False, r + 1
        for x, y in es:
            if all((x + dx, y + dy) not in es for dx, dy in NS):
                nps[(x, y)] = (x, y)
                continue

            for d, ns in ds:
                if all((x + dx, y + dy) not in es for dx, dy in ns):
                    nps[(x, y)] = (np := (x + d[0], y + d[1]))
                    cs[np] = cs.get(np, 0) + 1
                    break
            else:
                nps[(x, y)] = (x, y)

        es = set()
        for cp, np in nps.items():
            if cp == np or cs.get(np, 0) > 1:
                es.add(cp)
            else:
                m = True
                es.add(np)

        ds.rotate(-1)

    if p == 2:
        return r

    xs, ys = [x for x, _ in es], [y for _, y in es]

    return (max(xs)-min(xs)+1) * (max(ys)-min(ys)+1) - len(es)


def part_1(data): return sim(data)

def part_2(data): return sim(data, 2)


EX_0 = """\
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 110
    assert part_2(EX_0) == 20


if __name__ == "__main__":
    test()
