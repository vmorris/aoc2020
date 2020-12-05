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
