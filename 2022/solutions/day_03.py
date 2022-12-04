from functools import reduce


fp = lambda c: ord(c) - (38 if c.isupper() else 96)
ps = lambda x: sum(fp(reduce(lambda a, b: set(a) & set(b), s).pop()) for s in x)

def part_1(data):
    return ps((l[:len(l)//2], l[len(l)//2:]) for l in data.splitlines())

def part_2(data):
    ls = data.splitlines()

    return ps((ls[i], ls[i+1], ls[i+2]) for i in range(0, len(ls), 3))


EX_1 = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def test():
    assert(part_1(EX_1) == 157)
    assert(part_2(EX_1) == 70)


if __name__ == "__main__":
    test()
