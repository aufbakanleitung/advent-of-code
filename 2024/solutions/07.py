# --- Day 7: Bridge Repair ---
from itertools import permutations
from pprint import pprint
import re

# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20


lines = [items.strip() for items in open('../input/07e.txt').read().splitlines()]
lines = [list(map(int, re.split(' |: ', line))) for line in lines]

def binary_string_all_ones(length):
    return '1' * length

def valid(line):
    if len(line) < 2: return sum
    if valid(line[1:]): line[1] * line[2]


for line in lines:
    binary_str = binary_string_all_ones(len(line)-1)
    for i in range(int(binary_str, 2)+1):
        print(str(bin(i))[2:])
        for i in str(bin(i))[2:]:
            if 1 == 0: pass
    # for nr in range(len(line)-1):
    #     line[nr] + line[nr+1]