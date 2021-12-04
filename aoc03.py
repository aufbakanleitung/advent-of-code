lines = [line for line in open('input/03_example.txt').read().splitlines()]
print(lines)

count = [0] * len(lines[0])

for line in lines:
    for i, c in enumerate(line):
        if c == '1':
            count[i] += 1

gamma = epsilon = 0
for i in range(len(lines[0])):
    gamma