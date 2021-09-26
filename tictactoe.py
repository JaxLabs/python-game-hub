import math
import random
class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class User(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        grid = {'a1':0, 'b1':1, 'c1':2, 'a2':3, 'b2':4, 'c2':5, 'a3':6, 'b3':7, 'c3':8}
        valid_square = False
        val = None
        while not valid_square:
            selection = input('Input a move! colum then row (e.g.:a3): ')
            square = grid.get(selection)

            try: #checking for invalid move
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        rows = 1
        print('   ' + 'a'+ '   '+'b' + '   ' + 'c')
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            
            print(str(rows) + '| ' + ' | '.join(row) + ' |')
            rows += 1

    def make_move(self, square, letter): #showing move on board
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #check rows
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        #check columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([l == letter for l in column]):
            return True
        #check both diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([l == letter for l in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([l == letter for l in diagonal2]):
                return True
        #no winner
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:

                    print(letter + ' wins!')

                return 0 
            letter = 'O' if letter == 'X' else 'X'  # Makes turns

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = ComputerPlayer('X')
    o_player = User('O')
    tic = TicTacToe()
    play(tic, x_player, o_player, print_game=True)