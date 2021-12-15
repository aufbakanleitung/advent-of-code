# --- Day 14: Extended Polymerization ---
from helpers import timer

polymer, ins = open('input/14_input.txt').read().split('\n\n')
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
    letters = dict.fromkeys(set('PHOSBSKBBBFSPPPCCCHNV'), 0)
    letters[polymer[-1]] += 1  # add the last letter of the polymer, because else it isn't counted
    for i in pc:
        letters[i[0]] += pc[i]
        # letters[i[1]] += pc[i]
    return letters
print(count_letters({'CH': 1, 'HB': 1, 'NC': 1, 'NB': 1, 'BC': 1, 'CN': 1}))

def plen(pc):
    return sum(pc.values()) + 1

pc = count_pairs(polymer)
# Do steps
for i in range(40):
    pc = insert(pc)
    print(f"#{i+1} len: {plen(pc)}  count: {count_letters(pc)}\n {pc}")


letters = count_letters(pc)
print("max-min difference: ", max(letters.values()) - min(letters.values()))
