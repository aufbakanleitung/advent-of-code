# --- Day 3: Rucksack Reorganization ---
from pprint import pprint
sacks = [items for items in open('../input/03i.txt').read().splitlines()]
sacks_c = [[items[0:len(items)//2],items[len(items)//2:]] for items in sacks]

def counter(i):
    if ord(i) > 96:
        return ord(i)-96
    else:
        return ord(i)-38

count_a = 0
for sack in sacks_c:
    for i in sack[0]:
        if i in sack[1]:
            count_a += counter(i)
            break
print("Day 3a:", count_a)
# ------------
count_b = 0
for n in range(0, len(sacks), 3):
    for i in sacks[n]:
        if i in sacks[n+1] and i in sacks[n+2]:
            count_b += counter(i)
            break
print("Day 3b:", count_b)
