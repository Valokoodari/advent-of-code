ns = [int(l) for l in open("inputs/01.in").readlines()]

a = sum(1 if ns[i] < ns[i+1] else 0 for i in range(len(ns)-1))
b = sum(1 if sum(ns[i:i+3]) < sum(ns[i+1:i+4]) else 0 for i in range(len(ns)-3))

print(f"Part 1: {a}\nPart 2: {b}")