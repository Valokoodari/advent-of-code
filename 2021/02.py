cs = [l.split(" ") for l in open("inputs/02.in").readlines()]

h,a,d = 0,0,0
for c,x in cs:
    if c == "forward":
        h += int(x)
        d += a * int(x)
    if c == "down":
        a += int(x)
    if c == "up":
        a -= int(x)

print(f"Part 1: {a*h}\nPart 2: {d*h}")