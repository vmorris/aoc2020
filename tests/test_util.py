from aoc2020 import util


input_file = "tests/testinput.util"


def test_get_input():
    expected = ["1", "2", "3", "4"]
    actual = util.get_input(input_file)
    assert actual == expected


def test_get_input_as_int():
    expected = [1, 2, 3, 4]
    actual = util.get_input_as_int(input_file)
    assert actual == expected
