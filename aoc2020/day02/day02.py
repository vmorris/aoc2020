from aoc2020.util import get_input


def parse_entry(entry):
    policy, password = entry.split(":")
    ab, char = policy.split(" ")
    a, b = ab.split("-")
    return (int(a), int(b), char, password)


def solve_part1(entries):
    valid = 0
    for entry in entries:
        a, b, char, password = parse_entry(entry)
        counter = password.count(char)
        if a <= counter <= b:
            valid += 1
    return valid


def solve_part2(entries):
    valid = 0
    for entry in entries:
        a, b, char, password = parse_entry(entry)
        if password[a] == password[b]:
            continue
        if char in (password[a], password[b]):
            valid += 1
    return valid


if __name__ == "__main__":
    entries = get_input("aoc2020/day02/day02.input")
    print(solve_part1(entries))
    print(solve_part2(entries))

