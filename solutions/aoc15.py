# --- Day 15: Chiton ---
from pprint import pp
import heapq
from helpers import timer, string_print

grid = [*map(list,open('../input/15_input.txt').read().splitlines())]
grid = [list(map(int, line)) for line in grid]

@timer
def shortest_path(grid):
    y_size, x_size = len(grid),len(grid[0])
    paths = [(0,0,0)]  # total, y, x
    visited = [[0] * len(row) for row in grid]
    while True:
        total, y, x = heapq.heappop(paths)  # Get coordinates for lowest path
        if visited[y][x]: continue
        if (y, x) == (y_size - 1, x_size - 1):
            return total
        visited[y][x] = 1
        for ny, nx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:  # prefer down and right
            if not x_size > ny >= 0 <= nx < y_size: continue
            if visited[ny][nx]: continue
            heapq.heappush(paths, (total + grid[ny][nx], ny, nx))

print(f"Shortest path: {shortest_path(grid)}")

# --- Part Two ---
def wrap(x):
    return (x - 1) % 9 + 1

def unfold_map(grid):
    grid2 = [[0] * len(row) * 5 for row in grid * 5]
    y_size,x_size = len(grid),len(grid[0])
    for y in range(len(grid2)):
        for x in range(len(grid2[0])):
            grid2[y][x] = wrap(grid[y % y_size][x % x_size] + y // y_size + x // x_size)
    return grid2

# string_print(grid2, ' ')
grid2 = unfold_map(grid)
print(f"Full map shortest path: {shortest_path(grid2)}")
