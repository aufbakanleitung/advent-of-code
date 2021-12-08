# --- Day 8: Seven Segment Search ---
from pprint import pp

segs = [[seg.split(' ') for seg in line.split(" | ")] for line in open('input/08_input.txt').read().splitlines()]

numbers = {}
for i, line in enumerate(segs):
    for j, out in enumerate(line[1]):
        if len(out) == 2:
            print(f"({i},{j}) nr 1: {out}")
            numbers[i,j] = '1'
        if len(out) == 3:
            print(f"({i},{j}) nr 7: {out}")
            numbers[i,j] = '7'
        if len(out) == 4:
            print(f"({i},{j}) nr 4: {out}")
            numbers[i,j] = '4'
        if len(out) == 7:
            print(f"({i},{j}) nr 8: {out}")
            numbers[i,j] = '8'
print(len(numbers))
