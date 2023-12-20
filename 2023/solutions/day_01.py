def part_1(data):
    return sum(int(l[0] + l[-1]) for l in [[c for c in l if c.isdigit()] for l in data.splitlines()])


def part_2(data):
    for d, s in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        data = data.replace(s, s[0] + str(d+1) + s[-1])
    return part_1(data)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(1, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
