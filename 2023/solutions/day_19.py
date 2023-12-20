from math import prod


def parse(d):
    (rsd, psd), rs = d.replace("}", "").split("\n\n"), {}
    for r in rsd.splitlines():
        n, os = r.split("{")
        rs[n] = []
        for o in os.split(","):
            if ":" in o:
                e, d = o.split(":")
                rs[n].append(((e[0], e[1], int(e[2:])), d))
            else:
                rs[n].append(o)
    return rs, [{ k: int(v) for k, v in [s.split("=") for s in p.replace("{","").split(",")] } for p in psd.splitlines()]


def part_1(data):
    ans, (rs, ps) = 0, parse(data)

    for p in ps:
        w = "in"
        while w not in ["R", "A"]:
            for r in rs[w]:
                if type(r) == str:
                    w = r
                    break
                k, v, vv = r[0]
                if v == "<" and p[k] < vv or v == ">" and p[k] > vv:
                    w = r[1]
                    break
        if w == "A":
            ans += sum(p.values())

    return ans


def part_2(data):
    ans, (rs, _), prs = 0, parse(data), [("in", {"x": (1,4000), "m": (1,4000), "a": (1,4000), "s": (1,4000)})]

    while prs:
        nprs = []
        while prs:
            w, ps = prs.pop()
            if w == "A":
                ans += prod([b - a + 1 for a, b in ps.values()])
                continue
            if w == "R":
                continue
            for r in rs[w]:
                if type(r) == str:
                    nprs.append((r, ps))
                    break
                k, v, vv = r[0]
                if v == "<":
                    nprs.append((r[1], { pk: (pa, pb) if pk != k else (pa, min(vv-1, pb)) for pk, (pa, pb) in ps.items() }))
                    ps[k] = (vv, ps[k][1])
                elif v == ">":
                    nprs.append((r[1], { pk: (pa, pb) if pk != k else (max(vv+1, pa), pb) for pk, (pa, pb) in ps.items() }))
                    ps[k] = (ps[k][0], vv)
        prs = nprs

    return ans


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(19, part_1, part_2)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
