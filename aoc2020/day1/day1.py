from functools import reduce
from itertools import combinations
from operator import mul

entries = [int(line) for line in open("day1.input")]


def solve(i):
    print([reduce(mul, comb) for comb in combinations(entries, i) if sum(comb) == 2020])


solve(2)
solve(3)
