#!/usr/bin/python3
ls = [l.strip().split(" ") for l in open("inputs/08.in", "r").readlines()]

def run(sw):
    acc,p,ps = 0,0,[]
    while p < len(ls):
        if p in ps: return acc if sw == -1 else -1
        ps.append(p)
        acc += int(ls[p][1]) if ls[p][0] == "acc" else 0
        p += int(ls[p][1]) if (ls[p][0]=="jmp" and sw!=p) or (ls[p][0]=="nop" and sw==p) else 1
    return acc

def brute():
    for i,l in enumerate(ls):
        if l[0] == "acc": continue
        ans = run(i)
        if ans != -1: return ans

print("Part 1:", run(-1))
print("Part 2:", brute())