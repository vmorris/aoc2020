from aoc2020.day14 import solution
from aoc2020.util import get_input


input_data = get_input("tests/testinput.day14")
input_data_2 = get_input("tests/testinput.day14.2")


def test_int2binstr():
    value = 64
    expected = "000000000000000000000000000001000000"
    actual = solution.int2binstr(value)
    assert expected == actual


def test_apply_mask_part1():
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    value = 11
    expected = 73
    actual = solution.apply_mask_part1(value, mask)
    assert expected == actual


def test_solve_part1():
    expected = 165
    actual = solution.solve_part1(input_data)
    assert expected == actual


# def test_solve_part2():
#    expected = 208
#    actual = solution.solve_part2(input_data_2)
#    assert expected == actual
