from itertools import product


def solve(d, os = "+*"):
    ans = 0
    for l in d.splitlines():
        t, *ns = [int(n) for n in l.replace(":","").split()]
        for ops in product(os, repeat=len(ns)-1):
            r = ns[0]
            for i, op in enumerate(ops):
                match op:
                    case "+": r += ns[i+1]
                    case "*": r *= ns[i+1]
                    case "|": r = int(str(r) + str(ns[i+1]))
            if r == t:
                ans += t
                break
    return ans


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, "+*|")


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(7, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
