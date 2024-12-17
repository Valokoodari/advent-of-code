def parse(data):
    rs, ps = data.split("\n\n")
    return [int(r.split(": ")[1]) for r in rs.split("\n")], [int(n) for n in ps.split(": ")[1].split(",")]


def run(rs, ps):
    def c(n):
        return n if n < 4 else rs[0] if n == 4 else rs[1] if n == 5 else rs[2]

    i, o = 0, []
    while i < len(ps) - 1:
        match ps[i]:
            case 0:
                rs[0], i = rs[0] >> c(ps[i+1]), i + 2
            case 1:
                rs[1], i = rs[1] ^ ps[i+1], i + 2
            case 2:
                rs[1], i = c(ps[i+1]) & 0b111, i + 2
            case 3:
                i = ps[i+1] if rs[0] else i + 2
            case 4:
                rs[1], i = rs[1] ^ rs[2], i + 2
            case 5:
                o.append(c(ps[i+1]) & 0b111)
                i += 2
            case 6:
                rs[1], i = rs[0] >> c(ps[i+1]), i + 2
            case 7:
                rs[2], i = rs[0] >> c(ps[i+1]), i + 2
    return o


def b(s, c, ps):
    for a in range(8):
        if run([s * 8 + a, 0, 0], ps) == ps[c:]:
            if c == 0:
                return s * 8 + a
            r = b(s * 8 + a, c - 1, ps)
            if r is not None:
                return r


def part_1(data):
    return ",".join(map(str, run(*parse(data))))


def part_2(data):
    ps = parse(data)[1]
    return b(0, len(ps) - 1, ps)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(17, part_1, part_2, False)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
