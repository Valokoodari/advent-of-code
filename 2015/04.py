#!/usr/bin/python3
import hashlib

line = open("inputs/04.in", "r").readline()

def find(a):
    for i in range(0, 10000000):
        if (hashlib.md5((line + str(i)).encode()).hexdigest()[:a:] == "0"*a):
            break
    return i

print(find(5))
print(find(6))
