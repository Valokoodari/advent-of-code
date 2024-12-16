from collections import Counter


H, W, T = 103, 101, 100


def part_1(data):
    ps = [((r[0]+r[2]*T)%W, (r[1]+r[3]*T)%H) for r in [[int(p) for p in r.split(",")] for r in data.replace("p=","").replace(" v=",",").splitlines()]]
    c = Counter(1 if x < mx and y < my else 2 if x < mx and y > my else 3 if x > mx and y < my else 4 for x, y in ps if x != (mx:=W//2) and y != (my:=H//2))
    return c[1] * c[2] * c[3] * c[4]


def part_2(data):
    rs = [[int(p) for p in r.split(",")] for r in data.replace("p=","").replace(" v=",",").splitlines()]
    ps = lambda t: [((r[0] + r[2] * t) % W, (r[1] + r[3] * t) % H) for r in rs]

    lc, lr = (0, W*H**2), (0, W*H**2)
    for t in range(1, max(H, W)):
        vc, vr = 0, 0
        for c, r in ps(t):
            vc, vr = vc + abs(c - W//2), vr + abs(r - H//2)
        lc, lr = (t, vc) if vc < lc[1] else lc, (t, vr) if vr < lr[1] else lr

    return lc[0] + ((pow(W, -1, H) * (lr[0] - lc[0])) % H) * W


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    global W, H
    w, h, W, H = W, H, 11, 7
    run_tests(14, part_1, part_2, False)
    W, H = w, h


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
