![](input/advent%20of%20code.jpg)
# Advent of Code 2021: Python solutions
https://adventofcode.com/2021
∂∂
## Lessons learned:
**Assignment 1** 

Load the input file on a single line using list comprehension
```python
report = [int(line.rstrip('\n')) for line in open("input/01_input.txt")]
```

**Assignment 2** 

Convert list of lists to correct filetypes using list comprehension
```python
moves = [[move[0], int(move[1])] for move in moves]
```

Initialize multiple variables with sequential equal signs 
```python
x = y = aim = 0
```