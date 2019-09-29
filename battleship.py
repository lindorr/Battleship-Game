#Based off of CodeAcademy
from random import randint

board = []

def print_board(board):
    for row in board:
        print (" ".join(row))

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

for x in range(0, 5):
    board.append(["O"] * 5)
ship_row = random_row(board)
ship_col = random_col(board)

while True:
    print_board(board)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row==ship_row and guess_col==ship_col:
        print("Congratulations! you sank my battleship")
        break

    elif (guess_row not in range (6) or guess_col not in range (6)):
        print ("Oops, that's not even in the ocean")
    elif (guess_row != ship_row or guess_col != ship_col):
        board [guess_row-1][guess_col-1]= 'X'
        print("You missed my battleship")
    elif (board[guess_row-1][guess_col-1]=='X'):
        print ("you guessed that one already")
