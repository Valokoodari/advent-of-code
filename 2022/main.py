from termcolor import colored
from time import process_time
import sys

from solutions import day_01, day_02, day_03, day_04, day_05, day_06, day_07, \
    day_08, day_09, day_10


total_time = 0
NAMES = (
    "Calorie Counting",
    "Rock Paper Scissors",
    "Rucksack Reorganization",
    "Camp Cleanup",
    "Supply Stacks",
    "Tuning Trouble",
    "No Space Left On Device",
    "Treetop Tree House",
    "Rope Bridge",
    "Cathode-Ray Tube",
)


def test(day):
    try:
        eval(f"day_{day:02d}.test()")
        return colored("PASS", "green")
    except AssertionError:
        return colored("FAIL", "red")


def solve(day, part):
    data = open(f"inputs/{day:02d}.txt").read().rstrip()

    start_time = process_time()
    answer = eval(f"day_{day:02d}.part_{part}")(data)
    end_time = process_time()

    global total_time
    total_time += end_time - start_time

    return answer, end_time - start_time


def run(day):
    print(f"Day {day}: {NAMES[day-1]} ({test(day)})")

    answer, time1 = solve(day, 1)
    print(f"  Part 1: {colored(answer, 'cyan')}")

    answer, time2 = solve(day, 2)
    print(f"  Part 2: {colored(answer, 'cyan')}")

    time_str = colored(f"{(time1+time2)*1000:.3f} ms", "magenta")
    print(f"  ({time_str})\n")


def main():
    if len(sys.argv) == 1:
        for day in range(len(NAMES)):
            run(day+1)
    else:
        run(int(sys.argv[1]))

    time_str = colored(f"{total_time:.3f}", "magenta")
    avg_time_str = colored(f"{total_time/len(NAMES):.3f}", "magenta")

    print(f"Time:")
    print(f"  sum: {time_str} seconds")
    print(f"  avg: {avg_time_str} seconds")


if __name__ == "__main__":
    main()
