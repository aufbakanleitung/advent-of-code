# --- Day 3: Binary Diagnostic ---
lines = [line for line in open('input/03_example.txt').read().splitlines()]


print(round(0.5))

# What is the life support rating of the submarine?
gamma_rate = ''
def common_count(slist, pos):
    common_counter = 0
    for line in slist:
        common_counter += int(line[pos])
    fraction = (common_counter * 2) / len(lines) == 0.5
    if fraction == 0.5:
        return '1'
    else:
        return str(round(fraction))


s_lines = lines.copy()
for pos in range(len(lines[0])):
    print(s_lines)
    common_digit = common_count(s_lines, pos)
    for line in s_lines:
        if common_digit != line[pos]:
            s_lines.remove(line)


