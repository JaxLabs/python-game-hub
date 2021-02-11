import random
import string

def readFile(file):
        fileObj = open(file, "r")
        words = fileObj.read().splitlines() #turns words into an array
        fileObj.close()
        return words

def hangman():
    words = readFile("words.txt")
    word = random.choice(words)
    letters = set(word.upper)
    choices = set(string.ascii_uppercase) #the alphabet
    usedLetters = set() #for seeing what has already been picked


    wizard = "(∩ ͡° ͜ʖ ͡°)⊃━☆"
    spell = "･ﾟ✧" #if game is lost should be output 6 times
    manAlive = "/(°□°)/"
    manDead = "/(╥﹏╥)/"

    


