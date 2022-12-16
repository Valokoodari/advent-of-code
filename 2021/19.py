class S():
    rs = [
        lambda p: ( p[0],  p[1],  p[2]),
        lambda p: (-p[2],  p[1],  p[0]),
        lambda p: (-p[0],  p[1], -p[2]),
        lambda p: ( p[2],  p[1], -p[0]),
        lambda p: ( p[1], -p[0],  p[2]),
        lambda p: ( p[1],  p[2],  p[0]),
        lambda p: ( p[1],  p[0], -p[2]),
        lambda p: ( p[1], -p[2], -p[0]),
        lambda p: (-p[1],  p[0],  p[2]),
        lambda p: (-p[1], -p[2],  p[0]),
        lambda p: (-p[1], -p[0], -p[2]),
        lambda p: (-p[1],  p[2], -p[0]),
        lambda p: ( p[0],  p[2], -p[1]),
        lambda p: (-p[2],  p[0], -p[1]),
        lambda p: (-p[0], -p[2], -p[1]),
        lambda p: ( p[2], -p[0], -p[1]),
        lambda p: ( p[0], -p[1], -p[2]),
        lambda p: (-p[2], -p[1], -p[0]),
        lambda p: (-p[0], -p[1],  p[2]),
        lambda p: ( p[2], -p[1],  p[0]),
        lambda p: ( p[0], -p[2],  p[1]),
        lambda p: (-p[2], -p[0],  p[1]),
        lambda p: (-p[0],  p[2],  p[1]),
        lambda p: ( p[2],  p[0],  p[1]),
    ]

    def __init__(self, bs):
        self.bs = set(bs)
        self.r = -1
        self.p = (0, 0, 0)

    def frs(self) -> bool:
        self.r += 1
        if self.r == 24:
            self.r = -1
            return False
        return True

    def gbs(self) -> set:
        return set(S.rs[self.r if self.r >= 0 else 0](b) for b in self.bs)

    def sp(self, p) -> None:
        self.p = p

    def fcd(self, other: "S") -> int:
        return sum(abs(self.p[i] - other.p[i]) for i in range(3))


rs = [[tuple(map(int, x.split(","))) for x in l.strip().splitlines()[1:]] for l in open("../inputs/2021/19.txt").read().strip().split("\n\n")]

ss, gs = [S(s) for s in rs], set()
bs = ss[0].gbs()

while len(ss):
    c = False
    for s in ss:
        while s.frs():
            for b in s.gbs():
                for dx,dy,dz in [(a[0]-b[0], a[1]-b[1], a[2]-b[2]) for a in bs]:
                    o = sum(1 for x,y,z in s.gbs() if (dx+x, dy+y, dz+z) in bs)
                    if o >= 12:
                        s.sp((dx,dy,dz))
                        gs.add(s)
                        for a in s.gbs():
                            bs.add((a[0]+dx, a[1]+dy, a[2]+dz))
                        c = True
                        break
                else:
                    continue
                break
            else:
                continue
            break
    ss = [s for s in ss if s not in gs]
    if not c:
        break

print(f"Part 1: {len(bs)}")
print(f"Part 2: {max(s0.fcd(s1) for s0 in gs for s1 in gs)}")