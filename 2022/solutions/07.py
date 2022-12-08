# --- Day 7: No Space Left On Device ---
from pprint import pprint
lines = open('../input/07i.txt').read().splitlines()
pwd = {}
root = {}
stack = []

for line in lines:
    line = line.strip()
    if line[0] == "$":
        if line[2] == "c":
            dir = line[5:]
            if dir == "/":
                pwd = root
                stack = []
            elif dir == "..":
                pwd = stack.pop()
            else:
                if dir not in pwd:
                    pwd[dir] = {}
                stack.append(pwd)
                pwd = pwd[dir]
    else:
        x,y = line.split()
        if x == "dir":
            if y not in pwd:
                pwd[y] = {}
        else:
            pwd[y] = int(x)

# pprint(root)

def solve_a(dir=root):
    if type(dir) == int:
        return (dir,0)
    size = 0
    ans = 0
    for child in dir.values():
        s,a = solve_a(child)
        size += s
        ans += a
    if size <= 100000:
        ans += size
    return (size, ans)
print(solve_a())

def size(dir = root):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))


t = size() - 40_000_000


def solve(dir = root):
    ans = float("inf")
    if size(dir) >= t:
        ans = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        q = solve(child)
        ans = min(ans, q)
    return ans

print(solve())