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

# def binary_string_all_ones(length):
#     return '1' * length

def valid(target, line):
    if len(line) == 1: return sum
    if target % line[0] == 0 and valid(target, line[1:]): return True
    if target - line[0] > 0 and valid(target, line[1:]): return True
    return False

test =[3267, 81, 40, 27]
print(3267 % 27)
tar = 3267 // 27
tar -= 40
tar -= 81
print(tar)


valid(test[0], test[1:])

#
# for line in lines:
#     binary_str = binary_string_all_ones(len(line)-1)
#     for i in range(int(binary_str, 2)+1):
#         print(str(bin(i))[2:])
#         for i in str(bin(i))[2:]:
#             if 1 == 0: pass
#     # for nr in range(len(line)-1):
#     #     line[nr] + line[nr+1]