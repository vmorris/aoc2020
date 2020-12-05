from aoc2020.util import get_input


def decode_location(data, mapping):
    """ We can simply map 0 and 1 to the characters in the location data
    and convert the binary to an integer to determine the value """
    trans = data.translate(str.maketrans(mapping, "01"))
    return int(trans, base=2)


def get_row(data):
    data = data[:7]
    return decode_location(data, "FB")


def get_column(data):
    data = data[7:]
    return decode_location(data, "LR")


def get_seat(data):
    return (get_row(data) * 8) + get_column(data)


def get_max_seat():
    return get_seat("BBBBBBBRRR")


def get_highest_seat(entries):
    highest = 0
    for entry in entries:
        seat = get_seat(entry)
        if seat > highest:
            highest = seat
    return highest


def get_lowest_seat(entries):
    lowest = get_max_seat()
    for entry in entries:
        seat = get_seat(entry)
        if seat < lowest:
            lowest = seat
    return lowest


def solve_part1(entries):
    return get_highest_seat(entries)


def solve_part2(entries):
    low = get_lowest_seat(entries)
    high = get_highest_seat(entries)
    seats_filled = [False for _ in range(get_max_seat())]
    for entry in entries:
        seats_filled[get_seat(entry)] = True
    for seat, filled in enumerate(seats_filled):
        if not filled and low <= seat <= high:
            return seat


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2020/day05/input")
    print(solve_part1(entries))
    print(solve_part2(entries))

