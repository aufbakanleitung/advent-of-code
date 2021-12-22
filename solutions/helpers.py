from itertools import count,chain
import heapq
from functools import wraps
from time import time

def timer(func):
    # define a function within a function, and call it with a decorator (@timer)
    # Takes any amount of arguments: args = arguments, kwargs = keyword arguments
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        print(f"\nTime required: {(time() - start_time)*1000:.2f} ms")
        return result
    return wrapper


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


def string_print(grid, spacer=''):
    for line in grid:
        print(spacer.join(str(x) for x in line))
    print()


def expanding_range(x0):
    down = count(x0, -1)
    up = count(x0 + 1)
    return chain.from_iterable(zip(down, up))


def expanding_range_2d(x0, y0):
    yield x0, y0
    for radius in count(1):
        for i in range(-radius, radius):
            yield x0+i, y0-radius
            yield x0+radius, y0+i
            yield x0-i, y0+radius
            yield x0-radius, y0-i


def expanding_manhattan_2d(x0, y0):
    yield x0, y0
    for radius in count(1):
        for i in range(radius):
            j = radius - i
            yield x0+i, y0-j
            yield x0+j, y0+i
            yield x0-i, y0+j
            yield x0-j, y0-i


