# --- Day 7: Handy Haversacks ---
import re

content = [line.rstrip('\n') for line in open("input/aoc07_input.txt")]
bags = [re.findall(r'\w+\s\w+(?=\s+bag)', line) for line in content]


def check_bag(color):
    contain_color = set()
    for bag in bags:
        if color in bag[1:]:
            contain_color.add(bag[0])
    return contain_color


def find_bags(color):
    for sub_bag in check_bag(color):
        found_bags.add(sub_bag)
        if sub_bag in check_bag(color):
            find_bags(sub_bag)  # recursion


# How many bag colors can eventually contain at least one shiny gold bag?
found_bags = set()
find_bags("shiny gold")
print(found_bags)
print(len(found_bags))