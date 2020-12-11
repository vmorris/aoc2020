from aoc2020.day10 import solution
from aoc2020.util import get_input_as_int


input_data = get_input_as_int("tests/testinput.day10")
input_data2 = get_input_as_int("tests/testinput.day10.2")


def test_get_device_rating():
    expected = 22
    actual = solution.get_device_rating(input_data)
    assert expected == actual


def test_solve_part1():
    expected = 35
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part1_2():
    expected = 220
    actual = solution.solve_part1(input_data2)
    assert expected == actual


def test_solve_part2():
    expected = 8
    actual = solution.solve_part2(input_data)
    assert expected == actual


def test_solve_part2_2():
    expected = 19208
    actual = solution.solve_part2(input_data2)
    assert expected == actual
