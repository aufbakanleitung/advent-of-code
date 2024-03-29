# --- Day 1: Calorie Counting ---
from helpers import timer

@timer
def main():
    bags = open('../input/01i.txt').read().split("\n\n")
    bags = [sum(list(map(int,bag.split('\n')))) for bag in bags]

    max_value = max(bags)
    max_index = bags.index(max_value)

    print(f"1a:  Bag {max_index} has {max_value} calories")

    # --- Day 1b ---
    bags = sorted(bags,reverse=True)
    print("1b: ", bags[0] + bags[1] + bags[2])
    return "your mom"

print(main())