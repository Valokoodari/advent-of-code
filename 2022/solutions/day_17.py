R = ("####", ".#.\n###\n.#.", "..#\n..#\n###", "#\n#\n#\n#", "##\n##")
RS = [[(x+2, -y) for y, l in enumerate(r.splitlines()) for x, c in enumerate(l) if c == "#"] for r in R]


def sim(data, rc=2022):
    i, m, ss, ms, f, ds = 0, 0, set(), {}, False, [1 if c == ">" else -1 for c in data]

    while i < rc:
        cr, my = RS[i%len(RS)], max(max([y for _, y in ss], [0]))
        p = (0, my + 4 - min(sy for _, sy in cr))

        while True:
            if all((x + ds[m] + p[0], y + p[1]) not in ss and 0 <= (p[0] + x + ds[m]) < 7 for x, y in cr):
                p = (p[0] + ds[m%len(ds)], p[1])
            m = (m+1) % len(ds)
            if all((x + p[0], y + p[1] - 1) not in ss and y + p[1] > 1 for x, y in cr):
                p = (p[0], p[1] - 1)
            else:
                ss.update([(x + p[0], y + p[1]) for x, y in cr])
                if not f and rc > 2022:
                    my = max(y for _, y in ss)
                    ts = tuple(my-y for y in [max(max([y for x, y in ss if x == c],[0])) for c in range(7)])
                    d = (ts, i%len(RS), m)

                    if d in ms:
                        f, r = True, (rc - i) // (i - ms[d][0]) - 1
                        ss = set((x, (my - ms[d][1]) * r - ts[x] + my) for x in range(7))
                        i += r * (i - ms[d][0])
                    ms[d] = (i, my)
                break
        i += 1

    return max(y for _, y in ss)


def part_1(data): return sim(data)

def part_2(data): return sim(data, 1000000000000)


EX_0 = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 3068
    assert part_2(EX_0) == 1514285714288


if __name__ == "__main__":
    test()
