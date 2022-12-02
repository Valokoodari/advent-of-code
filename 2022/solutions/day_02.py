parse = lambda x: [(ord(a)-64, ord(b)-87) for a,b in [l.split(" ") for l in x.splitlines()]]


def part_1(data):
    return sum(b + (6 if a%3+1 == b else 3 if a == b else 0) for a, b in parse(data))


def part_2(data):
    return sum(3 + a if b == 2 else 6 + a%3+1 if b == 3 else (a+1)%3+1 for a,b in parse(data))


INPUT_1 = """\
A Y
B X
C Z"""

def test():
    assert(part_1(INPUT_1) == 15)
    assert(part_2(INPUT_1) == 12)
