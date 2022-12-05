# --- Day 5: Supply Stacks ---
import re

st = [['Z','N'],
      ['M','C','D'],
      ['P']]
mv = [[1,2,1],
     [3,1,3],
     [2,2,1],
     [1,1,2]]


moves = [list(map(int, re.findall('[0-9]+', line))) for line in open('../input/05moves.txt').read().splitlines()]
stack = [re.findall('[A-Z]', line) for line in open('../input/05trans_crates.txt').read().splitlines()]

def crate9000(moves, st):
    for m in moves:
        for _ in range(m[0]):
            st[m[2]-1].append(st[m[1]-1].pop())
    print("Crate9000: ",end='')
    for i in st:
        print(i[-1], end='')

crate9000(moves,stack)



def crate9001(moves, st):
    for m in moves:
        substack = st[m[1]-1][-m[0]:]
        for i in range(len(substack)):
            st[m[2]-1].append(substack[i])
        del st[m[1]-1][-m[0]:]
    print("\nCrate9001: ",end='')
    for i in st:
        print(i[-1], end='')
crate9001(moves,stack)