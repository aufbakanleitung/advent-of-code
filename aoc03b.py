# --- Day 3b: Binary Diagnostic ---
lines = [line for line in open('input/03_example.txt').read().splitlines()]

# What is the life support rating of the submarine?
oxygen = CO2 = 0
def counter(lines):
    count = [0] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            if c == '1':
                count[i] += 1
    most = [0] * len(lines[0])
    least = [1] * len(lines[0])
    for i in range(len(lines[0])):
        if count[i] > len(lines) // 2:
            most[i] = 1
        else:
            least[i] = 0
    return most, least

count = (counter(lines))
print(count)
gamma = epsilon = 0

for line in lines:
    for i in range(len(lines)):
        most, least = counter(lines)
        if line[i] != most[i]:
            print('remove')
            print(lines)
            lines.remove(line)
print(lines)