# --- Day 5: Hydrothermal Venture ---
lines = open('input/05_input.txt').read().splitlines()

# Generate grid, don't make my mistake to append list-references: [[0] * len(lines[0])] * len(lines)
grid = []
for i in range(len(lines)):
    grid.append(list([0] * len(lines[0])))

points = {}
for line in lines:
    l, r = line.split(' -> ')
    x1, y1 = map(int, l.split(','))
    x2, y2 = map(int, r.split(','))

    if y1 == y2:  # Horizontal line
        print("H:", x1,y1,x2,y2)
        for i in range(min(x1, x2), max(x1, x2)+1):
            points[(y1, i)] = points.get((y1, i), 0) + 1
            # grid[y1][i] += 1

    if x1 == x2:  # Vertical line
        print("V:", x1,y1,x2,y2)
        for i in range(min(y1, y2), max(y1, y2)+1):
            points[(i, x1)] = points.get((i, x1), 0) + 1
            # grid[i][x1] += 1

# At how many points do at least two lines overlap?
overlap_count = 0
for i in points.items():
    if i[1] >= 2:
        overlap_count += 1
print(overlap_count)
