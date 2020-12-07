from aoc2020.day06 import solution
from aoc2020.util import get_input_nlnl_records


input_data = get_input_nlnl_records("tests/testinput.day06")


def test_solve_part1():
    expected = 11
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 6
    actual = solution.solve_part2(input_data)
    assert expected == actual
