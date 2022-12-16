p1,p2,cs = {},{},[[int(n) for n in l.replace(" -> ", ",").split(",")] for l in open("../inputs/2021/05.txt").readlines()]

for ax,ay,bx,by in cs:
    mx,my = (ax-bx) // abs(ax-bx) if (ax-bx) != 0 else 0, (ay-by) // abs(ay-by) if (ay-by) != 0 else 0
    for p in [(bx+mx*i, by+my*i) for i in range(max(abs(ax-bx), abs(ay-by))+1)]:
        if p not in p1: p1[p],p2[p] = 0,0
        p1[p],p2[p] = p1[p]+1 if mx == 0 or my == 0 else p1[p], p2[p]+1

print(f"Part 1: {sum([1 for x in p1.values() if x > 1])}\nPart 2: {sum([1 for x in p2.values() if x > 1])}")