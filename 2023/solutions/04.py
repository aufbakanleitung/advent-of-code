# --- Day 4: Scratchcards ---
import re
from pprint import pprint

lines = [items.strip() for items in open('../input/04.txt').read().splitlines()]
lines = [re.split(':|,|;|\|', line) for line in lines]
tickets = []

for line in lines:
    tickets.append([list(map(int, line[1].split())), list(map(int, line[2].split()))])
# pprint(tickets)

def part1(tickets):
    t_score = []
    for t, ticket in enumerate(tickets):
        ts = 0
        for nr in ticket[1]:
            if nr in ticket[0]:
                # print(t, "win:", nr)
                if ts == 0: ts += 1
                else: ts *= 2
        t_score.append(ts)
    print(t_score)
    return(t_score)
# print("Part 1:", sum(part1(tickets)))

def part2(tickets):
    t_score = []
    for t, ticket in enumerate(tickets):
        ts = 0
        for nr in ticket[1]:
            if nr in ticket[0]:
                ts += 1
                # print(t, "win:", nr)
        t_score.append(ts)
    return(t_score)

tic = []
for n in part2(tickets):
    tic.append([1,n])

# tic = [[1,4], [1,2], [1,2], [1,1], [1,0], [1,0]]
for n, t in enumerate(tic):
    for x in range(n+1, t[1]+n+1):
        tic[x][0] += tic[n][0]

som = 0
for n in tic:
    som += n[0]
print(som)
