#!/usr/bin/python3
import re

lights = [[False]*1000 for i in range(1000)]
lights1 = [[0]*1000 for i in range(1000)]

def toggle(s):
    s = re.split("[ ,]", s[7::])
    for i in range(int(s[0]), int(s[3])+1):
        for j in range(int(s[1]), int(s[4])+1):
            lights[i][j] = not lights[i][j]
            lights1[i][j] += 2

def turn_on(s):
    s = re.split("[ ,]", s[8::])
    for i in range(int(s[0]), int(s[3])+1):
        for j in range(int(s[1]), int(s[4])+1):
            lights[i][j] = True
            lights1[i][j] += 1

def turn_off(s):
    s = re.split("[ ,]", s[9::])
    for i in range(int(s[0]), int(s[3])+1):
        for j in range(int(s[1]), int(s[4])+1):
            lights[i][j] = False
            lights1[i][j] -= 1
            if (lights1[i][j] < 0):
                lights1[i][j] = 0

for line in open("inputs/06.in", "r").readlines():
    if "toggle" in line:
        toggle(line)
    if "turn on" in line:
        turn_on(line)
    if "turn off" in line:
        turn_off(line)

on = 0
for row in lights:
    for light in row:
        if light:
            on += 1
print("Part 1: " + str(on))

brightness = 0
for row in lights1:
    for light in row:
        brightness += light
print("Part 2: " + str(brightness))
