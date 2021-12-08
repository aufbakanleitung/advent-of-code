# --- Day 8: Seven Segment Search ---
from pprint import pp

segs = [line.split(" | ") for line in open('input/08_example.txt').read().splitlines()]
seg_list = [[seg.split(' ') for seg in line.split(" | ")] for line in open('input/08_example.txt').read().splitlines()]
numbers = {}

number_list = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
number_str = 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'
number_dict = {'a':8, 'b':6, 'c':8, 'd':7, 'e':4, 'f':9,  'g':7}
def count_letters(seg):
    nr_dict = {}
    for l in 'abcdefg':
        nr_dict[l] = seg.count(l)
    return nr_dict

def get_keys(d, val):
    return [k for k, v in d.items() if v == val]


for seg in segs:
    nr_dict = count_letters(seg[0])
    print(nr_dict)
    if nr_dict.values() == 4: # e
        print(f"e:{get_keys(nr_dict, 4)}")
    if nr_dict.values() == 6: # b
        print(f"b:{get_keys(nr_dict, 6)}")
    if nr_dict.values() == 7: # d/g
        pass
    if nr_dict.values() == 8: # a/c
        pass
    if nr_dict.values() == 9: # f
        pass


def pattern(i, line):
    values = {}
    for j, out in enumerate(line[1]):
        if len(out) == 2:
            # print(f"({i},{j}) nr 1: {out}")
            numbers[i,j] = '1'
            values['1'] = out
        if len(out) == 3:
            # print(f"({i},{j}) nr 7: {out}")
            numbers[i,j] = '7'
            values['7'] = out
        if len(out) == 4:
            # print(f"({i},{j}) nr 4: {out}")
            numbers[i,j] = '4'
            values['4'] = out
        if len(out) == 7:
            # print(f"({i},{j}) nr 8: {out}")
            numbers[i,j] = '8'
            values['8'] = out
    print(values)


for i, line in enumerate(seg_list):
    pattern(i, line)