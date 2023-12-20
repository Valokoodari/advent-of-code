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


EX_0 = """\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 19114
    assert part_2(EX_0) == 167409079868000


if __name__ == "__main__":
    test()
