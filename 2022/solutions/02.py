# --- Day 2: Rock Paper Scissors ---
# X Y Z = Rock Paper Scissors = 1 2 3
moves = [move.split() for move in open('../input/02i.txt').read().splitlines()]

def count_moves(m):
    count = 0
    if m[0] == m[1]: count += 3
    if m[0] == 1 and m[1] == 2: count += 6
    if m[0] == 2 and m[1] == 3: count += 6
    if m[0] == 3 and m[1] == 1: count += 6
    count += m[1]
    return count

# --- Day 2b: X Y Z = Lose Draw Win ---
def count_b(m):
    count = 0
    if m[1] == 1:  # Lose
        if m[0] == 1: count += 3
        if m[0] == 2: count += 1
        if m[0] == 3: count += 2
    if m[1] == 2:  # Draw
        count += 3 + m[0]
    if m[1] == 3:  # Win
        count += 6
        if m[0] == 1: count += 2
        if m[0] == 2: count += 3
        if m[0] == 3: count += 1
    return count


scores = []
scores_b = []
for m in moves:
    m[0] = ord(m[0]) - 64
    m[1] = ord(m[1]) - 64 - 23
    scores.append(count_moves(m))
    scores_b.append(count_b(m))

print("Score A:", sum(scores))
print("Score B:", sum(scores_b))