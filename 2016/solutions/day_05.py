from hashlib import md5


def part_1(data):
    i, p = 0, ""
    while True:
        if len(p) == 8:
            break
        hash = md5((data + str(i)).encode()).hexdigest()
        if hash[:5] == "00000":
            p += hash[5]
        i += 1
    return p


def part_2(data):
    i, p = 0, "________"
    while True:
        if "_" not in p:
            break
        hash = md5((data + str(i)).encode()).hexdigest()
        if hash[:5] == "00000":
            if hash[5].isdigit() and int(hash[5]) < 8 and p[int(hash[5])] == "_":
                p = p[:int(hash[5])] + hash[6] + p[int(hash[5])+1:]
        i += 1
    return p


def test():
    assert(part_1("abc") == "18f47a30")
    assert(part_2("abc") == "05ace8e3")