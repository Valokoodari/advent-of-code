import re

ls = [l.strip() for l in open("../inputs/2020/18.txt", "r").readlines()]

def a(ss):
    ss = ss.split(" ")
    sum = int(ss[0])
    for i in range(1, len(ss)-1, 2):
        sum = sum + int(ss[i+1]) if ss[i] == "+" else sum * int(ss[i+1])
    return sum

def aa(ss):
    while "+" in ss:
        ss = re.sub(r"(\d+) \+ (\d+)", lambda x: str(int(x[1]) + int(x[2])), ss)
    return a(ss)

a1,a2 = 0,0
for l1 in ls:
    l2 = l1
    while "(" in l1:
        l1 = re.sub(r"\(\d[^\(\)]*\)", lambda x: str(a(x[0][1:-1])), l1)
        l2 = re.sub(r"\(\d[^\(\)]*\)", lambda x: str(aa(x[0][1:-1])), l2)
    a1,a2 = a1+a(l1),a2+aa(l2)

print("Part 1:", a1)
print("Part 2:", a2)