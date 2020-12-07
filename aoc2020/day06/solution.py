from aoc2020.util import get_input_nlnl_records


def intersection_answers(answers):
    isect = answers[0]
    for answer in answers:
        isect = set(isect).intersection(answer)
    return len(isect)


def union_answers(answers):
    union = answers[0]
    for answer in answers:
        union = set(union).union(answer)
    return len(union)


def solve_part1(entries):
    total = 0
    for entry in entries:
        total += union_answers(entry)
    return total


def solve_part2(entries):
    total = 0
    for entry in entries:
        total += intersection_answers(entry)
    return total


if __name__ == "__main__":  # pragma: no cover
    entries = get_input_nlnl_records("aoc2020/day06/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
