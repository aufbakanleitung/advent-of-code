![](input/advent%20of%20code.jpg)
# Advent of Code 2022: Lessons learned
https://adventofcode.com/2022

## Assignment 1 ('22)

Convert a list of strings to ints using `map(int,[])`, convert the resulting map-object back to list with `list()`.
```python
list(map(int,bag.split('\n')))
```

![](input/advent%20of%20code.jpg)
# Advent of Code 2021: Lessons learned
https://adventofcode.com/2021

## Assignment 1 

Load the input file as integers on a single line using list comprehension
```python
scans = [int(line) for line in open('input/01_input.txt').read().splitlines()]
```

## Assignment 2 

Convert list of lists to correct filetypes using list comprehension
```python
moves = [[move[0], int(move[1])] for move in moves]
```

Initialize multiple variables with sequential equal signs 
```python
x = y = aim = 0
```

## Assignment 3 

Use the binary left shift `<<` to append a binary variable without type conversion 
```python
gamma = 0
for i in range(x):
    gamma <<= 1
```


## Assignment 4

Load first variable in one var and all subsequent variables in another with `*var`

```python
numbers, *boards = open('input/04_input.txt').read().split('\n\n')
```

Don't remove values from a list you're iterating over while iterating. This will cause the iterator to skip items. For a set it is even prohibited and will throw this error `RuntimeError: Set changed size during iteration`
```python
for board in boards:
    if check(board):
        boards.remove(board)  # This is bad
```

Instead, make a separate list/set/dict to store removed values and check for them in for-loop.
Also consider using an enumerator to store indexes instead of entire datasets for efficiency.
```python
done_boards = set()
for index, board in enumerate(boards):
    if index in done_boards:  continue
    if check(board):  done_boards.add(index)
```


## Assignment 5

Don't generate an empty (3x3) list of lists like below; the grid will contain 3 references to the same data item.
```python
grid = [[0] * 3] * 3

for line in grid:
    print(id(line))
# 4390269824
# 4390269824
# 4390269824
```
Instead create a new list every time and append it to the list of lists.

```python
grid2 = [[0] * 3 for _ in range(3)]
```

Split and cast values over multiple variables using `map()`
```python
x, y = map(int, var.split(','))
```

## Assignment 13
Print a list as a string so it looks more compact.
```python
for line in grid:
    print(''.join(line))
```

## Assignment 14
Directly load a split line as a dictionary with dict comprehension
```python
lines = {x.split()[0]:x.split()[1] for x in lines.splitlines()}
```

It is common to count occurrences of certain values with a dict, e.g.: `{'x': 2, 'y': 3}` 
Initialize a dict with the all the values set at 0 using `.fromkeys(x, 0)`, and get all the unique values with a `set()`
```python
pc = dict.fromkeys(set(lines), 0)
```

To time a function it is common to use a wrapper, which then uses a decorator. 
A decorator is a function that takes a function as an argument.
```python
def decorator(func): 
    def wrap(*args):  # take any arguments
        result = func(*args)
        return result
    return wrap 
some_function = decorator(some_function)
```

A wrapper is a notation to replace this line `function_used = decorator(function_used)` 
with a more convenient `@decorator`
```python
@timer
def run():
    for _ in range(10):
        sleep(.5)
run()
# Time required: 5034.56 ms
```

## Assignment 15
My first implementation of a Depth-first search (DFS): this is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node and explores as far as possible along each branch before backtracking. It uses a heap (`heapq`), which is a data type that efficiently stores the smallest value first, to store the path sum (and corresponding coordinates). It pops the lowest value from the heap and adds all 4 values around back to the heap and then repeats a the next lowest point. 

This implementation only returns the path sum `total` and it doesn't store the actual path taken. 

```python
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
```

# Advent of Code 2020: Lessons learned
https://adventofcode.com/2020


* assignment 2 - You can use the bitwise operator `^` to do a xor in python: 
```python
if bool(a) ^ bool(b):
```
* assignment 2 - Immediately assign split values to their variables for efficiency.
```python 
n1, n2, letter, x, passw = re.split('[-:\s]', line)
```
* assignment 3 - If you're using the `x` coordinate to calculate the `y` coordinate by, don't forget to divide y over x's step size `xn` to make them independent again (`x*yn/xn`). Though it's probably better never to make the two depend on each other in the first place.
```python    
for x in range(0, len(trees), xn):
    y = int(x*yn/xn) % len(trees[0])
```
* assignment 4 - This is a way to convert a list of lists with value pairs to a list of dictionaries, using list comprehension.
```python
    dict_list = [dict([(value_pair.split(":")) for value_pair in list]) for list in llist]
```
* assignment 4 - If you remove values from the list you're looping over the length will change and values will be skipped. Instead make a copy() of it and remove the values from there.
```python
list = [1,4,7,7,2,3,4,5]; copied_list = list.copy(); test = [3,4]  # Make three lists
[copied_list.remove(item) for item in list if item in test]        # Remove items in test from copied_list
```
* assignment 6 - This is how you sort a string.
```python
sorted_string = ''.join(sorted(unsorted_string))
```
* assignment 7 - In Regex look before a certain string with the `?=` positive lookahead and find all occurences with `re.findall()`.
```python
re.findall(r'(\d+)*\s*(\w+\s\w+)(?=\sbag)', line)
```
* assignment 7 - Recursion is very powerful, looks very clean, but it's really difficult to grasp.
```python
def find_bags(color): 
    teller = 0
    for bag in bags_dict[color]:
        teller += bags_dict[color][bag] + find_bags(bag) * bags_dict[color][bag]  # Recursively sum the contents of the bag
    return teller
```
