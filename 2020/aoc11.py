# --- Day 11: Seating System ---
from copy import deepcopy
from pprint import pp

seats = [*map(list,open('input/aoc11_input.txt').read().splitlines())]
y_size, x_size = len(seats), len(seats[0])

# Check the eight positions immediately up, down, left, right, or diagonal from the seat
def adjacent(seats,y,x):
    count = 0
    adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for yi,xi in adj:
        if 0 <= x+xi < x_size and 0 <= y+yi < y_size and seats[y+yi][x+xi] == "#":
            count += 1
    # print(f"Seat({y},{x}) is {seats[y][x]} and has {count} filled adjacent seats.")
    return count


def next(seats):
    new = deepcopy(seats)
    for y in range(y_size):
        for x in range(x_size):
            if seats[y][x] == ".": continue
            if adjacent(seats, y, x) == 0: new[y][x] = "#"
            if adjacent(seats, y, x) >= 4: new[y][x] = "L"
    return new


def print_string(seats):
    # print(''.join(seats[60]))
    for line in seats:
        print(''.join(line))
    print()


def run():
    seat_history = [seats]
    print_string(seat_history[0])
    for i in range(1, 1000):
        seat_history.append(next(seat_history[i-1]))
        print_string(seat_history[i])
        if seat_history[i] == seat_history[i-1]:
            print(f"Seating equilibrium at: {i-1}")
            return sum(line.count('#') for line in seat_history[i])

# How many seats end up occupied?
print(f"Seating: {run()}")

