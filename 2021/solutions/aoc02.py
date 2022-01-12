# --- Day 2: Dive! ---
moves = [move.split() for move in open('../input/02_input.txt').read().splitlines()]
moves = [[move[0], int(move[1])] for move in moves]

x = y = 0
for move in moves:
    if move[0] == 'forward': x += move[1]
    if move[0] == 'down': y += move[1]
    if move[0] == 'up': y -= move[1]

print(f"horizontal: {x}\n"
      f"depth: {y}\n"
      f"product: {x*y}")