ks = [int(l.strip()) for l in open("../inputs/2020/25.txt")]

def f(k):
    a,t = 7,1
    while a != k:
        a = (a * 7) % 20201227
        t += 1
    return t

print("Part 1:", pow(ks[0], f(ks[1]), 20201227))