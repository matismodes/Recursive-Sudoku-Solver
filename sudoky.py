"""Time is used optionally to delay each iteration of solution"""
import time

# Python Sudoku Solver by Mateo Ismodes
def print_board(board):
    """Prints Sudoku board from two-dimensional array input"""
    counter = 0
    d_line = "-" * 25
    for row in board:
        row_print = ""
        for value in row:
            value = str(value)
            row_print += value + " "
        row_print_new = "| " + row_print[:6] + "| " + row_print[6:12] + "| " + row_print[12:18] + "|"
        row_print_new = row_print_new.replace("0", " ")
        if counter == 0 or counter == 3 or counter == 6:
            print(d_line)
        print(row_print_new)
        counter += 1
    print(d_line)
    print("")
    print("")
#    time.sleep(.001)

def find_zero(board):
    """Finds next zero value in Sudoku Puzzle"""
    horizontal_length = len(board[0])
    vertical_length = len(board)
    for row in range(0, vertical_length, 1):
        for col in range(0, horizontal_length, 1):
            if board[row][col] == 0:
                return [row, col]
    return False


def is_valid(board, row, col, value):
    """Checks if a value input is valid according to Sudoku rules"""
    if value > 9 or value < 1:
        return False
    value_row = board[row]
    value_col = []
    for m in board:
        value_col += [m[col]]
    if value in value_row:
        return False
    if value in value_col:
        return False
    box_y = 0
    box_x = 0
    if row <= 2:
        box_y = 0
    elif row <= 5:
        box_y = 1
    elif row <= 8:
        box_y = 2
    if col <= 2:
        box_x = 0
    elif col <= 5:
        box_x = 1
    elif col <= 8:
        box_x = 2
    box_list = board[(box_y * 3)][(box_x * 3):((box_x * 3) + 3)] + \
               board[((box_y * 3) + 1)][(box_x * 3):((box_x * 3) + 3)] + \
               board[((box_y * 3) + 2)][(box_x * 3):((box_x * 3) + 3)]
    if value in box_list:
        return False
    return True


def solve(board):
    """Recursive function that attempts to solve all solution paths"""
    if find_zero(board) is False:
        return board

    p_1 = find_zero(board)[0]
    p_2 = find_zero(board)[1]

    for i in range(1, 10, 1):
        if is_valid(board, p_1, p_2, i) is False:
            continue
        
        board[p_1][p_2] = i
        # The print_board function below outputs the current board state for each iteration if desired.
        #print_board(board)
        s = solve(board)
        if s is None:
            continue
        
        return s
    board[p_1][p_2] = 0
    return None




board1 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 2, 6, 0, 0, 5, 0],
          [0, 0, 9, 8, 0, 0, 0, 0, 4],
          [7, 0, 3, 0, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 4, 0, 0, 8, 1],
          [5, 0, 0, 0, 0, 7, 0, 3, 0],
          [0, 5, 0, 0, 0, 9, 2, 4, 0],
          [0, 0, 0, 7, 0, 0, 0, 0, 0],
          [9, 1, 0, 0, 0, 0, 0, 0, 0]]


print_board(board1)

print_board(solve(board1))

