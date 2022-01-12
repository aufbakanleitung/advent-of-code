# --- Day 22: Reactor Reboot ---
# lines = [x.split(' ') for x in open('../input/22_example.txt').read().splitlines()]
import re

from helpers import timer

lines = [list(filter(None, re.split(' |,|=|x|y|z|\.', a))) for a in open('../input/22_input1.txt').read().splitlines()]
# bool = [n[0] for n in lines]
# lines = [list(map(lambda x: int(x) if int(x) else x, line[1:])) for line in lines]

@timer
def run():
    cube = set()
    for line in lines:
        if -50 < int(line[1]) < 50:
            print(line[1])
            for x in range(int(line[1]),int(line[2])+1):
                for y in range(int(line[3]),int(line[4])+1):
                    for z in range(int(line[5]),int(line[6])+1):
                        if line[0] == 'on':
                            cube.add(f"{x},{y},{z}")
                        if line[0] == 'off':
                            try: cube.remove(f"{x},{y},{z}")
                            except: pass
    return len(cube)

print(f"{run()} cubes are on")
