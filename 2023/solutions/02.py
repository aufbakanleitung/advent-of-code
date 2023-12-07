# --- Day 2: Cube Conundrum ---
import re
from pprint import pprint

lines = [items.strip() for items in open('../input/02.txt').read().splitlines()]
lines = [re.split(':|,|;', line) for line in lines]
max_color = {"red": 12, "green": 13, "blue": 14}

def part_1(lines, max_color):
    tot = 0
    for i, line in enumerate(lines):
        for item in line[1:]:
            n, c = item.split()
            if int(n) > max_color[c]:
                tot -= i+1
                break
        tot += i+1
    return tot
# print(part_1(lines, max_color))

def part_2(lines):
    tot = 0
    for i, line in enumerate(lines):
        min_color = {"red": 0,"green": 0,"blue": 0}
        for item in line[1:]:
            n, color = item.split()
            if int(n) > min_color[color]:
                min_color[color] = int(n)
        tot += min_color['red'] * min_color['green'] * min_color['blue']
    return tot

print(part_2(lines))