#!/usr/bin/python3
lines = open("inputs/07.in", "r").readlines()
for i,line in enumerate(lines):
    lines[i] = line.split("\n")[0]

l = lines.copy();

wires = {}

def func_set(p, i):
    if p[0].isdigit():
        wires[p[2]] = int(p[0])
        lines.pop(i)
    elif p[0] in wires.keys():
        wires[p[2]] = wires[p[0]]
        lines.pop(i)

def func_and(p, i):
    if p[0].isdigit() and p[2] in wires.keys():
        wires[p[4]] = int(p[0]) & wires[p[2]]
        lines.pop(i)
    if p[0] in wires.keys() and p[2] in wires.keys():
        wires[p[4]] = wires[p[0]] & wires[p[2]]
        lines.pop(i)

def func_or(p, i):
    if p[0] in wires.keys() and p[2] in wires.keys():
        wires[p[4]] = wires[p[0]] | wires[p[2]]
        lines.pop(i)

def func_rshift(p, i):
    if p[0] in wires.keys():
        wires[p[4]] = wires[p[0]] >> int(p[2])
        lines.pop(i)

def func_lshift(p, i):
    if p[0] in wires.keys():
        wires[p[4]] = wires[p[0]] << int(p[2])
        lines.pop(i)

def func_not(p, i):
    if p[1] in wires.keys():
        wires[p[3]] = 65535 - wires[p[1]]
        lines.pop(i)

def run():
    i = 0
    while len(lines) > 0:
        parts = lines[i].split(" ")
        if "AND" in parts:
            func_and(parts, i)
        elif "NOT" in parts:
            func_not(parts, i)
        elif "RSHIFT" in parts:
            func_rshift(parts, i)
        elif "LSHIFT" in parts:
            func_lshift(parts, i)
        elif "OR" in parts:
            func_or(parts, i)
        else:
            func_set(parts, i)

        i += 1
        if i >= len(lines):
            i = 0

run()
print("Part 1: " + str(wires["a"]))

lines = l
wires = {"b": wires["a"]}
run()
print("Part 2: " + str(wires["a"]))
