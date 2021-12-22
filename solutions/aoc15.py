# --- Day 15: Chiton ---
from pprint import pp
import heapq
from helpers import timer, string_print

grid = [*map(list,open('../input/15_input.txt').read().splitlines())]
grid = [list(map(int, line)) for line in grid]

@timer
def shortest_path(grid):
    y_size, x_size = len(grid),len(grid[0])
    paths = [(0,0,0)]
    visited = [[0] * len(row) for row in grid]
    while True:
        total, x, y = heapq.heappop(paths)
        if visited[x][y]: continue
        if (x, y) == (x_size - 1, y_size - 1):
            return total
        visited[x][y] = 1
        for nx, ny in [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]:
            if not y_size > nx >= 0 <= ny < x_size: continue
            if visited[nx][ny]: continue
            heapq.heappush(paths, (total + grid[nx][ny], nx, ny))

print(f"Shortest path: {shortest_path(grid)}")

# --- Part Two ---
grid2 = [[0] * len(row) * 5 for row in grid * 5]
y_size, x_size = len(grid),len(grid[0])

def wrap(x):
    return (x - 1) % 9 + 1

for y in range(len(grid2)):
    for x in range(len(grid2[0])):
        grid2[y][x] = wrap(grid[y % y_size][x % x_size] + y // y_size + x // x_size)

# string_print(grid2, ' ')

print(f"Full map shortest path: {shortest_path(grid2)}")
