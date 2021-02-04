import random
def rockPaperScissors():

    print("Rules: rock smashes scissors, paper covers rock, scissors cuts paper.\ninput 'r' for rock 'p' for paper or 's' for scissors\n")

    player = input("your choice: ")
    computer = random.choice(['r', 'p', 's'])

    player = player.lower()
    print("opponent choice: " + computer)

    if player == computer:
        print ("\nIt's a tie.")

    #Rock
    elif player == 'r' and computer == 'p':
        print ("\nOpponent wins.")

    elif player == 'r' and computer == 's':
        print ("\nYou win!")

    #Scissors
    elif player == 's' and computer == 'r':
        print ("\nOpponent wins.")

    elif player == 's' and computer == 'p':
        print ("\nYou win!")

    #Paper
    elif player == 'p' and computer == 'r':
        print ("\nYou win!")

    elif player == 'p' and computer == 's':
        print ("\nOpponent wins.")


