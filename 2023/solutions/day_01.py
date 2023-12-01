def part_1(data):
    return sum(int(l[0] + l[-1]) for l in [[c for c in l if c.isdigit()] for l in data.splitlines()])


def part_2(data):
    for d, s in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        data = data.replace(s, s[0] + str(d+1) + s[-1])
    return part_1(data)


EX_0 = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

EX_1 = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 142
    assert part_2(EX_1) == 281


if __name__ == "__main__":
    test()
