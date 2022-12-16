fs = [open("../inputs/2021/06.txt").read().count(str(i)) for i in range(9)]

for _ in range(80):
    fs = [fs[i%9] if i != 7 else fs[i%9]+fs[0] for i in range(1,10)]
print(f"Part 1: {sum(fs)}")

for _ in range(256-80):
    fs = [fs[i%9] if i != 7 else fs[i%9]+fs[0] for i in range(1,10)]
print(f"Part 2: {sum(fs)}")