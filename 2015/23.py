ls = open("../inputs/2015/23.txt").read().rstrip().split("\n")

def f(a = 0):
    i, b = 0, 0
    while i < len(ls):
        match ls[i].split():
            case ["hlf", r]:
                a, b = a // 2 if r == "a" else a, b // 2 if r == "b" else b
                i += 1
            case ["tpl", r]:
                a, b = a * 3 if r == "a" else a, b * 3 if r == "b" else b
                i += 1
            case ["inc", r]:
                a, b = a + 1 if r == "a" else a, b + 1 if r == "b" else b
                i += 1
            case ["jmp", o]:
                i += int(o)
            case ["jie", r, o]:
                i += int(o) if (a if r == "a," else b) % 2 == 0 else 1
            case ["jio", r, o]:
                i += int(o) if (a if r == "a," else b) == 1 else 1
    return b

print(f())
print(f(1))
