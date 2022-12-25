# --- Day 9b: Rope Bridge ---
lines = open('../input/09e.txt').read().splitlines()
dir = {'R':(0,1), 'U':(1,0), 'L':(0,-1), 'D':(-1,0)}
dir_diag = {
    (2,0):(1,0), (2,1):(1,0), (2,-1):(1,0),
    (0,2):(0,1), (1,2):(0,1), (-1,2):(0,1),
    (-2,0):(-1,0), (-2,1):(1,0), (-2,-1):(-1,0),
    (0,-2):(0,1), (1,-2):(0,1), (-1,-2):(0,-1)}
tail_set = [(0,0)]
rope = {}
length = 10

def move(d,l):
    hy = rope[l][0] + dir[d][0]
    hx = rope[l][1] + dir[d][1]
    rope[l] = (hy,hx)
    res = tuple(map(lambda i, j:i-j,(hy,hx),rope[l+1]))
    if abs(res[0]) > 1 or abs(res[1]) > 1:
        rope[l+1] = dir_diag[res]
        ty = rope[l][0] - dir[d][0]
        tx = rope[l][1] - dir[d][1]
        rope[l+1] = (ty, tx)
        if l == length-1:
            tail_set.append((ty,tx))
            return (ty,tx)

def solve():
    for l in range(length+1):
        rope[l] = (0,0)
    for line in lines:
        d, a = line.split()[0], int(line.split()[1])
        for _ in range(a):
            for l in range(length):
                move(d,l)

    print(rope)
    print(tail_set)
    print(f"Visited {len(set(tail_set))} places")

solve()