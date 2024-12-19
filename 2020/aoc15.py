# --- Day 15: Rambunctious Recitation ---
example = [0, 3, 6]
example2 = [0, 3, 6, 0, 3]
input = [19,0,5,1,10,13]
number_spoken = 2020

def find_index(input_list, value):
    values = []
    count = 0
    for pos, nr in reversed(list(enumerate(input_list))):
        if nr == value:
            values.append((pos, nr))
            count += 1
        if count >= 2:
            return values[-2][0], values[-1][0]
# print(find_index(example2, 3))

def step(input, nr):
    if nr in input[:-1]:
        last_pos, prev_pos = find_index(input, nr)
        input.append(last_pos - prev_pos)
        # input.append(len(input) - input[:-1].count(nr))
    else:
        input.append(input[:-1].count(nr))
    if len(input) == number_spoken:
        print(len(input), ":", input[-1])

while len(input) < number_spoken:
    step(input, input[-1])
