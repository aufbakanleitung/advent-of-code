# --- Day 13: Transparent Origami ---
from pprint import pp

coor, folds = open('input/13_input.txt').read().split('\n\n')
folds = [line.split()[2] for line in folds.splitlines()]
pp(folds)

dots = set()

for c in coor.splitlines():
    x, y = map(int, c.split(","))
    dots.add((x, y))
print(len(dots))

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

# for fold in folds[0]:
dots = fold_it(dots, folds[0])

# How many dots are visible after completing just
# the first fold instruction on your transparent paper?
print(len(dots))

