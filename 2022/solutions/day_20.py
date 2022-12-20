from collections import deque


def solve(data, k=1, r=1):
    ns = deque(list(range(len(os := [int(n)*k for n in data.splitlines()]))))

    for _ in range(r):
        for i, n in enumerate(os):
            ns.rotate(-ns.index(i))
            ns.remove(i)
            ns.rotate(-n)
            ns.appendleft(i)

    ns.rotate(-ns.index(os.index(0)))

    return sum(os[ns[1000*(i+1)%len(ns)]] for i in range(3))


def part_1(data): return solve(data)

def part_2(data): return solve(data, 811589153, 10)


EX_0 = """\
1
2
-3
3
-2
0
4"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 3
    assert part_2(EX_0) == 1623178306


if __name__ == "__main__":
    test()
