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
    # checks to see if game has been completed

    def __init__(self, board_map):
        self.board_map = board_map
        self.build = SudokuBoard(board_map)

    def start(self):
        self.game_over = False