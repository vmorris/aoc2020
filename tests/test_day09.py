from aoc2020.day09 import solution
from aoc2020.util import get_input_as_int


input_data = get_input_as_int("tests/testinput.day09")


def test_solve_part1():
    expected = 127
    preamble_length = 5
    actual = solution.solve_part1(input_data, preamble_length)
    assert expected == actual


def test_solve_part2():
    expected = 62
    actual = solution.solve_part2(input_data, 127)
    assert expected == actual
