from aoc2020.day11 import solution
from aoc2020.util import get_input


input_data = get_input("tests/testinput.day11")


def test_solve_part1():
    expected = 37
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_count_adjacent_occupied():
    input_data = get_input("tests/testinput.day11.2")
    expected = 8
    actual = solution.count_adjacent_occupied(input_data, 4, 3)
    assert expected == actual


def test_count_adjacent_occupied_2():
    input_data = get_input("tests/testinput.day11.3")
    expected = 0
    actual = solution.count_adjacent_occupied(input_data, 3, 3)
    assert expected == actual


# def test_solve_part2():
#    expected = 26
#    actual = solution.solve_part2(input_data)
#    assert expected == actual
