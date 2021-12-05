# --- Day 3: Binary Diagnostic ---
lines = [line for line in open('input/03_input.txt').read().splitlines()]
# print(lines)

count = [0] * len(lines[0])

for line in lines:
    for i, c in enumerate(line):
        if c == '1':
            count[i] += 1
# print(count)

gamma = epsilon = 0
for i in range(len(lines[0])):
    gamma <<= 1
    epsilon <<= 1
    if count[i] > len(lines) // 2:
        gamma += 1
    else:
        epsilon += 1
    # print(f"Epsilon: {bin(epsilon)}")

print(f"What is the power consumption of the submarine?\n"
      f"Gamma: {gamma}\n"
      f"Epsilon: {epsilon}\n"
      f"Power: {gamma * epsilon}")