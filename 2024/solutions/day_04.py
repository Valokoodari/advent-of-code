import numpy as np


def part_1(data):
    s = max(len(data.splitlines()[0]), len(data.splitlines()))
    rd = "\n".join(["".join(l) for l in zip(*data.splitlines())])
    ds = "\n".join(["".join(np.diag([[c for c in l] for l in data.splitlines()], i)) for i in range(-s+1, s)])
    rds = "\n".join(["".join(np.diag([[c for c in l[::-1]] for l in data.splitlines()], i)) for i in range(-s+1, s)])

    return sum(data.count(w)+rd.count(w)+ds.count(w)+rds.count(w) for w in ("XMAS","SAMX"))


def part_2(data):
    return sum(1 if d[r][c] == "A" and (d[r-1][c-1],d[r-1][c+1],d[r+1][c-1],d[r+1][c+1]) in [("M","M","S","S"),("S","S","M","M"),("M","S","M","S"),("S","M","S","M")] else 0 for d in [data.splitlines()] for r in range(1,len(d)-1) for c in range(1,len(d[r])-1))


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(4, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
