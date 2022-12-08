# --- Day 8b: Treetop Tree House ---
from pprint import pp
trees = [[int(n) for n in line] for line in open('../input/08i.txt').read().splitlines()]
invisibles = [[0] * len(trees[0]) for _ in range(len(trees))]
# pp(trees)

l = len(trees)  # if square
def view(ty, tx, th):
    right = left = down = up = 0
    for x in range(tx+1, l):  # looking right
        right += 1
        if trees[ty][x] >= th:
            break
    for x in range(tx-1, -1, -1):  # looking left
        left += 1
        if trees[ty][x] >= th:
            break
    for y in range(ty+1, l):  # looking down
        down += 1
        if trees[y][tx] >= th:
            break
    for y in range(ty-1, -1, -1):  # looking up
        up += 1
        if trees[y][tx] >= th:
            break
    return up * left * right * down

scenic_high_score = 0
for y in range(l):
    for x in range(l):
        scenic_score = view(y,x,trees[y][x])
        if scenic_score > scenic_high_score:
            scenic_high_score = scenic_score

print("Scenic score:", scenic_high_score)


