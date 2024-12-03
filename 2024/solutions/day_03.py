import re

def part_1(data):
    ms, ans = re.findall(r"mul\(\d+,\d+\)", data), 0
    for m in ms:
        m = m.replace("(", ",").replace(")", ",").split(",")
        ans += int(m[1]) * int(m[2])
    return ans


def part_2(data):
    ms, ans, e = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data), 0, 1
    for m in ms:
        if m == "do()":
            e = 1
        elif m == "don't()":
            e = 0
        else:
            m = m.replace("(", ",").replace(")", ",").split(",")
            ans += int(m[1]) * int(m[2]) * e
    return ans


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(3, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
