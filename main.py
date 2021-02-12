from madlibs import *
import random
from rockpaperscissors import * 
from tictactoe import *
from sudoku import *
from hangman import *

def welcome():
    clearScreen()
    print ('･:*:･Welcome to the game hub･:*:･\nto choose a game please type in the name\n')
    print ('|madlibs \t|tic tac toe\n|rock paper scissors\n|sudoku \t|hangman')


def gameselection(chosen):
    while chosen == False:
        choice = input('')
        if choice == 'madlibs':
            madlibs()
            chosen = True
            backToGameHub()

        elif choice == 'rock paper scissors':
            rockPaperScissors()
            chosen = True
            backToGameHub()


        elif choice == 'tic tac toe':
            if __name__ == '__main__':
                x_player = ComputerPlayer('X')
                o_player = User('O')
                tic = TicTacToe()
                play(tic, x_player, o_player, print_game=True)
            chosen = True
            backToGameHub()
        
        elif choice == 'sudoku':
            solve(sodokuBoard)
            print_board(sodokuBoard)
            chosen = True
            backToGameHub()

        elif choice == 'hangman':
            hangman()
            chosen = True
            backToGameHub()
            
        else:
            print('Sorry thats not a game we have ●︿●\'')

def clearScreen():
    print(chr(27)+'[2j') 
    print('\033c')
    print('\x1bc')

def backToGameHub():
    input("Press enter to get back to the gamehub!")
    clearScreen()
    welcome()
    gameselection(False)

welcome()
gameselection(False)