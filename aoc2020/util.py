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
