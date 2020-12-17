from pprint import pprint

from aoc2020.util import get_input


def int2binstr(value):
    return f"{int(value):036b}"


def apply_mask_part1(value, mask):
    value = int2binstr(value)
    for i, _ in enumerate(value):
        if mask[i] != value[i] and mask[i] != "X":
            value = value[:i] + mask[i] + value[i + 1 :]
    return int(value, 2)


def solve_part1(entries):
    addresses = dict()
    for entry in entries:
        operation, operand = (e.strip() for e in entry.split("="))
        if operation == "mask":
            mask = operand
        elif operation.startswith("mem"):
            address = int(operation.split("[")[1].split("]")[0])
            value = operand
            addresses[address] = apply_mask_part1(value, mask)
    return sum(addresses.values())


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def set_str_char(s, index, char):
    return s[:index] + char + s[index + 1 :]


def apply_mask_part2(address, mask):
    addresses = list()
    num_X = mask.count("X")
    address = int2binstr(address)
    for i in range(2 ** num_X):
        addresses.append(address)
    indexes = [(index, char) for index, char in enumerate(mask) if char == "X"]
    indexes = list(reversed(indexes))
    pprint(indexes)
    step = 0
    while step < num_X:
        groups = list(chunks(addresses, 2 ** step))
        zero = 0
        for i, group in enumerate(groups):
            print(
                f"{zero}; i:{i}; indexes[step][0]:{indexes[step][0]}; len(group):{len(group)}"
            )
        step += 1

    for i, _ in enumerate(address):
        if mask[i] == "1":
            address = set_str_char(address, i, "1")


def solve_part2(entries):
    addresses = dict()
    for entry in entries:
        operation, operand = (e.strip() for e in entry.split("="))
        if operation == "mask":
            mask = operand
        elif operation.startswith("mem"):
            address = operation.split("[")[1].split("]")[0]
            value = operand
            to_write = apply_mask_part2(address, mask)
    return


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2020/day14/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
