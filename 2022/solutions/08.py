# --- Day 8: Treetop Tree House ---
from pprint import pp
lines = [[int(n) for n in line] for line in open('../input/08i.txt').read().splitlines()]
invisibles = [[0] * len(lines[0]) for _ in range(len(lines))]
pp(lines)

l = len(lines)  # if square
for y in range(l):
    right = -1
    left = -1
    for x in range(l):  # looking right
        if lines[y][x] > right:
            right = lines[y][x]
        else: invisibles[y][x] += 1
    for x in reversed(range(l)):  # looking left
        if lines[y][x] > left:
            left = lines[y][x]
        else: invisibles[y][x] += 1

for x in range(l):
    down = -1
    up = -1
    for y in range(l):  # looking down
        if lines[y][x] > down:
            down = lines[y][x]
        else: invisibles[y][x] += 1
    for y in reversed(range(l)):  # looking up
        if lines[y][x] > up:
            up = lines[y][x]
        else: invisibles[y][x] += 1

# pp(invisibles)
count = 0
for y in range(l):
    count += invisibles[y].count(4)
print(l*l - count)

