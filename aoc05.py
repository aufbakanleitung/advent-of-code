# --- Day 5: Hydrothermal Venture ---
from pprint import pp

lines = open('input/05_example.txt').read().splitlines()

gridline = [0] * len(lines[0])
grid = []
for i in range(len(lines)):
    grid.append(list(gridline))

for line in lines:
    l, r = line.split(' -> ')
    x1, y1 = map(int, l.split(','))
    x2, y2 = map(int, r.split(','))
    if y1 == y2:  # Horizontal line
        print("H:", x1,y1,x2,y2)
        for i in range(x1, x2+1):
            grid[y1][i] += 1

    if x1 == x2:  # Vertical line
        print("V:", x1,y1,x2,y2)
        for i in range(y1, y2+1):
            grid[i][x1] += 1
pp(grid)

