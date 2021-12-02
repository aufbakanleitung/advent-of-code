# --- Day 2: Dive! ---

moves = [line.split() for line in open("input/02_input.txt").read().splitlines()]
moves = [[move[0], int(move[1])] for move in moves]

x = y = aim = 0

for move in moves:
    if move[0] == 'forward':
        x += move[1]
        y += move[1] * aim
    if move[0] == 'down':
        aim += move[1]
    if move[0] == 'up':
        aim -= move[1]

print(f"Horizontal: {x}\n"
      f"Depth: {y}\n"
      f"Product: {x*y}")