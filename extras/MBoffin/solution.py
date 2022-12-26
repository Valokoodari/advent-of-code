from termcolor import colored
from time import process_time

NAME = "u/MBoffin: The Hidden Gift Card"


def part_1(data):
    return "".join(data[i] for i in range(len(data)-1) if data[i] == data[i+1] and (data[i].isupper() or data[i] == "-"))

def part_2(data):
    return "".join(data[i] for i in range(len(data)-1) if data[i] == data[i+1] and data[i].isnumeric())


EX_0 = """\
7*(()HsdiKK%322sbu--1^*NsK##-DHHdMm&&--vhso55eeneskTT@#1k"""

def test():
    assert EX_0 != ""
    assert part_1(EX_0) == "K-H-T"
    assert part_2(EX_0) == "25"


if __name__ == "__main__":
    test_results = colored("PASS", "green")
    try:
        test()
    except AssertionError:
        test_results = colored("FAIL", "red")

    print(f"{NAME} ({test_results})")

    with open("input.txt") as f:
        data = f.read().rstrip()

    start_time_1 = process_time()
    print("  Part 1:", colored(part_1(data), "cyan"))
    end_time_1 = process_time()

    start_time_2 = process_time()
    print("  Part 2:", colored(part_2(data), "cyan"))
    end_time_2 = process_time()

    time_str_1 = colored(f"{(end_time_1 - start_time_1)*1000:.3f}", "magenta")
    time_str_2 = colored(f"{(end_time_2 - start_time_2)*1000:.3f}", "magenta")
    time_str = colored(f"{(end_time_1 + end_time_2 - start_time_1 - start_time_2)*1000:.3f} ms", "magenta")

    print(f"  ({time_str})" + f" [{time_str_1} / {time_str_2}]")
