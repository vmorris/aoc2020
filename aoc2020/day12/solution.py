from aoc2020.util import get_input


compass = {0: "N", 90: "E", 180: "S", 270: "W"}


class Ship:
    def __init__(self):
        self.degree = 90
        self.direction = "E"
        self.x = 0
        self.y = 0

    def forward(self, distance):
        self.translate(self.direction, distance)

    def translate(self, direction, distance):
        if direction == "N":
            self.y += distance
        elif direction == "E":
            self.x += distance
        elif direction == "S":
            self.y -= distance
        elif direction == "W":
            self.x -= distance

    def rotate(self, degrees):
        self.degree += degrees
        self.degree %= 360
        self.direction = compass[self.degree]


def solve_part1(entries):
    ship = Ship()
    for instruction in entries:
        operation = instruction[0]
        operand = int(instruction[1:])
        if operation == "F":
            ship.forward(operand)
        elif operation == "R":
            ship.rotate(operand)
        elif operation == "L":
            ship.rotate(-operand)
        else:
            ship.translate(operation, operand)
    return abs(ship.x) + abs(ship.y)


def solve_part2(entries):
    return


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2020/day12/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
