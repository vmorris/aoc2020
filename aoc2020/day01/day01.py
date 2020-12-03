from functools import reduce
from itertools import combinations
from operator import mul

from aoc2020.util import get_input_as_int


def solve_part1(e):
    return [reduce(mul, comb) for comb in combinations(e, 2) if sum(comb) == 2020][0]


def solve_part2(e):
    return [reduce(mul, comb) for comb in combinations(e, 3) if sum(comb) == 2020][0]


if __name__ == "__main__":  # pragma: no cover
    entries = get_input_as_int("aoc2020/day01/day01.input")
    print(solve_part1(entries))
    print(solve_part2(entries))
