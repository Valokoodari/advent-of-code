from termcolor import colored

from solutions import day_01


names = (
    "No Time for a Taxicab",
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
    print(f"Day {day}: {names[day-1]} ({test(day)})")
    print(f"  Part 1: {colored(solve(day, 1), 'cyan')}")
    print(f"  Part 2: {colored(solve(day, 2), 'cyan')}\n")


for day in range(1, 2):
    run(day)