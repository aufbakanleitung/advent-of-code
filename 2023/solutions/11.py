#--- Day 11: Cosmic Expansion ---
from itertools import combinations

grid = open("../input/11.txt").read().splitlines()

erows = [r for r, row in enumerate(grid) if all(x == "." for x in row)]
ecols = [c for c, col in enumerate(zip(*grid)) if all(y == "." for y in col)]
galaxies = [[r,c] for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]

# Expand galaxy
for i, (r,c) in enumerate(galaxies):
    for er in erows:
        if r > er:
            galaxies[i][0] += 999999
    for ec in ecols:
        if c > ec:
            galaxies[i][1] += 999999

# Sum distances
tot = 0
for (r1, c1), (r2, c2) in combinations(galaxies, 2):
    tot += abs(r2-r1) + abs(c2-c1)
print(tot)