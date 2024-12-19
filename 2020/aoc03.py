# Day 3: Toboggan Trajectory
# -----------
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#

trees = [line.rstrip('\n') for line in open("input/aoc03_input.txt")]

def tree_count(xn, yn):
    count1 = 0
    for x in range(0, len(trees), xn):
        y = int(x*yn/xn) % len(trees[0])
        # print(trees[x][y])
        count1 += trees[x][y] == '#'
    return count1

# following a slope of right 3 and down 1, how many trees would you encounter?
print(tree_count(1,3))

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?
count2 = 1
slopes = [[1,1], [1,3], [1,5], [1,7], [2,1]]
for x, y in slopes:
    count2 *= (tree_count(x,y))
print(count2)
