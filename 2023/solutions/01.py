# --- Day 1: Trebuchet?! ---
import curses.ascii
import re

lines = [items for items in open('../input/01e2.txt').read().splitlines()]

def part_1(lines):
    tot = 0
    for line in lines:
        nr_lines = re.findall(r'\d+', line)
        tot += (int(str(nr_lines[0][0]) + str(nr_lines[-1][-1])))
    print(tot)

# --- part 2 ---

def part_2(lines):
    total = 0

    n = "one two three four five six seven eight nine".split()
    pattern = "\\d|" + "|".join(n)
    print(n)
    print(pattern)

    m = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for line in lines:
        f = re.search(pattern, line).group()
        print(f)
        l = re.search(".*(" + pattern + ")", line).group(1)
        print(l)
        total += int(m.get(f, f) + m.get(l, l))

    print(total)
part_2(lines)