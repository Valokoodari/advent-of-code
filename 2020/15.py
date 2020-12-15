#!venv/bin/python3
turns = {int(n): [i] for i,n in enumerate(open("inputs/15.in", "r").readline().split(","))}

a1,l = 0,[k for k in turns][-1]
for i in range(len(turns), 30000000):
    a = 0
    if len(turns[l]) >= 2:
        a = i - 1 - turns[l][-2]
    if a not in turns:
        turns[a] = [i]
    else:
        turns[a].append(i)
    l = a
    if i+1 == 2020:
        a1 = l

print("Part 1:", a1)
print("Part 2:", l)