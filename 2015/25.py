r,c = open("../inputs/2015/25.txt").read().strip().split(" row ")[1].split(", column ")
r,c = int(r), int(c[:-1])
n = sum(range(1,c+1)) + sum(range(c, r+c-1))

a = 20151125
for _ in range(n-1):
    a = (a*252533) % 33554393

print(f"Code: {a}")