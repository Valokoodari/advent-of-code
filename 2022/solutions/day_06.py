solve = lambda d, l: [i+l for i in range(len(d)-l) if len(set(d[i:i+l])) == l][0]

def part_1(data):
    return solve(data, 4)

def part_2(data):
    return solve(data, 14)


EX_0 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
EX_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
EX_2 = "nppdvjthqldpwncqszvftbrmjlhg"
EX_3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
EX_4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def test():
    assert part_1(EX_0) == 7
    assert part_1(EX_1) == 5
    assert part_1(EX_2) == 6
    assert part_1(EX_3) == 10
    assert part_1(EX_4) == 11

    assert part_2(EX_0) == 19
    assert part_2(EX_2) == 23
    assert part_2(EX_2) == 23
    assert part_2(EX_3) == 29
    assert part_2(EX_4) == 26


if __name__ == "__main__":
    test()
