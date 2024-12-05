def part_1(data):
    ans, d = 0, data.splitlines()
    for _ in range(4):
        ans += sum(1 for r in range(len(d)) for c in range(len(d[r])-3) if "".join(d[r][c:c+4]) == "XMAS")
        ans += sum(1 for r in range(len(d)-3) for c in range(len(d[r])-3) if "".join((d[r][c],d[r+1][c+1],d[r+2][c+2],d[r+3][c+3])) == "XMAS")
        d = list(zip(*d))[::-1]
    return ans


def part_2(data):
    return sum(1 if d[r][c] == "A" and "".join([d[r-1][c-1],d[r-1][c+1],d[r+1][c-1],d[r+1][c+1]]) in ["MMSS","SSMM","MSMS","SMSM"] else 0 for d in [data.splitlines()] for r in range(1,len(d)-1) for c in range(1,len(d[r])-1))


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(4, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
