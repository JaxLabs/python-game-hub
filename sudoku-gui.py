import argparse
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

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
        for i in xrange(9):
            self.layout.append([])
            for j in xrange(9):
                self.layout[i].append(self.game_layout[i][j])

    def win_check(self):
        #check row 
        for row in xrange(9):
            if not self._check_row(row):
                return False
        #check colum
        for column in xrange(3):
            if not self._check_colum(colum):
                return False
        #check box
        for row in xrange(3):
            for coulum in xrange(3):
                if not self._check_box(row, colum):
                    return False
        self.game_over = True
        return True

    def _check_box(self, box):
        return set(box) == set(range(1, 10))

    def _check_row(self, row):
        return self.__check_box(self.puzzle[row])

    def _check_column(self, row, column):
        return self._check_box(
            [self.layout[row][column] for row in xrange(9)]
        )

    def __check_square(self, row, column):
        return self.__check_box(
            [
                self.layout[r][c]
                for r in xrange(row * 3, (row + 1) * 3)
                for c in xrange(column * 3, (column + 1) * 3)
            ]
        )














