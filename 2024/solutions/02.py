# --- Day 2: Red-Nosed Reports ---
from pprint import pprint
import re

lines = [items.strip() for items in open('../input/02e.txt').read().splitlines()]
lines = [list(map(int, re.split(' ', line))) for line in lines]


def part_one(lines):
    count = 0
    for line in lines:
        delta = [x - y for x, y in zip(line, line[1:])]
        print(delta)
        if all(1 <= x <= 3 for x in delta) or all(-1 >= x >= -3 for x in delta):
            count += 1
    print(count)


# --- Part Two ---
def safe(levels):
    delta = [x - y for x, y in zip(levels, levels[1:])]
    return all(1 <= x <= 3 for x in delta) or all(-1 >= x >= -3 for x in delta)

count = 0
for line in lines:
    if any(safe(line[:index] + line[index + 1:]) for index in range(len(line))):
        count += 1



