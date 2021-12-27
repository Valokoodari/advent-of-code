from collections import Counter


def part_1(data):
    a, rs = 0, tuple(map(lambda r: ("".join(r[0].split("-")[:-1]), int(r[0].split("-")[-1]), r[1]), [l[:-1].split("[") for l in data.splitlines()]))

    for r in rs:
        c = "".join(map(lambda x: x[1], sorted(list((v,k) for k,v in Counter(r[0]).items()), key=lambda x: (-x[0],x[1]))[:5]))
        a += (c == r[2]) * r[1]

    return a


def part_2(data):
    rs = tuple(map(lambda r: ("-".join(r[0].split("-")[:-1]), int(r[0].split("-")[-1]), r[1]), [l[:-1].split("[") for l in data.splitlines()]))
    for r in rs:
        c = "".join(map(lambda x: x[1], sorted(list((v,k) for k,v in Counter(r[0]).items() if k != "-"), key=lambda x: (-x[0],x[1]))[:5]))
        if c != r[2]:
            continue
        if "pole" in "".join(chr((ord(c)-ord('a')+r[1])%(ord('z')-ord('a')+1)+ord('a')) if c != "-" else "-" for c in r[0]):
            return r[1]


TEST_DATA = """\
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""

def test():
    assert(part_1(TEST_DATA) == 1514)