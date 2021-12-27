def fvt(ss):
    ss = sorted(ss)[::-1]
    return ss[0] < sum(ss[1:])

def part_1(data):
    ts = tuple(tuple(int(n) for n in l.split(" ") if n != "") for l in data.splitlines())
    return sum(1 for t in ts if fvt(t))


def part_2(data):
    ls = tuple(tuple(int(n) for n in l.split(" ") if n != "") for l in data.splitlines())
    ts = tuple((ls[i*3][j], ls[i*3+1][j], ls[i*3+2][j]) for i in range(len(ls)//3) for j in range(3))
    return sum(1 for t in ts if fvt(t))


TEST_DATA = """\
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603"""

def test():
    assert(fvt([5, 10, 25]) == False)
    assert(part_1(TEST_DATA) == 3)
    assert(part_2(TEST_DATA) == 6)