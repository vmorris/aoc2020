from functools import reduce
from itertools import combinations
from operator import add

from aoc2020.util import get_input_as_int


def find_first_invalid_number(numbers, preamble_length):
    preamble = numbers[:preamble_length]
    print(f"preamble length = {preamble_length}")
    print(f"preamble = {preamble}")
    i = preamble_length
    while i < len(numbers):
        to_check = numbers[i]
        sums = set(
            [
                reduce(add, comb)
                for comb in combinations(numbers[i - preamble_length : i], 2)
            ]
        )
        if to_check not in sums:
            return to_check
        i += 1
    return


def solve_part1(entries, preamble_length):
    result = find_first_invalid_number(entries, preamble_length)
    return result


def solve_part2(entries, invalid_number):
    start = 0
    while start < len(entries):
        end = 0
        while end < len(entries):
            to_check = entries[start:end]
            if invalid_number == sum(to_check):
                return min(to_check) + max(to_check)
            end += 1
        start += 1


if __name__ == "__main__":  # pragma: no cover
    entries = get_input_as_int("aoc2020/day09/input")
    invalid_number = solve_part1(entries, preamble_length=25)
    print(invalid_number)
    print(solve_part2(entries, invalid_number))
