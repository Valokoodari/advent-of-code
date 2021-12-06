ds = open("inputs/04.in").read().split("\n\n")
ws,ns = [],[int(n) for n in ds.pop(0).split(",")]
bs = [[[(False, int(n)) for n in row.split(" ") if n != ""] for row in b.splitlines()] for b in ds]

for n in ns:
    bs = [[[(True, c[1]) if c[1] == n else c for c in r] for r in b] for b in bs]
    for b in bs:
        if 5 in [sum([1 for c in r if c[0]]) for r in b] + [sum([1 for c in r if c[0]]) for r in zip(*b)]:
            ws.append((b,n))
    bs = [b for b in bs if b not in [bn[0] for bn in ws]]

score = lambda bn: bn[1] * sum([x[1] for x in list(filter(lambda x: not x[0], sum(bn[0], [])))])
print(f"Part 1: {score(ws[0])}\nPart 2: {score(ws[-1])}")