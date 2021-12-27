def abba(s):
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False


def aba(s, l):
    for i in range(len(s)-2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            if any(bab(l[j], s[i], s[i+1]) for j in range(1, len(l), 2)):
                return True
    return False


def bab(s, a, b):
    for i in range(len(s)-2):
        if s[i] == b and s[i+1] == a and s[i+2] == b:
            return True
    return False


def part_1(data):
    a, ls = 0, [l.replace("[", ",").replace("]", ",").split(",") for l in data.splitlines()]
    for l in ls:
        if any(abba(l[i]) for i in range(1, len(l), 2)):
            continue
        if any(abba(l[i]) for i in range(0, len(l), 2)):
            a += 1
    return a


def part_2(data):
    ls = [l.replace("[", ",").replace("]", ",").split(",") for l in data.splitlines()]
    return sum(1 for l in ls if any(aba(l[i], l) for i in range(0, len(l), 2)))


TEST_DATA_1 = """\
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn"""

TEST_DATA_2 = """\
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb"""

def test():
    assert(abba("abba"))
    assert(not abba("abcd"))
    assert(not abba("aaaa"))
    assert(abba("ioxxoj"))
    assert(part_1(TEST_DATA_1) == 2)
    assert(part_2(TEST_DATA_2) == 3)