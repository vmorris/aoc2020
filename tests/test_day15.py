from aoc2020.day15 import solution


def test_speak_number():
    starting_numbers = [0, 3, 6]
    actual = solution.speak_number(1, starting_numbers)
    assert 0 == actual
    actual = solution.speak_number(2, starting_numbers)
    assert 3 == actual
    actual = solution.speak_number(3, starting_numbers)
    assert 6 == actual
    actual = solution.speak_number(4, starting_numbers)
    assert 0 == actual
    actual = solution.speak_number(5, starting_numbers)
    assert 3 == actual
    actual = solution.speak_number(6, starting_numbers)
    # assert 3 == actual
    # actual = solution.speak_number(7, starting_numbers)
    # assert 1 == actual
    # actual = solution.speak_number(8, starting_numbers)
    # assert 0 == actual
    # actual = solution.speak_number(9, starting_numbers)
    # assert 4 == actual
    # actual = solution.speak_number(10, starting_numbers)
    # assert 0 == actual


def test_solve_part1():
    input_data = [
        [0, 3, 6],
        [1, 3, 2],
        [2, 1, 3],
        [1, 2, 3],
        [2, 3, 1],
        [3, 2, 1],
        [3, 1, 2],
    ]

    expected_results = [436, 1, 10, 27, 78, 438, 1836]
    # for index, data in enumerate(input_data):
    #    expected = expected_results[index]
    #    actual = solution.solve_part1(data)
    # assert expected == actual


# def test_solve_part2():
#    data = None
#    expected = None
#    actual = solution.solve_part2(data)
#    assert expected == actual
