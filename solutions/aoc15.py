# --- Day 15: Chiton ---
from pprint import pp

lines = [*map(list,open('../input/15_example.txt').read().splitlines())]
risk = [list(map(int, line)) for line in lines]
pp(lines)