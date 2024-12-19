# --- Day 4: Ceres Search ---
from pprint import pprint

grid = open('../input/04.txt').read().splitlines()

def part_one(grid):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 'X': continue
            for yy in [-1, 0, 1]:
                for xx in [-1, 0, 1]:
                    if xx == yy == 0: continue
                    if not (0 <= y + 3 * yy < len(grid) and 0 <= x + 3 * xx < len(grid[0])): continue
                    if grid[y + yy][x + xx] == 'M' and grid[y + 2 * yy][x + 2 * xx] == 'A' and grid[y + 3 * yy][x + 3 * xx] == 'S':
                        # print(f"Found {grid[y][x]}{grid[y + yy][x + xx]}{grid[y + 2 * yy][x + 2 * xx]}{grid[y + 3 * yy][x + 3 * xx]}"
                        #       f" at {x}, {y}")
                        count += 1
    return count
print(f"XMAS:  {part_one(grid)}")


# --- Part Two ---
def part_two(grid):
    A_list = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 'M': continue
            for yy in [-1, 1]:
                for xx in [-1, 1]:
                    if not (0 <= y + 2 * yy < len(grid) and 0 <= x + 2 * xx < len(grid[0])): continue
                    if grid[y + yy][x + xx] == 'A' and grid[y + 2 * yy][x + 2 * xx] == 'S':
                        # print(f"Found {grid[y][x]}{grid[y + yy][x + xx]}{grid[y + 2 * yy][x + 2 * xx]}"
                        #       f" at {y},{x}  {y + yy},{x + xx}  {y + 2 * yy},{x + 2 * xx}")
                        A_list.append((y + yy,x + xx))
    return len(A_list) - len(set(A_list))

print(f"X-MAS: {part_two(grid)}")
