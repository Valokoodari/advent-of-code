from termcolor import colored
from time import time

from solutions import day_01, day_02, day_03


NAMES = (
    "No Time for a Taxicab",
    "Bathroom Security",
    "Squares With Three Sides",
)


def test(day):
    try:
        eval(f"day_{day:02d}.test()")
        return colored("PASS", "green")
    except AssertionError:
        return colored("FAIL", "red")


def solve(day, part):
    data = open(f"inputs/{day:02d}.txt").read().strip()
    return eval(f"day_{day:02d}.part_{part}")(data)


def run(day):
    print(f"Day {day}: {NAMES[day-1]} ({test(day)})")
    print(f"  Part 1: {colored(solve(day, 1), 'cyan')}")
    print(f"  Part 2: {colored(solve(day, 2), 'cyan')}\n")


start_time = time()
for day in range(len(NAMES)):
    run(day+1)
end_time = time()
time_str = colored(f"{end_time - start_time:.3f}s", "cyan")
print(f"Total time: {time_str} seconds")