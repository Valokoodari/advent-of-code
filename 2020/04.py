#!/usr/bin/python3
import re

ps = open("inputs/04.in", "r").read().split("\n\n")

fs = {
    "hgt": "(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))",
    "ecl": "(amb|blu|brn|gry|grn|hzl|oth)",
    "byr": "(19[2-9][0-9]|200[0-2])",
    "iyr": "(201[0-9]|2020)",
    "eyr": "(202[0-9]|2030)",
    "hcl": "#[0-9a-f]{6}",
    "pid": "[0-9]{9}"
}

def ca(s):
    for f in fs:
        if not f in s: return False
    return True

def dv(s):
    for k,v in fs.items():
        if not re.fullmatch("^.*"+k+":"+v+"([ \n].*|)$", s, re.DOTALL): return False
    return True

print("Part 1:", sum(ca(p) for p in ps))
print("Part 2:", sum(dv(p) for p in ps))