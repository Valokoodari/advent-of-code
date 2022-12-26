from heapq import heappush, heappop
from math import lcm

def solve(data, p=1):
    ls = data.splitlines()
    sp, ep = (0, ls[0].index(".")), (len(ls) - 1, ls[-1].index("."))
    bs = { d: set((r, c) for r, row in enumerate(ls) for c, ch in enumerate(row) if ch == d) for d in "<>^v#" }

    bc = lcm(len(ls)-2, len(ls[0])-2)

    bss = []
    for _ in range(bc):
        bss.append(bs)

        bs = {
            "^": set((r-1 if r > 1 else len(ls)-2, c) for r, c in bs["^"]),
            "v": set((r+1 if r < len(ls)-2 else 1, c) for r, c in bs["v"]),
            "<": set((r, c-1 if c > 1 else len(ls[0])-2) for r, c in bs["<"]),
            ">": set((r, c+1 if c < len(ls[0])-2 else 1) for r, c in bs[">"]),
            "#": bs["#"],
        }

    q, vs, cc = [(0, sp)], set(), 0
    while q:
        d, cp = heappop(q)

        if (d, cp) in vs:
            continue
        vs.add((d, cp))

        if cp == ep:
            if p == 2 and cc < 2:
                cc, sp, ep, vs, q = cc + 1, ep, sp, set(), [(d+1, ep)]
                continue
            return d

        for dp in ((0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)):
            np = (cp[0] + dp[0], cp[1] + dp[1])

            if not (0 <= np[0] < len(ls) and 0 <= np[1] < len(ls[0])):
                continue

            if any(np in bss[(d+1)%bc][s] for s in "<>^v#"):
                continue

            heappush(q, (d + 1, np))


def part_1(data): return solve(data)

def part_2(data): return solve(data, 2)


EX_0 = """\
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 18
    assert part_2(EX_0) == 54


if __name__ == "__main__":
    test()
