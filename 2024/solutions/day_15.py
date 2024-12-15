DS = { "^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1) }


def parse(data, p = 1):
    ms, ins = data.split("\n\n")
    ms, ws, bs, pr, pc = ms.splitlines(), [], [], 0, 0
    for r in range(len(ms)):
        for c in range(len(ms[0])):
            if ms[r][c] == "#":
                ws.append((r, c*p))
                if p == 2:
                    ws.append((r, c*p+1))
            elif ms[r][c] == "O":
                bs.append((r, c*p))
            elif ms[r][c] == "@":
                pr, pc = r, c*p
    return ins, ws, bs, pr, pc


def part_1(data):
    ins, ws, bs, pr, pc = parse(data)

    def m(br, bc, dr, dc):
        if (br+dr, bc+dc) in ws or (br+dr, bc+dc) in bs and not m(br+dr, bc+dc, dr, dc):
            return False
        bs[bs.index((br,bc))] = (br+dr, bc+dc)
        return True

    for dr, dc in [DS[i] for i in ins.replace("\n", "")]:
        if (pr+dr, pc+dc) in ws or (pr+dr, pc+dc) in bs and not m(pr+dr, pc+dc, dr, dc):
            continue
        pr, pc = pr+dr, pc+dc

    return sum(100*br+bc for br, bc in bs)


def part_2(data):
    ins, ws, bs, pr, pc = parse(data, 2)

    def m(br, bc, dr, dc):
        if not (br, bc) in bs:
            return
        for i in range(-1, 2):
            if br+dr != br or bc+dc+i != bc:
                m(br+dr, bc+dc+i, dr, dc)
        bs[bs.index((br, bc))] = (br+dr, bc+dc)

    def cm(br, bc, dr, dc):
        if not (br, bc) in bs:
            return True
        if (br+dr, bc+dc) in ws or (br+dr, bc+dc+1) in ws:
            return False
        for i in range(-1, 2):
            if (br+dr != br or bc+dc+i != bc) and not cm(br+dr, bc+dc+i, dr, dc):
                return False
        return True

    for dr, dc in [DS[i] for i in ins.replace("\n", "")]:
        if (pr+dr, pc+dc) in ws or not cm(pr+dr, pc+dc, dr, dc) or not cm(pr+dr, pc+dc-1, dr, dc):
            continue
        m(pr+dr, pc+dc, dr, dc)
        m(pr+dr, pc+dc-1, dr, dc)
        pr, pc = pr+dr, pc+dc

    return sum(100*br+bc for br,bc in bs)


def test(run_tests = None):
    if not run_tests:
        from solutions.test import run_tests
    run_tests(15, part_1, part_2, False)


if __name__ == "__main__":
    from test import run_tests
    test(run_tests)
