#!venv/bin/python3
import re

ps = [p.split("\n") for p in open("inputs/19.in", "r").read().split("\n\n")]
rs = {l[0][0]: [[l[i][0]] if len(l[i]) == 1 else [l[i][0], l[i][1]] for i in range(1, len(l))] for l in [[p.split(" ") for p in re.split(": | \| ", l)] for l in ps[0]]}

h = {}
def f(n, m):
    if tuple([n,m]) not in h:
        if m == 2 and n == "8": return f("42", m) + "+"
        if m == 2 and n == "11": return "(?:" + "|".join(f("42",m)*c+f("31",m)*c for c in range(1,10)) + ")"
        h[tuple([n,m])] = rs[n][0][0][1] if "\"" in rs[n][0][0] else "(?:" + "|".join(["".join(f(p, m) for p in r) for r in rs[n]]) + ")"
    return h[tuple([n,m])]

print("Part 1:", sum([1 for s in ps[1] if re.fullmatch(f("0", 1), s)]))
print("Part 2:", sum([1 for s in ps[1] if re.fullmatch(f("0", 2), s)]))