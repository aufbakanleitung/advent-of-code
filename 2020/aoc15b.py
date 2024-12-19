# --- Day 15: Rambunctious Recitation ---
example = [0, 3, 6, 0]
example2 = [0, 1, 2, 3, 6, 0, 3]
input = [19,0,5,1,10,13]
number_spoken = 2020

nr_dict = {number: turn + 1 for turn, number in enumerate(example2)}
last_number = example2.pop(-1)
print(nr_dict)
for turn in range(len(nr_dict)-1, 20+1):
    if not nr_dict[last_number]:
        print(0)
        nr_dict[0] = turn
    else:
        print(turn - nr_dict[turn])


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

nr_dict = {0:[0,0,0], 1:[0,0,0], 2:[0,0,0], 3:[0,0,0], 4:[0,0,0], 5:[0,0,0], 6:[0,0,0], 7:[0,0,0], 8:[0,0,0], 9:[0,0,0]}

def track_index(index, value):
    # nr_dict = {nr: [forelast index, last index, count]}
    nr_dict[value][0] = nr_dict[value][1]
    nr_dict[value][1] = index
    nr_dict[value][2] += 1
    return nr_dict[value][0], nr_dict[value][1], nr_dict[value][2],

def step(input, nr):
    track_index()
    if nr in input[:-1]:
        last_pos, prev_pos = track_index()
        input.append(last_pos - prev_pos)
        # input.append(len(input) - input[:-1].count(nr))
    else:
        input.append(input[:-1].count(nr))
    if len(input) == number_spoken:
        print(len(input), ":", input[-1])

