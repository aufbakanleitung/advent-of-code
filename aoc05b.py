# --- Day 5: Hydrothermal Venture ---
from pprint import pp

lines = open('input/05_input.txt').read().splitlines()

# Generate grid, don't make my mistake to append list-references: [[0] * len(lines[0])] * len(lines)
# Grid is only useful for example, comment out for 05_input.txt
grid = []
for i in range(len(lines)):
    grid.append(list([0] * len(lines[0])))

points = {}
for line in lines:
    l, r = line.split(' -> ')
    x1, y1 = map(int, l.split(','))
    x2, y2 = map(int, r.split(','))

    if y1 == y2:  # Horizontal line
        # print("H:", x1,y1,x2,y2)
        for x in range(min(x1, x2), max(x1, x2)+1):
            points[(y1, x)] = points.get((y1, x), 0) + 1  # get key or return 0
            # grid[y1][x] += 1

    if x1 == x2:  # Vertical line
        # print("V:", x1,y1,x2,y2)
        for y in range(min(y1, y2), max(y1, y2)+1):
            points[(y, x1)] = points.get((y, x1), 0) + 1
            # grid[y][x1] += 1

    if not (x1 == x2 or y1 == y2):  # Diagonal line
        # print("D:", x1,y1,x2,y2)
        dx = x2 - x1
        dy = y2 - y1
        points[(y1, x1)] = points.get((y1, x1), 0) + 1
        # grid[y1][x1] += 1
        while not x1 == x2:
            x1 = x1 + (dx // abs(dx))  # get positive (1) or negative (-1)
            y1 = y1 + (dy // abs(dy))
            points[(y1, x1)] = points.get((y1, x1), 0) + 1
            # grid[y1][x1] += 1

# pp(grid)

# At how many points do at least two lines overlap?
overlap_count = 0
for i in points.items():
    if i[1] >= 2:
        overlap_count += 1
print(f"Overlapping lines: {overlap_count}")

