from aoc2020.day01 import day01
from aoc2020.util import get_input_as_int


input_data = get_input_as_int("tests/testinput.day01")


def test_solve_part1():
    expected = 514579
    actual = day01.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 241861950
    actual = day01.solve_part2(input_data)
    assert expected == actual
