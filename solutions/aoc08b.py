# --- Day 8: Seven Segment Search ---
from pprint import pp
from bidict import bidict

segs = [line.split(" | ") for line in open('../input/08_example.txt').read().splitlines()]
seg_list = [[seg.split(' ') for seg in line.split(" | ")] for line in open(
    '../input/08_example.txt').read().splitlines()]
numbers = {}

number_list = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
number_str = 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'
number_dict = {'a':8, 'b':6, 'c':8, 'd':7, 'e':4, 'f':9,  'g':7}

def count_letters(seg):
    nr_dict = {}
    tuples = []
    for l in 'abcdefg':
        # nrbidict = bidict({l: seg.count(l)})
        nr_dict[l] = seg.count(l)
        tuples.append([l, seg.count(l), '??'])
    return tuples

def label_digits(seg, letters):
    nr_dict = count_letters(seg[0])
    for j,nr in enumerate(nr_dict):
        if nr[1] == 4:
            nr_dict[j][2] = 'E'
            letters.remove(nr[0])
        if nr[1] == 6:
            nr_dict[j][2] = 'B'
            letters.remove(nr[0])
        if nr[1] == 7:
            nr_dict[j][2] = 'DG'
        if nr[1] == 8:
            nr_dict[j][2] = 'AC'
        if nr[1] == 9:
            nr_dict[j][2] = 'F'
            letters.remove(nr[0])
    return nr_dict, letters

def pattern(seg):
    line = seg[0].split(' ')
    values = {}
    for j, out in enumerate(line):
        if len(out) == 2: values['1'] = out
        if len(out) == 3: values['7'] = out
        if len(out) == 4: values['4'] = out
        if len(out) == 7: values['8'] = out
    return values

def pop_letter(number, letters):
    letter = ''
    for l in number:
        if l in letters:
            letters.remove(l)
            letter = l
    print(letters)
    return letters, letter

def run(segs):
    for i, seg in enumerate(segs[2:3]):
        letters = ['a','b','c','d','e','f','g']
        values = pattern(seg)
        nr_dict, letters = label_digits(seg, letters)

        letters, l = pop_letter(values['1'], letters)
        nr_dict[ord(l)-97][2] = chr(ord(l)-32)  # convert letter value to position in (ordered) list
        letters, l = pop_letter(values['7'], letters)
        nr_dict[ord(l)-97][2] = chr(ord(l)-32)
        letters, l = pop_letter(values['4'], letters)
        nr_dict[ord(l)-97][2] = chr(ord(l)-32)
        nr_dict[ord(letters[0])-97][2] = chr(ord(letters[0])-32)

        print(letters)
        print(nr_dict)
        print(values)
run(segs)