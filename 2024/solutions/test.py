from os import listdir, path
from termcolor import colored


def get_tests(day):
    file_path = f"../inputs/2024/{day:02d}"
    assert path.exists(file_path)

    tests = []
    for file in listdir(file_path):
        if file == "input.txt":
            continue
        data, answers = open(f"{file_path}/{file}").read().rstrip().split("\n\n\n")
        answers = [answer.strip() for answer in answers.split("\n\n")]
        a1, a2 = [None if answer == "-" else answer for answer in answers]
        tests.append((data, a1, a2, file))

    assert len(tests) > 0
    return tests


def get_examples(day):
    return [data for data, *_ in get_tests(day)]


def run_tests(day, part_1, part_2, debug = False):
    tests = get_tests(day)

    assert len(tests) > 0
    for data, a1, a2, file in tests:
        assert data != "" and a1 or a2
        r1 = None if a1 == None else str(part_1(data))
        r2 = None if a2 == None else str(part_2(data))
        if debug:
            print(colored(file, "black", "on_light_blue"), end=" ")
            print(colored(r1, "grey" if a1 == None else "green" if a1 == r1 else "red"), end=" ")
            print(colored(r2, "grey" if a2 == None else "green" if a2 == r2 else "red"))
        assert a1 == None or r1 == a1
        assert a2 == None or r2 == a2
