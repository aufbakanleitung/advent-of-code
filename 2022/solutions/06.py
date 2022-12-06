# --- Day 6: Tuning Trouble ---
data1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
data2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
data3 = "nppdvjthqldpwncqszvftbrmjlhg"
data = open("../input/06i.txt").read()

def tune(data, l):
    for c in range(len(data)):
        if len(set(data[c:c+l])) == l:
            print(c+l)
            break
tune(data, 4)
tune(data, 14)