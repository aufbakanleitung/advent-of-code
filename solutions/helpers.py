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


def string_print(grid, spacer=''):
    for line in grid:
        print(spacer.join(str(x) for x in line))
    print()


class expanding_range_2d:

    def __init__(self, start_value1, start_value2):
        self.start_value1 = start_value1
        self.start_value2 = start_value2

    def __iter__(self):
        yield self.start_value1, self.start_value2

        radius = 1
        while True:
            for i in range(-radius, radius):
                yield self.start_value1+i, self.start_value2-radius
                yield self.start_value1+radius, self.start_value2+i
                yield self.start_value1+radius-i-1, self.start_value2+radius
                yield self.start_value1-radius, self.start_value2+radius-i-1
            radius += 1