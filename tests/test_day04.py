from aoc2020.day04 import solution
from aoc2020.util import get_input_day04


input_data = get_input_day04("tests/testinput.day04")


def test_solve_part1():
    expected = 2
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 2
    actual = solution.solve_part2(input_data)
    assert expected == actual


def test_valid_byr():
    assert solution.valid_byr("1920")
    assert solution.valid_byr("2002")
    assert not solution.valid_byr("1919")
    assert not solution.valid_byr("2003")
    assert not solution.valid_byr(None)


def test_valid_iyr():
    assert solution.valid_iyr("2010")
    assert solution.valid_iyr("2020")
    assert not solution.valid_iyr("2009")
    assert not solution.valid_iyr("2021")
    assert not solution.valid_iyr(None)


def test_valid_eyr():
    assert solution.valid_eyr("2020")
    assert solution.valid_eyr("2030")
    assert not solution.valid_eyr("2019")
    assert not solution.valid_eyr("2031")
    assert not solution.valid_eyr(None)


def test_valid_hgt():
    assert solution.valid_hgt("150cm")
    assert solution.valid_hgt("193cm")
    assert not solution.valid_hgt("149cm")
    assert not solution.valid_hgt("194cm")
    assert solution.valid_hgt("59in")
    assert solution.valid_hgt("76in")
    assert not solution.valid_hgt("58in")
    assert not solution.valid_hgt("77in")
    assert not solution.valid_hgt("150vm")
    assert not solution.valid_hgt(None)


def test_valid_hcl():
    assert solution.valid_hcl("#123456")
    assert not solution.valid_hcl("#1234567")
    assert not solution.valid_hcl("#12345")
    assert not solution.valid_hcl("123456")
    assert not solution.valid_hcl("#ZZZZZZ")
    assert not solution.valid_hcl(None)


def test_valid_ecl():
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for v in valid:
        assert solution.valid_ecl(v)
    assert not solution.valid_ecl("")
    assert not solution.valid_ecl(None)
    assert not solution.valid_ecl("ass")


def test_valid_pid():
    assert solution.valid_pid("123456789")
    assert not solution.valid_pid("12345678")
    assert not solution.valid_pid("1234567890")
    assert not solution.valid_pid(None)


def test_valid_cid():
    assert solution.valid_cid(None)
