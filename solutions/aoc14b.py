# --- Day 14: Extended Polymerization ---
from helpers import timer

polymer, ins = open('../input/14_example.txt').read().split('\n\n')
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
    letters = dict.fromkeys(set('PHOSBSKBBBFSPPPCCCHNV'), 0)  # A bit hacky
    letters[polymer[-1]] += 1  # add the last letter of the polymer, because else it isn't counted
    for i in pc:
        letters[i[0]] += pc[i]
    return letters


def plen(pc):
    return sum(pc.values()) + 1

@timer
def run():
    pc = count_pairs(polymer)
    # Do steps
    for i in range(40):
        pc = insert(pc)
        print(f"#{i+1} length: {plen(pc)} \ncount: {count_letters(pc)}")
    letters = count_letters(pc)
    print("max-min difference: ", max(letters.values())-min(letters.values()))

run()
