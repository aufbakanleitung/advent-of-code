from pprint import pprint
grid = [items.strip() for items in open('../input/03.txt').read().splitlines()]

def part_1(grid):
    symbols = []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "." or ch.isdigit():
                continue
            symbols.append((r,c))
            # print(ch, end="")
    # print("Symbol coordinates:", symbols)

    numbers = set()
    for r,c in symbols:
        for cr in [r-1, r, r+1]:
            for cc in [c-1, c, c+1]:
                # get the digits adjacent to a symbol
                if cr < 0 or cr >= len(row) or cc < 0 or cc >= len(grid) or not grid[cr][cc].isdigit():
                    continue
                # acquire the first digit of each number, in a set to avoid duplicates
                while cc > 0 and grid[cr][cc -1].isdigit():
                    cc -= 1
                numbers.add((cr,cc))
    # print("Number coordinates:", numbers)

    sum = 0
    for r,c in numbers:
        s = ""
        while c < len(grid[r]) and grid[r][c].isdigit():
            s += grid[r][c]
            c += 1
        sum += int(s)
    return sum
print("Part 1:", part_1(grid))

def part_2(grid):
    symbols = []
    for r,row in enumerate(grid):
        for c,ch in enumerate(row):
            if ch != "*":
                continue
            symbols.append((r,c))

    tot = 0
    for r, c in symbols:
        numbers = set()
        for cr in [r-1,r,r+1]:
            for cc in [c-1,c,c+1]:
                # get the digits adjacent to *
                if cr < 0 or cr >= len(row) or cc < 0 or cc >= len(grid) or not grid[cr][cc].isdigit():
                    continue
                # acquire the first digit of each number
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -= 1
                numbers.add((cr,cc))
        # print("Number coordinates", numbers, len(numbers))

        if len(numbers) == 1:
            continue
        prod = 1
        for r,c in numbers:
            s = ""
            while c < len(grid[r]) and grid[r][c].isdigit():
                s += grid[r][c]
                c += 1
            prod *= int(s)
        tot += prod
    return tot
print("Part 2:", part_2(grid))