#!venv/bin/python3
ls = [[l.strip()[:-1].split(" (contains ")[0].split(" "), l.strip()[:-1].split(" (contains ")[1].split(", ")] for l in open("inputs/21.in", "r").readlines()]

al = {}
for l in ls:
    for g in l[1]:
        if g not in al:
            al[g] = set(l[0].copy())
        else:
            al[g] &= set(l[0])

ng = {}
for a,b in al.items():
    for n in b:
        if n not in ng:
            ng[n] = [a]
        else:
            ng[n].append(a)

while max([len(b) for b in ng.values()]) > 1:
    for a,b in ng.items():
        if len(b) == 1:
            for c in ng:
                if c == a: continue
                ng[c] = [n for n in ng[c] if n != b[0]]

ng = {v[0]: k for k,v in ng.items()}

print("Part 1:", sum([1 for l in ls for g in l[0] if g not in ng.values()]))
print("Part 2:", ",".join([ng[g] for g in sorted(ng)]))