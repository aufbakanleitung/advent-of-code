# --- Day 1: Historian Hysteria ---
# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found.
import re

lines = [items.strip() for items in open('../input/01.txt').read().splitlines()]
lines = [list(map(int, re.split('   ', line))) for line in lines]
transposed = list(map(list, zip(*lines)))


def part_one(transposed):
    transposed[0].sort()
    transposed[1].sort()
    distance = 0
    for a in range(len(transposed[0])):
        distance += abs(transposed[1][a] - transposed[0][a])
    print(f"Total distance: {distance}")
part_one(transposed)


# --- Part Two ---
product_sum = 0
for x in transposed[0]:
    product_sum += x * transposed[1].count(x)
print(f"Similarity score: {product_sum}")