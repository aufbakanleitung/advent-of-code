numbers, *boards = open('input/04_input.txt').read().split('\n\n')

numbers = [int(n) for n in numbers.split(',')]
boards = [line.split('\n') for line in boards]
boards = [[list(filter(None, line.split(' '))) for line in board] for board in boards]
boards = [[[[int(nr), False] for nr in line] for line in board] for board in boards]


def mark_board(nr):
    for board in boards:
        for line in board:
            for n in line:
                if n[0] == nr:
                   n[1] = True

def check_row(board):
    for line in board:
        for i, nr in enumerate(line):
            if nr[1] == False:
                break
            if i == 4:
                return True

def check_column(board):
    for col in range(len(board)):
        for linenr, line in enumerate(board):
            if line[col][1] == False:
                break
            elif linenr == 4:
                return True
    return False

done_boards = set()

def test_numbers(boards):
    for nr in numbers:
        mark_board(nr)
        for n, board in enumerate(boards):
            if n in done_boards:
                continue

            if check_column(board):
                if len(done_boards) == len(boards)-1:
                    return nr, board
                done_boards.add(n)

            if check_row(board):
                if len(done_boards) == len(boards)-1:
                    return nr, board
                done_boards.add(n)


def final_score(win_nr, board):
    tot = 0
    for line in board:
        for nr in line:
            if nr[1] == False:
                tot += nr[0]
    print(f"Total: {tot}")
    print(f"Final score: {win_nr * tot}")


win_nr, win_board = test_numbers(boards)
final_score(win_nr, win_board)



