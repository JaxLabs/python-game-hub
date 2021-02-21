import argparse
from tkinter import *

BOARDS = ['easy', 'medium', 'hard', 'error']

MARGIN = 20
SIDE = 50  
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


class SudokuBoard(object):
    # builds base board for sudoku

    def __init__(self, board_map):
        self.board = board_map
    
    def __create_board(self, board_map):
        board = []

        #go over every line
        for line in board_map:
            line = line.strip()
            board.append([])

        #go over every character
        for cha in line:
            board[-1].append(int(cha))


        return board

class SudokuGame(object):
    # checks to see if game has been completeds
    def __init__(self, board_map):
        self.board_map = board_map
        self.game_layout = SudokuBoard(board_map)

    def start(self):
        self.game_over = False
        self.layout = []
        for i in range(9):
            self.layout.append([])
            for j in range(9):
                self.layout[i].append(self.game_layout[i][j])

    def win_check(self):
        #check row 
        for row in range(9):
            if not self._check_row(row):
                return False
        #check colum
        for column in range(9):
            if not self._check_colum(column):
                return False
        #check box
        for row in range(3):
            for column in range(3):
                if not self._check_box(row, column):
                    return False
        self.game_over = True
        return True

    def _check_box(self, box):
        return set(box) == set(range(1, 10))

    def _check_row(self, row):
        return self.__check_box(self.puzzle[row])

    def _check_column(self, column):
        return self._check_box(
            [self.layout[row][column] for row in range(9)]
        )

    def __check_square(self, row, column):
        return self.__check_box(
            [
                self.layout[r][c]
                for r in range(row * 3, (row + 1) * 3)
                for c in range(column * 3, (column + 1) * 3)
            ]
        )

class sudokuUI(Frame):
    #draw board in tkiter
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()
    
    def _initUI(self):
        self.parent.title("SUDOKU")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
            width = WIDTH,
            height = HEIGHT
        )
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
            text = 'Clear', #switch out for icon later
            command=self.__clear_answers)
        clear_button.pack(fill=BOTH, side=BOTTOM)

        solve_button = Button(self,
            text = 'Solve',
            command = self._solve_puzzle)
        solve_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_numbers()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def _draw_grid(self):
        #draws sudoku puzzle grid of 9x9 on the canvas 
        for i in range(10):
            color = "black" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)












