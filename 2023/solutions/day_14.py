def tilt(ms):
    ms = [list(r) for r in ms]
    for r in range(len(ms)):
        for c in range(len(ms[0])):
            if ms[r][c] == "O":
                dr = 1
                while r-dr >= 0 and ms[r-dr][c] == ".":
                    dr += 1
                ms[r][c], ms[r-dr+1][c] = ".", "O"
    return ms


def cycle(ms):
    return list(list(r[::-1]) for r in zip(*tilt(list(zip(*tilt(list(zip(*tilt(list(zip(*tilt(ms))))))[::-1])))[::-1])))[::-1]


def part_1(data):
    ms = tilt(data.splitlines())
    return sum(len(ms)-r for r in range(len(ms)) for c in range(len(ms[0])) if ms[r][c] == "O")


def part_2(data):
    hs, ms, cs = {}, data.splitlines(), 1000000000

    for i in range(cs):
        ms = cycle(ms)
        m = tuple(tuple(r) for r in ms)
        if m in hs:
            cr, mr = i+1, hs[m]+1
            break
        hs[m] = i

    for _ in range((cs-cr) % (cr-mr)):
        ms = cycle(ms)

    return sum(len(ms)-r for r in range(len(ms)) for c in range(len(ms[0])) if ms[r][c] == "O")


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(14, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
