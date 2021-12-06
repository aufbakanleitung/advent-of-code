# --- Day 1b: Sonar Sweep ---
scans = [int(line) for line in open('input/01_input.txt').read().splitlines()]

# three-measurement sliding window
count = 0
for i in range(len(scans)-3):
    window_a = scans[i] + scans[i+1] + scans[i+2]
    window_b = scans[i+1] + scans[i+2] + scans[i+3]
    if window_b > window_a:
        count += 1

print(count)
