from aoc2020.day05 import solution
from aoc2020.util import get_input


# input_data = get_input("tests/testinput.day05")
input_data = "FBFBBFFRLR"


def test_decode_location():
    expected = 70
    actual = solution.decode_location("BFFFBBF", "FB")
    assert actual == expected


def test_get_row():
    expected = 44
    actual = solution.get_row(input_data)
    assert actual == expected


def test_get_column():
    expected = 5
    actual = solution.get_column(input_data)
    assert actual == expected


def test_get_seat():
    expected = 357
    actual = solution.get_seat(input_data)
    assert actual == expected


# def test_solve_part1():
# expected = None
# actual = solution.solve_part1(input_data)
# assert expected == actual


# def test_solve_part2():
# expected = None
# actual = solution.solve_part2(input_data)
# assert expected == actual
