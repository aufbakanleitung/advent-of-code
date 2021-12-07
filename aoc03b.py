# --- Day 3b: Binary Diagnostic ---
from pprint import pp

lines = [line for line in open('input/03_example.txt').read().splitlines()]
pp(lines)

# What is the life support rating of the submarine?
oxygen = CO2 = 0
def count_most(lines, bit):
    count = 0
    for line in lines:
        if line[bit] == '1':
            count += 1
    if count > len(lines) // 2:
        return 1
    else:
        return 0

count = (count_most(lines, 0))
print(count)

gamma = lines[:]
epsilon = lines[:]
for i in range(len(lines[0])):
    gamma_remove = []
    eps_remove = []
    if len(gamma) == 1: print(f"gamma: {gamma}")
    if len(eps_remove) == 1: print(f"epsilon: {epsilon}")
    if count_most(lines, i):
        for line in lines:
            if line[i]:
                gamma_remove.append(line)
            if not line[i]:
                eps_remove.append(line)
    for rm in gamma_remove:
        if rm in gamma:
            gamma.remove(rm)
    for rm in eps_remove:
        epsilon.remove(rm)

# for i in range(len(lines[0])):
#     if count_most(lines, i):
#         for lines in lines:
#             gamma.
#
#     most, least = counter(lines)
#     if line[i] != most[i]:
#         print('remove')
#         print(lines)
#         lines.remove(line)
# print(lines)