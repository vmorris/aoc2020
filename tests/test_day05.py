from aoc2020.day05 import solution


input_data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
expected = [
    {"row": 44, "col": 5, "seat": 357},
    {"row": 70, "col": 7, "seat": 567},
    {"row": 14, "col": 7, "seat": 119},
    {"row": 102, "col": 4, "seat": 820},
]


def test_get_row():
    for i, data in enumerate(input_data):
        actual = solution.get_row(data)
        assert actual == expected[i].get("row")


def test_get_column():
    for i, data in enumerate(input_data):
        actual = solution.get_column(data)
        assert actual == expected[i].get("col")


def test_get_seat():
    for i, data in enumerate(input_data):
        actual = solution.get_seat(data)
        assert actual == expected[i].get("seat")


def test_solve_part1():
    expected = 820
    actual = solution.solve_part1(input_data)
    assert actual == expected


def test_get_max_seat():
    expected = 1023
    actual = solution.get_max_seat(7, 3)
    assert actual == expected


def test_get_lowest_seat():
    expected = 119
    actual = solution.get_lowest_seat(input_data)
    assert actual == expected


# def test_solve_part2():
# expected = None
# actual = solution.solve_part2(input_data)
# assert expected == actual
