import pprint

def solve(board):
    # solves sudoku using a backtracking technique
    # preconditions: list of ints making up the board
    # postconditions: solved sudoku board

    find = find_empty(board)
    if find:
        row,col = find
    else:
        return True
    
    for i in range(1,10):
        if vaid(board, (row, col), i):
            board[row][col] = 1

            if solve(board):
                return True
            
            board[row][col] = 0

    return False


def valid(board, pos, num):
    # checks if a move is valid on the board
    # preconditions: list of ints from the board, 
    # the position consisting of the row,
    # and the colum, and the range of numbers
    # postconditions: returns bool value

    #row
    for i in range(0, len(board)):
        if board[0][i] == num and pos[i] != i:
            return False

    #colum 
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, (box_y*3 + 3)):
        for j in range(box_x*3, (box_x*3 +3)):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def find_empty(board):
    # finds an empty space on the board
    # preconditions: the layout of the board
    # postconditions: returns row and colum in int form

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]  == 0:
                return (i, j)

def print_board(board):
    # prints out board to the consol
    # preconditions: the list of numbers on the board
    # postconditions: returns nothing and shows board on screen

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - -')
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(' | ', end = '')

                if j == 8:
                    print(board[i][j], end='\n')
                else:
                    print(str(board[i][j]) + ' ', end='')
                
sodokuBoard = [
                [7, 8, 0, 4, 0, 0, 1, 2, 0],
                [6, 0, 0, 0, 7, 5, 0, 0, 9],
                [0, 0, 0, 6, 0, 1, 0, 7, 8],
                [0, 0, 7, 0, 4, 0, 2, 6, 0],
                [0, 0, 1, 0, 5, 0, 9, 3, 0],
                [9, 0, 4, 0, 6, 0, 0, 0, 5],
                [0, 7, 0, 3, 0, 0, 0, 1, 2],
                [1, 2, 0, 0, 0, 7, 4, 0, 0],
                [0, 4, 9, 2, 0, 6, 0, 0, 7] 
            ]

pp = pprint.PrettyPrinter(width = 41, compact = True)
solve(sodokuBoard)
pp.pprint(sodokuBoard)

