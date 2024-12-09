def part_1(data):
    fs, i, f = [], 0, False
    for c in data:
        n, f = int(c), not f
        if f:
            fs.extend(i for _ in range(n))
            i += 1
        else:
            fs.extend(-1 for _ in range(n))

    i, j = 0, len(fs) - 1
    while i < j:
        if fs[i] == -1:
            while fs[j] == -1:
                j -= 1
            if j <= i:
                break
            fs[i], fs[j] = fs[j], fs[i]
            j -= 1
        i += 1

    return sum(i * f for i, f in enumerate(fs) if f != -1)


def part_2(data):
    fs, i, f = [], 0, False
    for c in data:
        n, f = int(c), not f
        if f:
            fs.append((i, n))
            i += 1
        else:
            fs.append((-1, n))

    i = -1
    while i < len(fs) - 1:
        f, l, i = *fs[-i-2], i+1
        if f == -1:
            continue
        for j in range(len(fs)-i-1):
            g, s = fs[j]
            if g == -1 and s >= l:
                fs[j] = (g, s - l)
                fs.insert(j, fs.pop(-i-1))
                fs.insert(-i-1, (-1, l))
                break

    return sum(i * f for i, f in enumerate(f for f, l in fs for _ in range(l)) if f != -1)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(9, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
