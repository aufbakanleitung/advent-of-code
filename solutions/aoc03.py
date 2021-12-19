# --- Day 3: Binary Diagnostic ---
lines = open('../input/03_input.txt').read().splitlines()
count = [0] * len(lines[0])

for line in lines:
    for i, c in enumerate(line):
        if c == '1':
            count[i] += 1

gamma = epsilon = 0
for i in range(len(lines[0])):
    gamma <<= 1
    epsilon <<= 1
    print(bin(gamma))
    print(bin(epsilon))
    if count[i] > len(lines) // 2:
        gamma += 1
    else:
        epsilon += 1
    # print(f"Epsilon: {bin(epsilon)}")

print(f"What is the power consumption of the submarine?\n"
      f"Gamma: {gamma}\n"
      f"Epsilon: {epsilon}\n"
      f"Power: {gamma * epsilon}")