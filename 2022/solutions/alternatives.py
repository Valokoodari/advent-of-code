# Day 6 - Faster method (1.7 ms vs. 2.7 ms for both parts)
def fast_solve(data, length):
    multiples_count = 0
    character_counts = [0]*26

    for index, character in enumerate(data):
        character_counts[ord(character)-97] += 1

        if character_counts[ord(character)-97] == 2:
            multiples_count += 1

        if index >= length:
            character_to_remove = ord(data[index-length])-97
            character_counts[character_to_remove] -= 1
            multiples_count -= 1 if character_counts[character_to_remove] == 1 else 0

        if index >= length - 1 and multiples_count == 0:
            return index + 1


# Day 8 - Slower more compact method (89 ms vs 18 ms)
from math import prod
from itertools import product

def part_2(data):
    ts = [[int(n) for n in l] for l in data.splitlines()]
    rs = list(zip(*ts))

    return max(prod(([i+1 for i, t in enumerate(ss) if t >= ts[r][c]] + [len(ss)])[0] for ss in (ts[r][c+1:], ts[r][c-1::-1], rs[c][r+1:], rs[c][r-1::-1])) for r, c in product(range(1, len(ts)-1), repeat=2))
