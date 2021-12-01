test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
report = [int(line.rstrip('\n')) for line in open("input_aoc01.txt")]
count = 0

for i in range(len(report)-3):
    window_a = report[i] + report[i+1] + report[i+2]
    window_b = report[i+1] + report[i+2] + report[i+3]
    if window_b > window_a:
        count += 1

print(count)
