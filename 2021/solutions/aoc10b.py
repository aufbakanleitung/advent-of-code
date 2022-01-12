# --- Day 10: Syntax Scoring ---
lines = open('../input/10_input.txt').read().splitlines()

haakje_dict = {'(':')','{':'}','[':']','<':'>'}
def not_corrupt(line):
    state = []
    for s in line:
        if s in haakje_dict:
            state.append(s)
        elif haakje_dict[state[-1]] == s:
            state.pop()
        else:
            return False
    return state


scores = {'(':1,'[':2,'{':3,'<':4}
score_list = []
for line in lines:
    state = not_corrupt(line)
    if state:
        score = 0
        for s in reversed(state):
            score *= 5
            score += scores[s]
        score_list.append(score)

# Find the completion string for each incomplete line, score the completion strings,
# and sort the scores. What is the middle score?
# print(f"The corrupt lines sum to: {sum}")
score_list.sort()
print(f"The middle score is: {score_list[len(score_list)//2]}")

