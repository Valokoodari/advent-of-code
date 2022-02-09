def part_1(data):
    l = 0
    while "(" in data:
        l += data.find("(")
        data = data[data.find("(")+1:]
        m = [int(n) for n in data[:data.find(")")].split("x")]
        data = data[data.find(")")+1+m[0]:]
        l += m[1]*m[0]
    return l + len(data)


def part_2(data):
    l = 0
    while "(" in data:
        l += data.find("(")
        data = data[data.find("(")+1:]
        m = [int(n) for n in data[:data.find(")")].split("x")]
        l += m[1] * part_2(data[data.find(")")+1:data.find(")")+1+m[0]])
        data = data[data.find(")")+1+m[0]:]
    return l + len(data)


def test():
    assert(part_1("ADVENT") == 6)
    assert(part_1("A(1x5)BC") == 7)
    assert(part_1("(3x3)XYZ") == 9)
    assert(part_1("A(2x2)BCD(2x2)EFG") == 11)
    assert(part_1("(6x1)(1x3)A") == 6)
    assert(part_1("X(8x2)(3x3)ABCY") == 18)

    assert(part_2("(3x3)XYZ") == 9)
    assert(part_2("X(8x2)(3x3)ABCY") == 20)
    assert(part_2("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920)
    assert(part_2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445)