def get_input(f):
    return [line.rstrip() for line in open(f)]


def get_input_as_int(f):
    input = get_input(f)
    return [int(i) for i in input]


def get_input_day04(f):
    """ day04 has empty lines separating input records """
    input = open(f).read()
    input = input.split("\n\n")
    return [line.replace("\n", " ") for line in input]


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
