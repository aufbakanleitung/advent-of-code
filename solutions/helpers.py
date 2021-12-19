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
