from aoc2020.day03 import day03
from aoc2020.util import get_input


input_data = get_input("tests/testinput.day03")


def test_traverse():
    w = 3
    p = (0, 0)
    s = (1, 2)
    expected = (1, 2)
    actual = day03.traverse(p, s, w)
    assert expected == actual

    p = (2, 3)
    s = (2, 3)
    expected = (1, 6)
    actual = day03.traverse(p, s, w)
    assert expected == actual


def test_solve_part1():
    expected = 7
    actual = day03.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 336
    actual = day03.solve_part2(input_data)
    assert expected == actual
