# --- Day 4: Camp Cleanup ---
pairs = [items.split(',') for items in open('../input/04i.txt').read().splitlines()]
pairs = [[list(map(int, item.split('-'))) for item in items] for items in pairs]

pl = []
for pair in pairs:
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        pl.append(pair)
    elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        pl.append(pair)

print("4a: redundant pairs:  ", len(pl))

# --- Day 4b ---
ol = []
for pair in pairs:
    if pair[0][1] >= pair[1][0] and pair[0][0] <= pair[1][1]:
        ol.append(pair)
    elif pair[0][1] <= pair[1][0] and pair[0][0] >= pair[1][1]:  # somehow no effect
        ol.append(pair)

print("4b: overlapping pairs:", len(ol))
