from aoc2020.util import get_input_as_int


def get_device_rating(entries):
    return max(entries) + 3


def solve_part1(adapters):
    adapters.sort()
    one_diffs = 0
    three_diffs = 1
    joltage = 0
    for rating in adapters:
        # print(f"rating: {rating} joltage: {joltage}")
        if rating == joltage:
            pass
        elif rating - 1 == joltage:
            one_diffs += 1
        elif rating - 2 == joltage:
            print("found a two-jump!")
            pass
        elif rating - 3 == joltage:
            three_diffs += 1
        else:
            raise Exception("How'd this happen?")
        joltage = rating
    return one_diffs * three_diffs


def collect_sets(entries):
    entries.append(0)
    entries.append(get_device_rating(entries))
    entries.sort()
    sets = []
    immediate_set = []
    for i, entry in enumerate(entries):
        try:
            if entry + 1 != entries[i + 1]:
                immediate_set.append(entry)
                sets.append(immediate_set)
                immediate_set = []
            else:
                immediate_set.append(entry)
        except IndexError:
            pass
    return sets


def solve_part2(entries):
    sets = collect_sets(entries)
    len3 = 0
    len4 = 0
    len5 = 0
    for s in sets:
        if len(s) == 3:
            len3 += 1
        if len(s) == 4:
            len4 += 1
        if len(s) == 5:
            len5 += 1
        if len(s) > 5:
            raise Exception(f"How'd that happen? {s}")
    return 7 ** len5 * 4 ** len4 * 2 ** len3


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2020/day10/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
