# Analyze the rotations in your attached document. What's the actual password to open the door?
# --- Day 1: Secret Entrance ---
import re

lines = [int(line.strip().replace("L", "-").replace("R", "")) for line in open('../input/01.txt').read().splitlines()]
print(lines)

# --- Part One ---
def part_one(lines):
    dail = 50
    count = 0
    for turn in lines:
        dail += turn
        dail = dail % 100
        if dail == 0: count += 1
    print(f"Count: {count}")
part_one(lines)

# --- Part Two ---
def part_two(lines):
    print(lines)
    dail = 50
    count = 0
    for line in lines:
        print(line, end='')
        if dail == 0 and line[0] == "L":
            count -= 1
            print(" subtract 1", end='')
        if line[0] == 'L': dail -= line[1]
        if line[0] == 'R': dail += line[1]
        if dail < 0: print(" add -", abs(dail // 100), end='')
        if dail < 0: count += abs(dail // 100)
        if dail > 100: print(" add", dail // 100, end='')
        if dail > 100: count += dail // 100
        dail = dail % 100
        print(f" : {dail}")
        if dail == 0:
            count += 1
            print(" + 1")
    print(f"Count: {count}")

dial = 50
count = 0
for turn in lines:
    if turn < 0:
        div, mod = divmod(turn, -100)
        count += div
        if dial != 0 and dial + mod <= 0:
            count += 1
    else:
        div, mod = divmod(turn, 100)
        count += div
        if dial + mod >= 100:
            count += 1

    dial = (dial + turn) % 100

print(count)