from aoc2020.util import get_input_day16

from collections import defaultdict
import copy


def valid_value(validator, value):
    for _range in validator:
        _range = [int(r) for r in _range.split("-")]
        if _range[0] <= int(value) <= _range[1]:
            return True
    return False


def validate_ticket(validators, ticket):
    valid = [False] * len(ticket)
    for index, value in enumerate(ticket):
        for name, validator in validators.items():
            if valid_value(validator, value):
                valid[index] = True
    if all(valid):
        return True
    else:
        for index, v in enumerate(valid):
            if not v:
                return int(ticket[index])


def solve_part1(validators, my_ticket, other_tickets):
    invalid_count = 0
    for ticket in other_tickets:
        valid = validate_ticket(validators, ticket)
        if valid != True:
            invalid_count += valid
    return invalid_count


def solve_part2(validators, my_ticket, other_tickets):
    valid_tickets = list()
    for ticket in other_tickets:
        if validate_ticket(validators, ticket) == True:
            valid_tickets.append(ticket)
    result = defaultdict(list)
    for name, validator in validators.items():
        for index in range(len(my_ticket)):
            index_valid = True
            for ticket in valid_tickets:
                if not valid_value(validator, ticket[index]):
                    index_valid = False
            if index_valid:
                result[name].append(index)
    final = dict()
    while True:
        result_copy = copy.deepcopy(result)
        print(f"deep copy for loop1: {result_copy}")
        print(f"searching for single length values..")
        values_to_clean = list()
        for k, v in result_copy.items():
            if len(v) == 1:
                print(f"\tfound! {k}: {v[0]}")
                final[k] = v[0]
                values_to_clean.append(v[0])
                del result[k]
        if len(result) == 0:
            print("we're all done now")
            break
        result_copy = copy.deepcopy(result)
        print(f"deep copy for loop2: {result_copy}")
        print(f"- to purge: {values_to_clean}")
        for key in result_copy:
            for value in values_to_clean:
                print(f"\t- purging {value}")
                if value in result[key]:
                    print(f"\t\t- found {value} in {key}")
                    result[key].remove(value)
                    print(f"\t\t- result[{key}] == {result[key]}")
    result = 1
    for k, v in final.items():
        if k.startswith("departure"):
            result *= int(my_ticket[v])
            print(f"{k}: {v}: {my_ticket[v]}")
    return result
    # guess: 1483199335103 = too high


if __name__ == "__main__":  # pragma: no cover
    validators, ticket, other_tickets = get_input_day16("aoc2020/day16/input")
    print(solve_part1(validators, ticket, other_tickets))
    print(solve_part2(validators, ticket, other_tickets))
