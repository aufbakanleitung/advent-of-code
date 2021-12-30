# --- Day 25: Sea Cucumber ---
from copy import deepcopy

from helpers import timer

lines = list(map(list,open('../input/25_input.txt').read().splitlines()))
y_size, x_size = len(lines), len(lines[0])

def next(lines):
    new = deepcopy(lines)
    for y, line in enumerate(lines):
        for x, n in enumerate(line):
            if n == '>':
                if lines[y][(x+1) % x_size] == '.':
                    new[y][x] = '.'
                    new[y][(x+1) % x_size] = '>'
    new_2 = deepcopy(new)
    for y,line in enumerate(new):
        for x,n in enumerate(line):
            if n == 'v':
                if new[(y+1) % y_size][x] == '.':
                    new_2[y][x] = '.'
                    new_2[(y+1) % y_size][x] = 'v'

    return new_2


@timer
def run(lines):
    for n in range(1000):
        lines2 = next(lines)
        if lines == lines2:
            print(f"Stability achieved at step {n+1}:")
            break
        lines = lines2

run(lines)
