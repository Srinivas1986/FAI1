from Constants import EMPTY, PLAYER_1, PLAYER_2
from Model import BOARD_SIZE

# Function to print a Tic Tac Toe board 
# View part of MVC Architecture
def printBoard(board):
    for i in range(0, BOARD_SIZE):
        row = board._board[i]
        row_text = ""
        for square in row:
            text = EMPTY
            if (square == 1):
                text = PLAYER_1
            elif (square == 2):
                text = PLAYER_2
            row_text += (text + " ")
        print(row_text)
        
            
