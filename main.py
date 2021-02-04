import random
from rockpaperscissors import * 

def welcome():
    clearScreen()
    print ('･:*:･Welcome to the game hub･:*:･\nto choose a game please type in the name\n')
    print ('|madlibs \t|tic tac toe\n|rock paper scissors\n|sudoku \t|hangman')


def gameselection(chosen):
    while chosen == False:
        choice = input('')
        if choice == 'madlibs':
            print('madlibs!')

        elif choice == 'rock paper scissors':
            rockPaperScissors()
            chosen = True
            backToGameHub()


        elif choice == 'tic tac toe':
            print("tic tac toe!")
            chosen = True
            backToGameHub()
        
        elif choice == 'sudoku':
            print("sudoku!")
            chosen = True
            backToGameHub()

        elif choice == 'hangman':
            print("hangman!")
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