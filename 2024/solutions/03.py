# --- Day 3: Mull It Over ---
import re

example1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
lines = open('../input/03.txt').read()
mul_pattern = r'mul\((\d+),(\d+)\)'

matches = re.findall(mul_pattern, lines)
print(f"Part One - Product sum: {sum([int(x) * int(y) for x, y in matches])}")

# --- Part Two ---
example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
do_pattern = r"(do\(\)|don't\(\))"
combined_pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"

combined_matches = re.finditer(combined_pattern, lines)

active = True
prod_sum = 0
for match in combined_matches:
    if match.group(0) == "don't()": active = False
    if active and match.group(1) and match.group(2):
        prod_sum += int(match.group(2)) * int(match.group(3))
    if match.group(0) == "do()": active = True
print(f"Part Two - Product sum: {prod_sum}")