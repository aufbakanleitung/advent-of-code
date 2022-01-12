# --- Day 11: Dumbo Octopus ---
from pprint import pp
lines = open('../input/11_input.txt').read().splitlines()
lines = [list(map(int, line)) for line in lines]
y_size, x_size = len(lines), len(lines[0])
pp(lines)


# This doesn't work, flashes don't propagate upwards.
# I'll leave it here as a warning for future generations
def add_adjacent(y,x):
    adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for yi,xi in adj:
        if 0 <= x+xi < x_size and 0 <= y+yi < y_size:
            lines[y+yi][x+xi] += 1

flash = 0
def recursive_add(lines, y, x):
    global flash
    flash += 1
    for ly in (y-1, y, y+1):
        for lx in (x-1, x, x+1):
            if ly == y and lx == x: continue
            if 0 <= ly < y_size and 0 <= lx < x_size:
                lines[ly][lx] += 1
                if lines[ly][lx] == 10:
                    recursive_add(lines, ly, lx)
                    lines[ly][lx] += 1


def next(lines):
    global flash
    for y in range(y_size):
        for x in range(x_size):
            lines[y][x] += 1
            if lines[y][x] == 10:
                recursive_add(lines, y, x)
                lines[y][x] += 1

    for y in range(y_size):
        for x in range(x_size):
            if lines[y][x] > 9:
                lines[y][x] = 0

    return lines


def string_print(grid, spacer=''):
    for line in grid:
        print(spacer.join(str(x) for x in line))
    print()


def run():
    for i in range(1,500):
        print('step', i)
        previous_flash = flash
        string_print(next(lines))
        print(f"{flash} flashes\n")
        if flash - previous_flash == y_size * x_size:
            print(f"Simultaneous flash!")
            break
run()