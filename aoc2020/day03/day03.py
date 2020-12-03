from aoc2020.util import get_input


def traverse(p, s, w):
    x, y = p
    _x, _y = s
    return ((x + _x) % w, (y + _y))


def slide_down(slope, forest):
    width = len(forest[0])
    height = len(forest)
    trees_hit = 0
    position = (0, 0)
    while position[1] < height - 1:
        position = traverse(position, slope, width)
        if forest[position[1]][position[0]] == "#":
            trees_hit += 1
    return trees_hit


def solve_part1(forest):
    return slide_down((3, 1), forest)


def solve_part2(forest):
    hit = slide_down((1, 1), forest)
    hit *= slide_down((3, 1), forest)
    hit *= slide_down((5, 1), forest)
    hit *= slide_down((7, 1), forest)
    hit *= slide_down((1, 2), forest)
    return hit


if __name__ == "__main__":
    array = get_input("aoc2020/day03/day03.input")
    print(solve_part1(array))
    print(solve_part2(array))

