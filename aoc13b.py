# --- Day 13: Transparent Origami ---
from pprint import pp

coor, folds = open('input/13_input.txt').read().split('\n\n')
folds = [line.split()[2] for line in folds.splitlines()]

dots = set()
for c in coor.splitlines():
    x, y = map(int, c.split(","))
    dots.add((x, y))


def fold_it(dots, fold):
    new_dots = dots.copy()
    fold_dir, line = fold.split('=')
    for dot in dots:
        dx,dy = dot
        if fold_dir == 'x':
            if dx > int(line):
                new_dots.add((dx-2 * (dx-int(line)), dy))
                new_dots.remove((dx,dy))
        if fold_dir == 'y':
            if dy > int(line):
                new_dots.add((dx,dy-2 * (dy-int(line))))
                new_dots.remove((dx,dy))
    return new_dots

for fold in folds:
    dots = fold_it(dots, fold)


def print_string(dots):
    x_max = max(dot[0] for dot in dots)
    y_max = max(dot[1] for dot in dots)
    grid = [['.'] * (x_max+1) for _ in range(y_max+1)]
    # print('gridsize:',x_max,y_max)

    for dot in dots:
        grid[dot[1]][dot[0]] = '#'
    # print(''.join(seats[60]))
    for line in grid:
        print(''.join(line))
    print()

print('What are the eight capital letters?\n')
print_string(dots)

