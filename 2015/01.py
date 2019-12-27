#!/usr/bin/python3
f,b,i = 0,0,1
for c in open("inputs/01.in", 'r').readline():
    if c == '(': f += 1
    else: f -= 1
    if (f == -1 and b == 0):
        b = i
    i += 1

print(f, b)