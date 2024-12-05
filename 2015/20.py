from collections import defaultdict

n = int(open("../inputs/2015/20.txt").read().strip())

h1, h2 = defaultdict(int), defaultdict(int)
for i in range(1, n // 10):
    for j in range(i, n // 10, i):
        h1[j] += i
    for j in range(i, min(n // 11, (i+1) * 50), i):
        h2[j] += i

for i in range(1, max(h1.keys())):
    if h1[i] * 10 >= n:
        print(i)
        break

for i in range(1, max(h2.keys())):
    if h2[i] * 11 >= n:
        print(i)
        break
