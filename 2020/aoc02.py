# Day 2: Password Philosophy
# Second try because the first run was terrible
import re

pass_list = [line.rstrip('\n') for line in open("input/aoc02_input.txt")]
count1, count2 = 0, 0

for line in pass_list:
    n1, n2, letter, x, passw = re.split('[-:\s]', line)
    # lowest and highest number of times the letter must appear
    count1 += int(n1) <= passw.count(letter[0]) <= int(n2)
    # Exactly one of these positions must contain the given letter
    count2 += (passw[int(n1)-1] == letter) ^ (passw[int(n2)-1] == letter)

print(f'count1: {count1}\n'
      f'count2: {count2}')
