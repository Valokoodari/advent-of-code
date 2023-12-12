def solve(d, s = 1):
    ans = 0
    for rs in [[[int(n) for n in l.split()][::s]] for l in d.splitlines()]:
        while set(rs[-1]) != set([0]):
            rs.append([rs[-1][i+1] - rs[-1][i] for i in range(len(rs[-1])-1)])
        for i in range(len(rs), 1, -1):
            rs[i-2].append(rs[i-2][-1] + rs[i-1][-1])
        ans += rs[0][-1]
    return ans


def part_1(data):
    return solve(data)


def part_2(data):
    return solve(data, -1)


EX_0 = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 114
    assert part_2(EX_0) == 2


if __name__ == "__main__":
    test()
