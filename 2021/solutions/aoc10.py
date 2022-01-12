# --- Day 10: Syntax Scoring ---
from pprint import pp

lines = open('../input/10_example.txt').read().splitlines()
state = []
haakje_dict = {'(':')','{':'}','[':']','<':'>'}
points = {')':3,']':57,'}':1197,'>':25137}
def corrupt(line):
    for s in line:
        if s in haakje_dict:
            state.append(s)
        elif haakje_dict[state[-1]] == s:
            state.pop()
        else:
            print(f"Corrupt! Found illegal {s}")
            return points[s]
    return 0

sum = corrupts = 0
for line in lines:
    sum += corrupt(line)
print(f"The corrupt lines sum to: {sum}")
