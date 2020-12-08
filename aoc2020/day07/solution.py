import itertools

from anytree import Node, RenderTree
from anytree.iterators.preorderiter import PreOrderIter

from aoc2020.util import get_input


def collect_bags(entries):
    bags = dict()
    for entry in entries:
        bag, contains = entry.split(" bags contain ")
        contains = [bag.split("bag")[0].strip() for bag in contains.split(",")]
        if contains == ["no other"]:
            contains = None
        bags[bag] = contains
    return bags


def find_bags_that_contain(bag_to_find, all_bags):
    result = list()
    for _bag, contains in all_bags.items():
        if contains:
            for c in contains:
                if bag_to_find in c:
                    result.append(_bag)
    return result


def build_part1_tree(node, all_bags):
    children = find_bags_that_contain(node.name, all_bags)
    if children is None:
        return
    for child in children:
        build_part1_tree(Node(child, parent=node), all_bags)


def build_part2_tree(node, all_bags):
    children = all_bags[node.name]
    if children is None:
        return
    for child in children:
        count, name = child.split(" ", 1)
        build_part2_tree(Node(name, parent=node, count=int(count)), all_bags)


def solve_part1(entries):
    all_bags = collect_bags(entries)
    shiny_gold_tree = Node("shiny gold")
    build_part1_tree(shiny_gold_tree, all_bags)
    # collect all the nodes
    collected = [node.name for node in PreOrderIter(shiny_gold_tree)]
    # convert to set to remove duplicates
    dedup = set(collected)
    dedup.remove("shiny gold")
    return len(dedup)


def solve_part2(entries):
    all_bags = collect_bags(entries)
    shiny_gold_tree = Node("shiny gold")
    build_part2_tree(shiny_gold_tree, all_bags)
    print(RenderTree(shiny_gold_tree))
    return 2


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2020/day07/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
