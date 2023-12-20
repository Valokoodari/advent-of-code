from os import listdir, path


def get_tests(day):
    assert path.exists(f"examples/{day}")

    tests = []
    for file in listdir(f"examples/{day}"):
        data, answers = open(f"examples/{day}/{file}").read().rstrip().split("\n\n\n")
        answers = [answer.strip() for answer in answers.split("\n\n")]
        a1, a2 = [None if answer == "-" else answer for answer in answers]
        tests.append((data, a1, a2))

    return tests
