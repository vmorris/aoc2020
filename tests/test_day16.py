from aoc2020.day16 import solution
from aoc2020.util import get_input_day16


def test_solve_part1():
    validators, ticket, other_tickets = get_input_day16("tests/testinput.day16")
    expected = 71
    actual = solution.solve_part1(validators, ticket, other_tickets)
    assert expected == actual


def test_solve_part2():
    validators, ticket, other_tickets = get_input_day16("tests/testinput.day16.2")
    expected = {"row": 11, "class": 12, "seat": 13}
    actual = solution.solve_part2(validators, ticket, other_tickets)
    # assert expected == actual
