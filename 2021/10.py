ls = [l.strip() for l in open("inputs/10.in").read().strip().splitlines()]
bs = { "(": (")", 1), "[": ("]", 2), "{": ("}", 3), "<": (">", 4) }
es = { ")": 3, "]": 57, "}": 1197, ">": 25137 }

a,b,cs,js = 0,[],[],[]
for l in ls:
    s = []
    for c in l:
        if c in bs:
            s.append(c)
        elif bs.get(s[-1], [""])[0] == c:
            s.pop()
        else:
            a += es[c]
            cs.append(l)
            break
    if l not in cs:
        js.append(s)

for s in js:
    p = 0
    for c in s[::-1]:
        p = p * 5 + bs[c][1]
    b.append(p)

print(f"Part 1: {a}\nPart 2: {sorted(b)[len(b)//2]}")