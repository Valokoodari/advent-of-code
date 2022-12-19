from collections import deque
from math import prod
import re

ns = lambda d: [list(map(int, re.findall(r"-?\d+", l))) for l in d.splitlines()]


def solve(cs, m):
    mo = max(cs[0], cs[1], cs[2], cs[4])

    b, ss, q = 0, set(), deque([(m, (1, 0, 0, 0), (0, 0, 0, 0))])
    while q:
        t, bs, rs = q.popleft()

        rs = (
            r0 if rs[0] > (r0 := t * mo - bs[0] * (t - 1)) else rs[0],
            r1 if rs[1] > (r1 := t * cs[3] - bs[1] * (t - 1)) else rs[1],
            r2 if rs[2] > (r2 := t * cs[5] - bs[2] * (t - 1)) else rs[2],
            rs[3]
        )

        if (t, bs, rs) in ss:
            continue
        ss.add((t, bs, rs))

        rs = tuple(rs[i] + bs[i] for i in range(4))

        if t == 1:
            b = max(b, rs[3])
            continue

        if rs[0]-bs[0] >= cs[4] and rs[2]-bs[2] >= cs[5]:
            q.append((t-1, (bs[0], bs[1], bs[2], bs[3]+1), (rs[0] - cs[4], rs[1], rs[2] - cs[5], rs[3])))
            continue

        q.append((t-1, bs, rs))

        if rs[0]-bs[0] >= cs[0] and bs[0] < mo:
            q.append((t-1, (bs[0]+1, bs[1], bs[2], bs[3]), (rs[0] - cs[0], rs[1], rs[2], rs[3])))
        if rs[0]-bs[0] >= cs[1] and bs[1] < cs[3]:
            q.append((t-1, (bs[0], bs[1]+1, bs[2], bs[3]), (rs[0] - cs[1], rs[1], rs[2], rs[3])))
        if rs[0]-bs[0] >= cs[2] and rs[1]-bs[1] >= cs[3] and bs[2] < cs[5]:
            q.append((t-1, (bs[0], bs[1], bs[2]+1, bs[3]), (rs[0] - cs[2], rs[1] - cs[3], rs[2], rs[3])))

    return b


def part_1(data): return sum(i * solve(cs, 24) for i, *cs in ns(data))

def part_2(data): return prod(solve(cs, 32) for _, *cs in ns(data)[:3])


EX_0 = """\
Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.""".replace("\n ", "").replace("\n\n", "\n")

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 33
    assert part_2(EX_0) == 56 * 62


if __name__ == "__main__":
    test()
