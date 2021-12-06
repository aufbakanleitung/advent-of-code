# --- Day 3: Binary Diagnostic ---
lines = [line for line in open('input/03_example.txt').read().splitlines()]

# What is the power consumption of the submarine?
gamma_rate = ''
for pos in range(len(lines[0])):
    common_counter = 0
    for line in lines:
        common_counter += int(line[pos])
    gamma_rate += str(common_counter*2 // len(lines))

epsilon_rate = ''
for bit in gamma_rate:
    if bit == '0': epsilon_rate += '1'
    if bit == '1': epsilon_rate += '0'

print(f"Gamma rate: {gamma_rate}\n"
      f"Epsilon rate: {epsilon_rate}\n"
      f"Power consumption: {int(gamma_rate, base=2) * int(epsilon_rate, base=2)} ")

