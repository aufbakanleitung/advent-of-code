# --- Day 9: Smoke Basin ---
from pprint import pp

area = [*map(list,open('input/09_input.txt').read().splitlines())]
y_size, x_size = len(area), len(area[0])


def adjacent_lower(area,y,x):
    count = 0
    adj = [(-1,0),(0,-1),(0,1),(1,0)]
    for yi,xi in adj:
        if 0 <= x+xi < x_size and 0 <= y+yi < y_size:
            count += 1
            if area[y][x] < area[y+yi][x+xi]:
                count -= 1
            # print(f"point({y+yi},{x+xi}) is {area[y][x]} and has {count} higher points.")
    return True if count == 0 else False

tot = 0
for y in range(y_size):
    for x in range(x_size):
        if adjacent_lower(area, y, x):
            tot += int(area[y][x]) + 1
# What is the sum of the risk levels of all low points on your heightmap?
print(f"Sum of low points: {tot}")
