# --- Day 17: Trick Shot ---

# min_x, max_x, min_y, max_y = 20, 30, -10,-5
from solutions.helpers import timer,expanding_range_2d

min_x, max_x, min_y, max_y = 207, 263, -115, -63


def hit(vx, vy, x=0, y=0):
    global highest
    x += vx
    y += vy
    # print(f"loc: {x}, {y}  \t dir: {vx}, {vy}")
    if min_x <= x <= max_x and min_y <= y <= max_y:
        return True
    if y < min_y:
        return False
    vy -= 1
    if vx == 0: vx = 0
    elif vx == abs(vx): vx -= 1
    else: vx += 1
    return hit(vx, vy, x, y)

valids = []
valid_ys = []

@timer
def run():
    # for vx, vy in expanding_range_2d(140, 0):
    for vx in range(18,max_x+1):
        for vy in range(min_y-1,300):
            if hit(vx, vy):
                valids.append((vx, vy))
                valid_ys.append(vy)
                print(len(valids), vx, vy)

def highest(vy):
    x=0
    while vy >= 0:
        x+= vy
        vy -= 1
    return x

run()

print('Highest Y position:', highest(max(valid_ys)))
print('Distinct velocities:', len(valids))