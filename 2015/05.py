#!/usr/bin/python3
lines = open("inputs/05.in", "r").readlines()

def vowels(s):
    v = ["a", "e", "i", "o", "u"]
    a = 0

    for c in s:
        if c in v:
            a += 1
            if a == 3:
                return True
    return False

def double(s):
    for i in range(0, len(s)-2):
        if s[i:i+1:] == s[i+1:i+2:]:
            return True
    return False

def fail(s):
    p = ["ab", "cd", "pq", "xy"]

    for i in range(0, len(s)-2):
        if s[i:i+2:] in p:
            return False
    return True

def part_one(lines):
    nice = 0
    for line in lines:
        if vowels(line) and double(line) and fail(line):
            nice += 1

    return nice

def pair(s):
    for i in range(0, len(s)-3):
        for j in range(i+2, len(s)-1):
            if s[i:i+2:] == s[j:j+2:]:
                return True
    return False

def one_between(s):
    for i in range(0, len(s)-3):
        if s[i:i+1:] == s[i+2:i+3:]:
            return True
    return False

def part_two(lines):
    nice = 0
    for line in lines:
        if pair(line) and one_between(line):
            nice += 1

    return nice

print("Part 1: " + str(part_one(lines)))
print("Part 2: " + str(part_two(lines)))
