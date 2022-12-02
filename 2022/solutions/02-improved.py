# --- Day 2: Rock Paper Scissors - Romeo's solution ---
score_lookup = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
print(sum([score_lookup[move] for move in open('../input/02i.txt').read().splitlines()]))