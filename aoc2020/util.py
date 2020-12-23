def get_input(f):
    return [line.rstrip() for line in open(f)]


def get_input_nlnl_records(f):
    """ Return list of lists, split on newlines """
    data = open(f).read()
    groups = data.rstrip().split("\n\n")
    return [line.rstrip().split("\n") for line in groups]


def get_input_as_int(f):
    input = get_input(f)
    return [int(i) for i in input]


def get_input_day04(f):
    """ day04 has empty lines separating input records """
    input = open(f).read()
    input = input.split("\n\n")
    return [line.replace("\n", " ") for line in input]


def get_input_day13(f):
    result = []
    input = open(f).read()
    input = input.split("\n")
    result.append(input[0])
    result.append(input[1].split(","))
    return result


def get_input_day16(f):
    input = open(f).read()
    validators, ticket, other_tickets = input.split("\n\n")
    validators = validators.split("\n")
    _validators = dict()
    for validator in validators:
        name, ranges = validator.split(": ")
        range1, range2 = ranges.split(" or ")
        _validators[name] = (range1, range2)
    ticket = ticket.split(":")[1].strip().split(",")
    other_tickets = other_tickets.split("\n")[1:]
    _other_tickets = list()
    for _other in other_tickets:
        _other_tickets.append(_other.split(","))
    return (_validators, ticket, _other_tickets)


def binary_search(data, instructions, control):
    """ day05 has a few binary search problems where the
    search direction is a specific control character.
    - `data` is a list to search
    - `instructions` is a string with control characters
    - `control` is two characters,
        indicating which direction to subdivide to continue the search
    """
    if len(control) != 2:
        raise ValueError("Invalid control set")
    if len(instructions) > 0 and not any(item in instructions for item in control):
        raise ValueError("Instruction not in control set")
    half = int(len(data) / 2)
    if len(data) == 1:
        return data[0]
    if instructions[0] == control[0]:
        # first half
        return binary_search(data[:half], instructions[1:], control)
    elif instructions[0] == control[1]:
        # last half
        return binary_search(data[half:], instructions[1:], control)


def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError(f"{x} is not in the list.")
