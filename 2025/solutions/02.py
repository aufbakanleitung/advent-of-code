# --- Day 2: Gift Shop ---
idlist = [list(map(int, range.split("-"))) for range in open('../input/02.txt').read().split(",")]
nrs = [id for ids in idlist for id in range(ids[0], ids[1]+1)]

def repeating(nr):
    id_str = str(nr)
    if len(id_str) % 2 == 0 and id_str[0:len(id_str)//2] == id_str[len(id_str)//2:]:
        return True

# --- Part Two ---
def repeating_v2(nr):
    id_str = str(nr)
    length = len(id_str)
    for size in range(1, length // 2 + 1):
        if length % size == 0:
            if all(id_str[i:i+size] == id_str[i+size:i+2*size] for i in range(0, length - size, size)):
                return True
    return False

total = 0
for nr in nrs:
    if repeating_v2(nr):
        total += nr

print(total)