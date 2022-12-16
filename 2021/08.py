ls = [l.strip().split(" | ") for l in open("../inputs/2021/08.txt").readlines()]
ls = [([tuple(sorted([c for c in n])) for n in p.split(" ")], [tuple(sorted([c for c in n])) for n in o.split(" ")]) for p,o in ls]

s, sd = 0, { 2: 1, 4: 4, 3: 7, 7: 8 }
for p,o in ls:
    ns = { sd[len(n)]: n for n in p if len(n) in sd }

    ns[3] = [n for n in p if len(n) == 5 and len([c for c in n if c in ns[1]]) == 2][0]
    ns[6] = [n for n in p if len(n) == 6 and len([c for c in n if c in ns[7]]) == 2][0]
    ns[9] = [n for n in p if len(n) == 6 and len([c for c in n if c in ns[4]]) == 4][0]

    p = [n for n in p if n not in ns.values()]
    ns[5] = [n for n in p if len(n) == 5 and len([c for c in n if c in ns[4]]) == 3][0]
    ns[2] = [n for n in p if len(n) == 5 and len([c for c in n if c in ns[4]]) == 2][0]
    ns[0] = [n for n in p if len(n) == 6][0]

    ns = { n: cs for cs,n in ns.items() }
    s += int("".join([str(ns[n]) if n in ns else "0" for n in o]))

print(f"Part 1: {sum([sum([1 for n in o if len(n) in sd]) for _,o in ls])}\nPart 2: {s}")