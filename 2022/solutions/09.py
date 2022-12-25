# --- Day 9: Rope Bridge ---
lines = open('../input/09i.txt').read().splitlines()
dir = {'R':(0,1), 'U':(1,0), 'L':(0,-1), 'D':(-1,0)}
head_l = [(0,0)]
tail_l = [(0,0)]

for line in lines:
    d, a = line.split()[0], int(line.split()[1])
    for _ in range(a):
        hy = head_l[-1][0] + dir[d][0]
        hx = head_l[-1][1] + dir[d][1]
        head_l.append((hy,hx))
        res = tuple(map(lambda i, j:i-j,(hy,hx),tail_l[-1]))
        if res[0] > 1 or res[0] < -1 or res[1] > 1 or res[1] < -1:
            ty = head_l[-1][0] - dir[d][0]
            tx = head_l[-1][1] - dir[d][1]
            tail_l.append((ty,tx))
        # print("H:", head_l[-1], "T:", tail_l[-1])
print(f"Visited {len(set(tail_l))} places")