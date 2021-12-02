# Advent of Code 2021: Python solutions
https://adventofcode.com/2021

## Lessons learned:
* assignment 1 - Load the input file on a single line using list comprehension

```python
report = [int(line.rstrip('\n')) for line in open("input/01_input.txt")]
```

* assignment 2 - Convert list of lists to correct filetypes using list comprehension

```python
moves = [[move[0], int(move[1])] for move in moves]
```