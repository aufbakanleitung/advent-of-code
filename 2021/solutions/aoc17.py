# --- Day 17: Trick Shot ---
from helpers import timer

# min_x, max_x, min_y, max_y = 20, 30, -10,-5
min_x, max_x, min_y, max_y = 207, 263, -115, -63

def hit(vx, vy, x=0, y=0):
    x += vx
    y += vy
    # print(f"loc: {x}, {y}  \t dir: {vx}, {vy}")
    if min_x <= x <= max_x and min_y <= y <= max_y:
        return True
    if y < min_y or x > max_x:
        return False
    vy -= 1
    if vx > 0: vx -= 1
    return hit(vx, vy, x, y)

valids = []
valid_ys = []

@timer
def run():
    for vx in range(20,max_x+1):  # 20 is experimentally determined
        for vy in range(min_y,300):
            if hit(vx, vy):
                valids.append((vx, vy))
                valid_ys.append(vy)
                print(len(valids), vx, vy)

def highest(vy):
    x=0
    while vy >= 0:
        x += vy
        vy -= 1
    return x
run()

print('Highest Y position:', highest(max(valid_ys)))
print('Distinct velocities:', len(valids))
