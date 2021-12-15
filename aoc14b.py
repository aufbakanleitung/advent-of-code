# --- Day 14: Extended Polymerization ---
from helpers import timer

polymer, ins = open('input/14_example.txt').read().split('\n\n')
ins = {insert.split(' -> ')[0]:insert.split(' -> ')[1] for insert in ins.splitlines()}
pc = dict.fromkeys(ins, 0)

def count_pairs(poly):
    new_pc = dict.fromkeys(ins,0)
    for i in range(len(poly)-1):
        new_pc[poly[i]+poly[i+1]] += 1
    return new_pc


def insert(pc):
    new_pc = dict.fromkeys(ins, 0)
    for c in pc:
        new_pc[c[0] + ins[c]] += pc[c]
        new_pc[ins[c] + c[1]] += pc[c]
    return new_pc


def count_letters(pc):
    letters = dict.fromkeys(set('NCNBCHB'), 0)
    for i in pc:
        letters[i[0]] += pc[i]
        letters[i[1]] += pc[i]
    print(letters)
    return letters

pc = count_pairs(polymer)
# Do steps
for i in range(9):
    pc = insert(pc)
    print(i+1, pc)

letters = count_letters(pc)
print("max-min difference: ", max(letters.values()) - min(letters.values()))
