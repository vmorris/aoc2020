from aoc2020.dayCHANGEME import solution
from aoc2020.util import get_input_as_int


input_data = get_input_as_int("tests/testinput.dayCHANGEME")


def test_solve_part1():
    expected = None
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = None
    actual = solution.solve_part2(input_data)
    assert expected == actual
