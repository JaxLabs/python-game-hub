import random
import string

def readFile(file):
        fileObj = open(file, "r")
        words = fileObj.read().splitlines() #turns words into an array
        fileObj.close()
        return words

def clearScreen():
    print(chr(27)+'[2j') 
    print('\033c')
    print('\x1bc')

def hangman():
    words = readFile("words.txt")
    word = random.choice(words).upper()
    wordsLetters = set(word)
    choices = set(string.ascii_uppercase) #the alphabet
    usedLetters = set() #for calculating what has already been picked
    usedLettersShown = set() # for seeing what has already been picked
    trys = 6

    wizard = "(∩ ͡° ͜ʖ ͡°)⊃━☆"
    spell = "･ﾟ✧" #if game is lost should be output 6 times
    manAlive = "/(°□°)/"
    
    
    while trys > 0:
        #instructions
        clearScreen()
        print("Guess the word before the wizards spell reaches you.","You have", trys, "trys left")

        #wizard animation
        print(wizard, end = '')
        if trys%6 > 0:
            for x in range((6 - trys%6)):
                print(spell, end = '')
            for x in range(5 - (6 - trys%6)):
                print('   ', end = '')
        else:
            for x in range(7):
                print('   ', end = '')
        
        print(manAlive)




        #word preview
        word_list = [letter if letter in usedLetters else '_' for letter in word]
        print('Current word:', ' '.join(word_list))
        
        #list of already guessed letters
        print("alredy tried:", ' '.join(usedLettersShown))

        #guessing input
        curentLetter = input("choose a letter: ").upper()
        if curentLetter in choices - usedLetters:
            usedLetters.add(curentLetter)
            usedLettersShown.add(curentLetter)
            if curentLetter in wordsLetters:
                wordsLetters.remove(curentLetter)
                usedLettersShown.remove(curentLetter)
                print('')

            else:
                trys = trys - 1  # takes away a life if wrong

        elif curentLetter in choices:
            print('')

        else:
            print('')

        if trys == 0:
            print("Aw you've lost... the word was", word)
        else:
            print("You've won!!")


