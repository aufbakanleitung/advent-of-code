# --- Day 22: Reactor Reboot ---
import re
from helpers import to_int
lines = [list(filter(None, re.split(' |,|=|x|y|z|\.', a)))
         for a in open('../input/22_example.txt').read().splitlines()]
lines = [to_int(line) for line in lines]


def overlap(cube1, cube2):
    b,x1,x2,y1,y2,z1,z2 = cube1
    _b,_x1,_x2,_y1,_y2,_z1,_z2 = cube2
    size = x2-x1 * y2-y1 * z2-z1
    return size

print(sum([overlap(lines[i]) for i, line in enumerate(lines)]))
