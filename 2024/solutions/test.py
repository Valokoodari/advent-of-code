from os import listdir, path


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
        tests.append((data, a1, a2))

    assert len(tests) > 0
    return tests


def get_examples(day):
    return [data for data, *_ in get_tests(day)]


def run_tests(day, part_1, part_2):
    tests = get_tests(day)

    assert len(tests) > 0
    for data, a1, a2 in tests:
        assert data != "" and a1 or a2
        assert a1 == None or str(part_1(data)) == a1
        assert a2 == None or str(part_2(data)) == a2
