from aoc2020.day12 import solution
from aoc2020.util import get_input


input_data = get_input("tests/testinput.day12")


def test_solve_part1():
    expected = 25
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = None
    actual = solution.solve_part2(input_data)
    assert expected == actual
