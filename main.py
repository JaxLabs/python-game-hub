def welcome():
    print(chr(27)+'[2j') #to clear the screen
    print('\033c')
    print('\x1bc')

    print ('･:*:･Welcome to the game hub･:*:･\nto choose a game please type in the name\n')
    print ('|madlibs \t|tic tac toe\n|rock paper scissors\n|sudoku \t|hangman')


def gameselection(chosen):
    while chosen == False:
        choice = input('')
        if choice == 'madlibs':
            print('madlibs!')

        elif choice == 'rock paper scissors':
            print('rock paper scissors!')

        elif choice == 'tic tac toe':
            print("tic tac toe!")
        
        elif choice == 'sudoku':
            print("sudoku!")
        
        elif choice == 'hangman':
            print("hangman!")
        else:
            print('Sorry thats not a game we have ●︿●')


welcome()
gameselection(False)