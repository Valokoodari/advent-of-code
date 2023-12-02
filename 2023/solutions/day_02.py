LS = { "red": 12, "green": 13, "blue": 14 }


def part_1(data):
    ans = 0
    for l in data.splitlines():
        (g, ss), v = l.split(":"), True
        for s in ss.split(";"):
            for c in s.split(","):
                n, c = c.strip().split();
                if LS[c] < int(n):
                    v = False
            if not v:
                break
        ans += int(g.split()[1]) if v else 0
    return ans


def part_2(data):
    ans = 0
    for line in data.splitlines():
        cs = { "red": 0, "green": 0, "blue": 0 }
        _, ss = line.split(":")
        for s in ss.split(";"):
            for c in s.split(","):
                n, c = c.strip().split(" ");
                cs[c] = max(int(n), cs[c])
        ans += cs["red"] * cs["green"] * cs["blue"]
    return ans


EX_0 = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == 8
    assert part_2(EX_0) == 2286


if __name__ == "__main__":
    test()
