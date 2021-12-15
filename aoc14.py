# --- Day 14: Extended Polymerization ---
from helpers import timer

polymer, inserts = open('input/14_input.txt').read().split('\n\n')
poly_list = [polymer]
inserts = {insert.split(' -> ')[0]:insert.split(' -> ')[1] for insert in inserts.splitlines()}

def insert(poly):
    pl = poly[0]
    for i in range(len(poly)-1):
        pl += inserts.get(poly[i]+poly[i+1]) + poly[i+1]
    return pl

@timer
def run(times):
    for j, poly in enumerate(poly_list):
        print(j,':', len(poly))
        if j >= times:
            break
        poly_list.append(insert(poly))

    count = {}
    for l in set(poly_list[-1]):
        count[l] = poly_list[-1].count(l)
    print(count)

    return int(max(count.values())) - int(min(count.values()))

print("difference:", run(10))
