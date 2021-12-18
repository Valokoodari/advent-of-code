ns = [eval(x.strip()) for x in open('inputs/18.txt').read().strip().splitlines()]

def fsm(n):
    return n if type(n) == int else 3*fsm(n[0]) + 2*fsm(n[1])

def fsr(n):
    while fse(n) or fss(n):
        pass
    return n

def fse(n, ps=[]):
    if type(n) == int:
        return False
    if len(ps) < 4:
        return fse(n[0], ps+[(n, 0)]) or fse(n[1], ps+[(n, 1)])
    for a,b in ((0, 1), (1, 0)):
        for p,i in ps[::-1]:
            if i == a:
                if type(p[b]) == int:
                    p[b] += n[b]
                else:
                    p = p[b]
                    while type(p[a]) == list:
                        p = p[a]
                    p[a] += n[b]
                break
    ps[-1][0][ps[-1][1]] = 0
    return True

def fss(n, ps=[]):
    if type(n) == int:
        if n < 10:
            return False
        ps[-1][0][ps[-1][1]] = [n//2, (n+1)//2]
        return True
    return fss(n[0], ps+[(n, 0)]) or fss(n[1], ps+[(n, 1)])

s = ns[0]
[s := fsr([s, eval(repr(n))]) for n in ns[1:]]

print(f"Part 1: {fsm(s)}")
print(f"Part 2: {max(fsm(fsr([eval(repr(i)), eval(repr(j))])) for i in ns for j in ns if i != j)}")