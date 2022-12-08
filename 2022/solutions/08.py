# --- Day 8: Treetop Tree House ---
from pprint import pp
trees = [[int(n) for n in line] for line in open('../input/08i.txt').read().splitlines()]
invisibles = [[0] * len(trees[0]) for _ in range(len(trees))]

l = len(trees)  # if square
for y in range(l):
    right = -1
    left = -1
    for x in range(l):  # looking right
        if trees[y][x] > right:
            right = trees[y][x]
        else: invisibles[y][x] += 1
    for x in reversed(range(l)):  # looking left
        if trees[y][x] > left:
            left = trees[y][x]
        else: invisibles[y][x] += 1

for x in range(l):
    down = -1
    up = -1
    for y in range(l):  # looking down
        if trees[y][x] > down:
            down = trees[y][x]
        else: invisibles[y][x] += 1
    for y in reversed(range(l)):  # looking up
        if trees[y][x] > up:
            up = trees[y][x]
        else: invisibles[y][x] += 1

# pp(invisibles)
count = 0
for y in range(l):
    count += invisibles[y].count(4)
print(l*l - count)

