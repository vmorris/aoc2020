from operator import add

from aoc2020.util import get_input


def traverse(p, s, w):
    """ add the slope to the position and mod to the width """
    x, y = list(map(add, p, s))
    return (x % w, y)


def slide_down(slope, forest):
    """ move down the hill and count the number of trees hit """
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


if __name__ == "__main__":  # pragma: no cover
    array = get_input("aoc2020/day03/day03.input")
    print(solve_part1(array))
    print(solve_part2(array))

