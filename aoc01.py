test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
report = [int(line.rstrip('\n')) for line in open("input_aoc01.txt")]
print(report)
larger_count = 0

for i in range(len(report)-1):
    if report[i+1] > report[i]:
        larger_count += 1
print(larger_count)
