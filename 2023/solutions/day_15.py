def hash(s):
    v = 0
    for c in s:
        v = (v + ord(c)) * 17 % 256
    return v


def part_1(data):
    return sum(hash(p) for p in data.rstrip().split(","))


def part_2(data):
    bs, ps = [[] for _ in range(256)], data.rstrip().split(",")

    for p in ps:
        if "-" in p:
            for l in bs[hash(p[:-1])]:
                if l[0] == p[:-1]:
                    bs[hash(p[:-1])].remove(l)
                    break
        elif "=" in p:
            i, f = p.split("=")
            for j, (l, _) in enumerate(bs[hash(i)]):
                if l == i:
                    bs[hash(i)][j] = (i, f)
                    break
            else:
                bs[hash(i)].append((i, f))

    return sum((h+1)*(i+1)*int(l[1]) for h, ls in enumerate(bs) for i, l in enumerate(ls))


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(15, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
