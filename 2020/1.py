#!/usr/bin/python3
import itertools

lines = list(map(int, open("inputs/1.in", "r").readlines()))

for a,b in itertools.combinations(lines, 2):
    if (a + b == 2020):
        print("Part 1: " + str(a * b))

for a,b,c in itertools.combinations(lines, 3):
    if (a + b + c == 2020):
        print("Part 2: " + str(a * b * c))
