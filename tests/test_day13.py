from aoc2020.day13 import solution
from aoc2020.util import get_input_day13

input_data = get_input_day13("tests/testinput.day13")


def test_solve_part1():
    expected = 295
    actual = solution.solve_part1(input_data[0], input_data[1])
    assert expected == actual


def test_solve_part2():
    expected = 1068781
    actual = solution.solve_part2(0, input_data[1])
    assert expected == actual
