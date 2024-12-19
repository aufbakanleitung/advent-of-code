# --- Day 7b: Handy Haversacks ---
import re

content = [line.rstrip('\n') for line in open("input/aoc07_input.txt")]
bags = [re.findall(r'(\d+)*\s*(\w+\s\w+)(?=\sbag)', line) for line in content]

# Create dict of dicts
bags_dict = {}
for bag in bags:
    bags_dict[bag[0][1]] = {}
    for sub_bag in bag[1:]:
        if sub_bag[1] != 'no other':
            bags_dict[bag[0][1]][sub_bag[1]] = int(sub_bag[0])

# Recursively sum the contents of the bag
def find_bags(color):
    teller = 0
    for bag in bags_dict[color]:
        teller += bags_dict[color][bag] + find_bags(bag) * bags_dict[color][bag]
    return teller

# How many individual bags are required inside your single shiny gold bag?
print("The shiny gold bag contains", find_bags("shiny gold"), "bags")