# --- Day 1: Sonar Sweep ---

scans = [int(line) for line in open('input/01_input.txt').read().splitlines()]
print(scans)

# How many measurements are larger than the previous measurement?
count = 0
for i in range(len(scans)):
    if scans[i] > scans[i-1]:
        count += 1
print(f"Measurements larger than previous: {count}")
