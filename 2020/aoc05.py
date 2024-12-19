# --- Day 5: Binary Boarding ---
# FBFBBFF = 44/127 rows (2^7)
# RLR = 5/7 columns (2^3)
example = ['FBFBBFFRLR']
seats = [line.rstrip('\n') for line in open("input/aoc05_input.txt")]

def to_seatnr(seat):
    seatnr = ''
    for r in seat:
        if r == 'F' or r == 'L': seatnr += '0'
        if r == 'B' or r == 'R': seatnr += '1'
    return int(seatnr[0:7], 2), int(seatnr[7:10], 2)

seatIDs = []
for seat in seats:
    row, column = to_seatnr(seat)
    seatID = row*8 + column
    seatIDs.append(seatID)

# What is the highest seat ID on a boarding pass?
print("Highest boarding pass:", (sorted(seatIDs)[-1]))

# What is the ID of the missing seat?
count = 91
for i in (sorted(seatIDs)):
    if i != count:
        print("Missing seat:", i)
        break
    else:
       count += 1

