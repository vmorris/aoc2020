from aoc2020 import util

entries = util.get_input("day2.input")


def parse_entry(entry):
    policy, password = entry.split(":")
    ab, char = policy.split(" ")
    a, b = ab.split("-")
    return (int(a), int(b), char, password)


valid = 0
for entry in entries:
    a, b, char, password = parse_entry(entry)
    counter = password.count(char)
    if a <= counter <= b:
        valid += 1
print(valid)

valid = 0
for entry in entries:
    a, b, char, password = parse_entry(entry)
    if password[a] == password[b]:
        continue
    if char in (password[a], password[b]):
        valid += 1
print(valid)
