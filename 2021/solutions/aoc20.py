# --- Day 20: Trench Map ---
from pprint import pp

algo, image = open('../input/20_input.txt').read().split('\n\n')
image = list(map(list,image.splitlines()))

# TODO: Should be a set()
def load(image):
    im = {}
    for i, y in enumerate(image):
        for j, x in enumerate(y):
            im[(i,j)] = x
    return im


def get_9(im, y,x):
    bit = 0
    for ny in (y-1, y, y+1):
        for nx in (x-1, x, x+1):
            bit <<= 1
            if im.get((ny,nx)) == '#':  bit += 1
    # print(y, x,':', bit)
    return bit
# print(get_9(im, 2, 2))

def enhance(im):
    im2 = {}
    y_min, y_max = min([a[0] for a in im.keys()]), max([a[0] for a in im.keys()])
    x_min, x_max = min([a[1] for a in im.keys()]), max([a[1] for a in im.keys()])

    for y in range(y_min-1, y_max+2):
        for x in range(x_min-1, x_max+2):
            im2[(y,x)] = algo[get_9(im, y, x)]

    return im2

def print_dict(im, spacer=''):  # Render image from dict with y,x coordinates
    y_min,y_max = min([a[0] for a in im.keys()]),max([a[0] for a in im.keys()])
    x_min,x_max = min([a[1] for a in im.keys()]),max([a[1] for a in im.keys()])

    image = [['.'] * (x_max-x_min +1) for _ in range((y_max-y_min + 1))]
    for y,x in im:
        image[y-y_min][x-x_min] = im[(y,x)]

    for line in image:
        print(spacer.join(str(x) for x in line))
    print()

im = load(image)
print("lit:", sum(1 for v in im.values() if v == '#'))
# print_dict(im)
for _ in range(2):
    im = enhance(im)
    print("lit:", sum(1 for v in im.values() if v == '#'))
    # print_dict(im)
