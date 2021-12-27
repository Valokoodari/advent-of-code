from collections import Counter


def part_1(data):
    ds = [[l[c] for l in data.splitlines()] for c in range(len(data.splitlines()[0]))]
    return "".join(Counter(l).most_common(1)[0][0] for l in ds)


def part_2(data):
    ds = [[l[c] for l in data.splitlines()] for c in range(len(data.splitlines()[0]))]
    return "".join(Counter(l).most_common()[-1][0] for l in ds)


TEST_DATA = """\
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

def test():
    assert(part_1(TEST_DATA) == "easter")
    assert(part_2(TEST_DATA) == "advent")