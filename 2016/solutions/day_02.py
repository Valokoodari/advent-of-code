KS1 = ((1,2,3),(4,5,6),(7,8,9))
KS2 = (
    ('_', '_', '1', '_', '_'),
    ('_', '2', '3', '4', '_'),
    ('5', '6', '7', '8', '9'),
    ('_', 'A', 'B', 'C', '_'),
    ('_', '_', 'D', '_', '_'),
)


class KP:
    DS = { 'U': (0,-1), 'D': (0,1), 'L': (-1,0), 'R': (1,0) }

    def __init__(self, p, ks):
        self.p = p
        self.ks = ks

    def fm(self, d):
        np = (self.p[0] + self.DS[d][0], self.p[1] + self.DS[d][1])
        if np in self.ks:
            self.p = np

    def gk(self):
        return self.ks[self.p]


def part_1(data):
    a, kp = [], KP((1,1), {(x,y): k for y,r in enumerate(KS1) for x,k in enumerate(r)})
    for r in data.splitlines():
        for d in r:
            kp.fm(d)
        a.append(kp.gk())
    return "".join(str(k) for k in a if k)


def part_2(data):
    a, kp = [], KP((0,2), {(x,y): k for y,r in enumerate(KS2) for x,k in enumerate(r) if k != '_'})
    for r in data.splitlines():
        for d in r:
            kp.fm(d)
        a.append(kp.gk())
    return "".join(str(k) for k in a if k)


def test():
    assert(part_1("ULL\nRRDDD\nLURDL\nUUUUD") == "1985")
    assert(part_2("ULL\nRRDDD\nLURDL\nUUUUD") == "5DB3")