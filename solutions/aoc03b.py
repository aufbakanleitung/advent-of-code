# --- Day 3b: Binary Diagnostic ---
from pprint import pp

lines = [line for line in open('../input/03_example.txt').read().splitlines()]

# What is the life support rating of the submarine?
oxygen = CO2 = 0
def count_most(lines, bit):
    count = 0
    for line in lines:
        if line[bit] == '1':
            count += 1
    if count >= len(lines) // 2:
        return 1
    else:
        return 0

count = (count_most(['01111', '01010'], 4))
print(count)

gamma = lines[:]
epsilon = lines[:]
for i in range(len(lines[0])):
    gamma_remove = []
    eps_remove = []
    if not count_most(lines, i):
        for line in lines:
            if not line[i]:
                eps_remove.append(line)
    if count_most(lines, i):
        for line in lines:
            if line[i]:
                gamma_remove.append(line)
    for rm in gamma_remove:
        if len(gamma) == 1:
            print(f"gamma final: {gamma}")
            break
        if rm in gamma:
            gamma.remove(rm)
    for rm in eps_remove:
        if len(eps_remove) == 1:
            print(f"epsilon: {epsilon}")
            break
        if rm in gamma:
            epsilon.remove(rm)
    print(f"gamma: {gamma}")
print(gamma)
print(eps_remove)
