from aoc2020.util import get_input

import copy


class Floor:
    def __init__(self, kind):
        if kind != ".":
            self.seat = True
            if kind == "L":
                self.occupied = False
            elif kind == "#":
                self.occupied = True
        else:
            self.seat = False
            self.occupied = False

    def occupy(self, occupy):
        if self.seat and occupy:
            self.occupied = True
        else:
            self.occupied = False

    def __repr__(self):
        if self.seat and self.occupied:
            return "#"
        elif self.seat and not self.occupied:
            return "L"
        else:
            return "."

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return str(self) == str(other)


class Ferry:
    def __init__(self, seats):
        self.seats = self._create_floor(seats)
        self.num_rows = len(seats)
        self.num_cols = len(seats[0])
        self.mutations = 0

    def _create_floor(self, seats):
        _seats = list()
        _row = list()
        for row in seats:
            _col = list()
            for col in row:
                _col.append(Floor(col))
            _seats.append(_col)
        return _seats

    def get_seat(self, row, col):
        try:
            return self.seats[row][col]
        except IndexError:
            return None

    def count_adjacent_occupied(self, row, col):
        count = 0
        prev_row = row - 1
        next_row = row + 1
        prev_col = col - 1
        next_col = col + 1
        if prev_row >= 0 and prev_col >= 0:
            seat = self.get_seat(prev_row, prev_col)
            if seat and seat.occupied:
                count += 1
        if prev_row >= 0:
            seat = self.get_seat(prev_row, col)
            if seat and seat.occupied:
                count += 1
        if prev_row >= 0:
            seat = self.get_seat(prev_row, next_col)
            if seat and seat.occupied:
                count += 1
        if prev_col >= 0:
            seat = self.get_seat(row, prev_col)
            if seat and seat.occupied:
                count += 1
        seat = self.get_seat(row, next_col)
        if seat and seat.occupied:
            count += 1
        if prev_col >= 0:
            seat = self.get_seat(next_row, prev_col)
            if seat and seat.occupied:
                count += 1
        seat = self.get_seat(next_row, col)
        if seat and seat.occupied:
            count += 1
        seat = self.get_seat(next_row, next_col)
        if seat and seat.occupied:
            count += 1
        return count

    def mutate(self):
        new_seats = copy.deepcopy(self.seats)
        for i, row in enumerate(self.seats):
            for j, seat in enumerate(row):
                num_adj_occupied = self.count_adjacent_occupied(i, j)
                if seat and not seat.occupied and num_adj_occupied == 0:
                    new_seats[i][j].occupy(True)
                elif seat and seat.occupied and num_adj_occupied >= 4:
                    new_seats[i][j].occupy(False)
        self.mutations += 1
        if self.compare(new_seats):
            return 0
        else:
            self.seats = new_seats
            return self.mutations

    def compare(self, other):
        next_ferry = Ferry(other)
        for i, row in enumerate(self.seats):
            for j, seat in enumerate(row):
                if seat != next_ferry.get_seat(i, j):
                    return False
        return True

    def count_occupied_seats(self):
        count = 0
        for row in self.seats:
            for seat in row:
                if seat.occupied:
                    count += 1
        return count

    def __repr__(self):
        result = ""
        for row in self.seats:
            for seat in row:
                result += f"{seat}"
            result += "\n"
        return result


def solve_part1(entries):
    ferry = Ferry(entries)
    mutations = ferry.mutate()
    while mutations != 0:
        mutations = ferry.mutate()
    return ferry.count_occupied_seats()


def next_seat_east(seats, row, col):
    if seats[row][col] == ".":
        return None
    for seat in seats[row][col + 1 :]:
        if seat != ".":
            return seat


def next_seat_west(seats, row, col):
    if seats[row][col] == ".":
        return None
    for _col in reversed(range(col)):
        try:
            if seats[row][_col] != ".":
                return seats[row][_col]
        except IndexError:
            return None


def next_seat_south(seats, row, col):
    if seats[row][col] == ".":
        return None
    for _row in range(row + 1, len(seats)):
        if seats[_row][col] != ".":
            return seats[_row][col]


def next_seat_north(seats, row, col):
    if seats[row][col] == ".":
        return None
    for _row in reversed(range(row)):
        if seats[_row][col] != ".":
            return seats[_row][col]


def next_seat_southeast(seats, row, col):
    if seats[row][col] == ".":
        return None
    _col = col + 1
    for _row in range(row + 1, len(seats)):
        try:
            if seats[_row][_col] != ".":
                return seats[_row][_col]
        except IndexError:
            return None
        _col += 1


def next_seat_southwest(seats, row, col):
    if seats[row][col] == ".":
        return None
    _col = col - 1
    for _row in range(row + 1, len(seats)):
        try:
            if seats[_row][_col] != ".":
                return seats[_row][_col]
        except IndexError:
            return None
        _col -= 1


def next_seat_northeast(seats, row, col):
    if seats[row][col] == ".":
        return None
    _col = col + 1
    for _row in reversed(range(row)):
        try:
            if seats[_row][_col] != ".":
                return seats[_row][_col]
        except IndexError:
            return None
        _col += 1


def next_seat_northwest(seats, row, col):
    if seats[row][col] == ".":
        return None
    _col = col - 1
    for _row in reversed(range(row)):
        try:
            if seats[_row][_col] != ".":
                return seats[_row][_col]
        except IndexError:
            return None
        _col -= 1


def count_adjacent_occupied(seats, row, col):
    if seats[row][col] == ".":
        return None
    result = 0
    if next_seat_north(seats, row, col) == "#":
        # print("north")
        result += 1
    if next_seat_south(seats, row, col) == "#":
        # print("south")
        result += 1
    if next_seat_east(seats, row, col) == "#":
        # print("east")
        result += 1
    if next_seat_west(seats, row, col) == "#":
        # print("west")
        result += 1
    if next_seat_northeast(seats, row, col) == "#":
        # print("northeast")
        result += 1
    if next_seat_southeast(seats, row, col) == "#":
        # print("southeast")
        result += 1
    if next_seat_southwest(seats, row, col) == "#":
        # print("southwest")
        result += 1
    if next_seat_northwest(seats, row, col) == "#":
        # print("northwest")
        result += 1
    return result


def shift_seats(seats):
    new_seats = copy.copy(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            # if i == 0 and j == 0:
            # import pdb

            # pdb.set_trace()
            if seat == "#":  # occupied
                if count_adjacent_occupied(seats, i, j) >= 5:
                    new_seats[i] = (
                        new_seats[i][:j] + "L" + new_seats[i][j + 1 :]
                    )  # set unoccupied
            elif seat == "L":  # unoccupied
                if count_adjacent_occupied(seats, i, j) == 0:
                    new_seats[i] = (
                        new_seats[i][:j] + "#" + new_seats[i][j + 1 :]
                    )  # set occupied
    return new_seats


def seats_equal(old, new):
    for i, row in enumerate(old):
        for j, seat in enumerate(row):
            if old[i][j] != new[i][j]:
                return False
    return True


def count_total_occupied_seats(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                count += 1
    return count


def solve_part2(seats):
    num_rows = len(seats)
    num_cols = len(seats[0])
    new_seats = shift_seats(seats)
    while not seats_equal(seats, new_seats):
        print(seats)
        seats = new_seats
        new_seats = shift_seats(seats)
    print(seats)
    return count_total_occupied_seats(seats)


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2020/day11/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
