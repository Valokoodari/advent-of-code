#!/usr/bin/python3
import re

ps = open("inputs/04.in", "r").read().split("\n\n")

fs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
es = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def b(v, l, h):
    if not v.isdigit():
        return False
    return l <= int(v) <= h

def ca(s):
    for f in fs:
        if not f in s: return False
    return True

def dv(s):
    if not ca(s): return False
    p = re.split("[:\n ]", s)

    if not b(p[p.index("byr")+1], 1920, 2002): return False
    if not b(p[p.index("iyr")+1], 2010, 2020): return False
    if not b(p[p.index("eyr")+1], 2020, 2030): return False

    v = p[p.index("hgt")+1]
    if v[-2:] == "cm" and not b(v[:-2], 150, 193): return False
    if v[-2:] == "in" and not b(v[:-2], 59, 76): return False
    if v[-2:] not in ["cm", "in"]: return False

    if not re.search("^#[0-9a-f]{6}$", p[p.index("hcl")+1]): return False
    if p[p.index("ecl")+1] not in es:  return False
    if not re.search("^[0-9]{9}$", p[p.index("pid")+1]): return False

    return True

print("Part 1:", sum(ca(p) for p in ps))
print("Part 2:", sum(dv(p) for p in ps))