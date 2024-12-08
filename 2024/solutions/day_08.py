def solve(data, p = 1):
    fs, h, w = {}, len(ls := data.splitlines()), len(ls[0])
    for r, l in enumerate(ls):
        for c, x in enumerate(l):
            if x != ".":
                fs.setdefault(x, []).append((r, c))

    ns = set()
    for f in fs.values():
        for i in range(len(f)-1):
            for j in range(i+1, len(f)):
                r1, c1, r2, c2  = *f[i], *f[j]
                dr, dc = r2-r1, c2-c1

                for m in [1] if p == 1 else range(max(w, h) // max(abs(dr), abs(dc))):
                    ar, ac, br, bc = r1-m*dr, c1-m*dc, r2+m*dr, c2+m*dc
                    if 0 <= ar < w and 0 <= ac < h:
                        ns.add((ar, ac))
                    if 0 <= br < w and 0 <= bc < h:
                        ns.add((br, bc))

    return len(ns)


def part_1(data):
    return solve(data)


def part_2(data):
   return solve(data, 2)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(8, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
