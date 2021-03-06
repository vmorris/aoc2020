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


def test_get_input_day04():
    expected = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
        "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
        "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in",
    ]
    actual = util.get_input_day04("tests/testinput.day04")
    assert actual == expected


def test_binary_search():
    data = list(range(128))
    expected = 44
    actual = util.binary_search(data, "FBFBBFF", "FB")
    assert actual == expected
    data = list(range(8))
    expected = 4
    actual = util.binary_search(data, "RLL", "LR")
    assert actual == expected


def test_get_input_nlnl_records():
    expected = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
    actual = util.get_input_nlnl_records("tests/testinput.day06")
    assert actual == expected


def test_get_input_day13():
    expected = ["939", ["7", "13", "x", "x", "59", "x", "31", "19"]]
    actual = util.get_input_day13("tests/testinput.day13")
    assert actual == expected


def test_get_input_day16():
    expected_validators = {
        "class": ("1-3", "5-7"),
        "row": ("6-11", "33-44"),
        "seat": ("13-40", "45-50"),
    }
    expected_ticket = ["7", "1", "14"]
    expected_other_tickets = [
        ["7", "3", "47"],
        ["40", "4", "50"],
        ["55", "2", "20"],
        ["38", "6", "12"],
    ]
    validators, ticket, other_tickets = util.get_input_day16("tests/testinput.day16")
    assert validators == expected_validators
    assert ticket == expected_ticket
    assert other_tickets == expected_other_tickets

