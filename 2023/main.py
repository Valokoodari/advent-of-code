from termcolor import colored
from time import process_time
import sys

from solutions import day_01, day_02, day_03, day_04, day_05, day_06, day_07, \
    day_08, day_09, day_10, day_11, day_12, day_13, day_14


hide = False
total_time = 0
YEAR = 2023
NAMES = (
    "Trebuchet?!",
    "Cube Conundrum",
    "Gear Ratios",
    "Scratchcards",
    "If You Give A Seed A Fertilizer",
    "Wait For It",
    "Camel Cards",
    "Haunted Wasteland",
    "Mirage Maintenance",
    "Pipe Maze",
    "Cosmic Expansion",
    "Hot Springs",
    "Point of Incidence",
    "Parabolic Reflector Dish",
)


def test(day):
    try:
        eval(f"day_{day:02d}.test()")
        return colored("PASS", "green")
    except AssertionError:
        return colored("FAIL", "red")


def solve(day, part):
    data = open(f"../inputs/{YEAR}/{day:02d}.txt").read().rstrip()

    start_time = process_time()
    answer = eval(f"day_{day:02d}.part_{part}")(data)
    end_time = process_time()

    global total_time
    total_time += end_time - start_time

    return answer, end_time - start_time


def run(day):
    time1, time2 = 0, 0
    print(f"Day {day}: {NAMES[day-1]} ({test(day)})")

    answer, time1 = solve(day, 1)
    answer = "[hidden]" if hide else answer
    print(f"  Part 1: {colored(answer, 'cyan')}")

    if day != 25:
        answer, time2 = solve(day, 2)
        answer = "[hidden]" if hide else answer
        print(f"  Part 2: {colored(answer, 'cyan')}")

    time_str_1 = colored(f"{time1*1000:.3f}", "magenta")
    time_str_2 = colored(f"{time2*1000:.3f}", "magenta")
    time_str = colored(f"{(time1+time2)*1000:.3f} ms", "magenta")
    print(f"  ({time_str})" + (f" [{time_str_1} / {time_str_2}]" if day != 25 else "") + "\n")


def main():
    if "-h" in sys.argv:
        global hide
        hide = True
        sys.argv.remove("-h")
    if len(sys.argv) == 1:
        for day in range(len(NAMES)):
            run(day+1)
    elif len(sys.argv) == 2 and sys.argv[1].isdigit():
        if (day := int(sys.argv[1])) <= len(NAMES):
            run(day)
        else:
            print(colored(f"Day {day} does not exist{' yet' if day <= 25 else ''}.\n", "red"))
    elif sys.argv[1] in ("-s", "--skip"):
        days = [int(day) for day in sys.argv[2:] if day.isdigit()]
        for day in range(len(NAMES)):
            if day+1 not in days:
                run(day+1)
    else:
        print(colored("Invalid arguments.\n", "red"))

    time_str = colored(f"{total_time:.3f}", "magenta")
    avg_time_str = colored(f"{total_time/len(NAMES):.3f}", "magenta")

    print(f"Time:")
    print(f"  sum: {time_str} seconds")
    print(f"  avg: {avg_time_str} seconds")


if __name__ == "__main__":
    main()
