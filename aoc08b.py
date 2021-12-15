# --- Day 8: Seven Segment Search ---
from pprint import pp
from bidict import bidict

segs = [line.split(" | ") for line in open('input/08_example.txt').read().splitlines()]
seg_list = [[seg.split(' ') for seg in line.split(" | ")] for line in open('input/08_example.txt').read().splitlines()]
numbers = {}

number_list = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
number_str = 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'
req = (set(number_list))
print(req)
number_dict = {'a':8, 'b':6, 'c':8, 'd':7, 'e':4, 'f':9,  'g':7}
def count_letters(seg):
    nr_dict = {}
    nr_tuple_list = []
    nrbidict = bidict()
    for l in 'abcdefg':
        nrbidict = bidict({l: seg.count(l)})
        nr_dict[seg.count(l)] = l
        # nr_dict[l] = seg.count(l)
        # nr_tuple_list.append((l, seg.count(l)))
    return nr_dict, nrbidict
print(count_letters(segs[0][0]))

def run(segs):
    for seg in segs:
        nr_dict, nrbidict = count_letters(seg[0])
        ltr_list = ['.'] * 7
        if nr_dict.values() == 4:  # ee 4
            pass
        if nr_dict.values() == 6:  # bb 1
            print(f"yo")
        if nr_dict.values() == 7:  # d/g  3/6
            pass
        if nr_dict.values() == 8:  # a/c 0/2
            pass
        if nr_dict.values() == 9:  # ff 5
            pass
run(segs)

def pattern(i, line):
    values = {}
    for j, out in enumerate(line[0]):
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
pattern(0,seg_list[0])

# for i, line in enumerate(seg_list):
#     pattern(i, line)