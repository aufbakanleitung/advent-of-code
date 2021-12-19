# --- Day 11: Dumbo Octopus ---
from pprint import pp
lines = open('../input/11_example.txt').read().splitlines()
lines = [list(map(int, line)) for line in lines]
y_size, x_size = len(lines), len(lines[0])
pp(lines)

flash = 0

def add_adjacent(y,x):
    adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for yi,xi in adj:
        if 0 <= x+xi < x_size and 0 <= y+yi < y_size:
            lines[y+yi][x+xi] += 1


def next(lines):
    global flash
    reset = set()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            lines[y][x] += 1

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] > 9:
                add_adjacent(y,x)
    print('before reset')
    # pp(lines)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] > 9:
                flash += 1
                # reset.add((y,x))
                lines[y][x] = 0

    # for y,x in reset:
    #     lines[y][x] = 0
    return lines

def string_print(grid):
    for line in grid:
        print(''.join(str(x) for x in line))
    print()


for i in range(1,4):
    print('step:', i)
    string_print(next(lines))
    print(f"{flash} flashes\n")




# How many total flashes are there after 100 steps?

