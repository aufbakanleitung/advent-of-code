# --- Day 2: Dive! ---
import re

moves = [re.split('[\s]', line.rstrip('\n')) for line in open("input/02_input.txt")]
x = 0
y = 0
for move in moves:
    if move[0] == 'forward':
        x += int(move[1])
    if move[0] == 'down':
        y += int(move[1])
    if move[0] == 'up':
        y -= int(move[1])

print(f"Horizontal: {x}\n"
      f"Depth: {y}\n"
      f"Product: {x*y}")