# --- Day 7: The Treachery of Whales ---
positions = [int(days) for days in open('input/07_input.txt').read().split(',')]

fuel_dict = {}
for align in range(max(positions)):
    fuel = 0
    for pos in positions:
        fuel += abs(align - pos)
    fuel_dict[align] = fuel

# How much fuel must they spend to align to that position?
print(f"Position: {min(fuel_dict, key=fuel_dict.get)}\t Fuel expediture: {min(fuel_dict.values())}")