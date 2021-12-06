# --- Day 6: Lanternfish ---
school = [int(days) for days in open('input/06_input.txt').read().split(',')]

def count_fish(school):
    fish_age = {}
    for c in range(9):
        fish_age[c] = school.count(c)
    return fish_age
fish_age = count_fish(school)


def next_day():
    new_fish = fish_age[0]
    for c in range(0, 8):
        fish_age[c] = fish_age[c+1]
    fish_age[8] = new_fish
    fish_age[6] += new_fish


def simulate(days):
    for day in range(days+1):
        print(f"Day {day}\t Total fish: {sum(fish_age.values())}")
        next_day()
simulate(256)
