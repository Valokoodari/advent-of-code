#!venv/bin/python3
ss = {complex(i,j): c for i,j,c in [(i,j,c) for i,l in enumerate(open("inputs/11.in", "r")) for j,c in enumerate(l.strip())]}

ds = ( 1-1j, -1, -1+1j, -1j, 1j, -1-1j, 1, 1+1j )

def ad(ss, k, p):
    if p == 1:
        return sum(1 for d in ds if (k+d in ss) and (ss[k+d] == "#"))
    t = 0
    for d in ds:
        for i in range(1, len(ss)//2):
            if not k+d*i in ss: break
            if ss[k+d*i] == "#": t += 1
            if ss[k+d*i] != ".": break
    return t

def sim(ss, p, c):
    while c:
        c,cs = 0,ss.copy()
        for k,v in ss.items():
            if v == "L" and ad(ss, k, p) == 0: c,cs[k] = c+1,"#"
            if v == "#" and ad(ss, k, p) >= 3+p: c,cs[k] = c+1,"L"
        ss = cs
    return sum([1 for s in ss.values() if s == "#"])

print("Part 1:", sim(ss, 1, 1))
print("Part 2:", sim(ss, 2, 1))