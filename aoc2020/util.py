def get_input(f):
    return [line.rstrip() for line in open(f)]


def get_input_as_int(f):
    input = get_input(f)
    return [int(i) for i in input]
