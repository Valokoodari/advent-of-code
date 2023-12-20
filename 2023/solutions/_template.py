def part_1(data):
    ans = 0
    return ans


def part_2(data):
    ans = 0
    return ans


def test(get_tests = None):
    if not get_tests:
        from solutions.test import get_tests

    for data, a1, a2 in get_tests(0):
        assert data != None and a1 or a2
        assert a1 == None or str(part_1(data)) == a1
        assert a2 == None or str(part_2(data)) == a2


if __name__ == "__main__":
    from test import get_tests
    test(get_tests)
