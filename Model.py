# Model part of MVC Architecture

from sets import Set
from Constants import BOARD_SIZE, MIN_PLAYER, MAX_PLAYER, DIFFICULTY, TIE, \
    INPROGRESS, EMPTY_SQUARE
from Search import MinMaxSearch

# Application specific exception
class TicTacToeException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# Move class used to represent a move in ttt board
class Move(object):
    def __init__(self, row, col, player_id):
        self._rowId = row
        self._colId = col
        self._player_id = player_id
    def getRow(self):
        return self._rowId
    def getColumn(self):
        return self._colId
    def getPlayer(self):
        return self._player_id

# Board class for representing a TicTacToe Board
class Board(object):
    def __init__(self):
        self._board = []
      
    # Reset board for next game
    def reset(self):
        for i in range(0, len(self._board)):
            self._board.remove(self._board[0])
        for i in range(0, BOARD_SIZE):
            row = [0, 0, 0]
            self._board.append(row)
        self._firsttime = True               
               
    # Perform the given move on the current board
    def markSquare(self, move):
        if (move.getRow() >= BOARD_SIZE or move.getColumn() >= BOARD_SIZE):
            raise TicTacToeException("Invalid Row Id")
        elif(move.getPlayer() < MIN_PLAYER or move.getPlayer() > MAX_PLAYER):
            raise TicTacToeException("Invalid Cool Id")
        elif(self._board[move.getRow()][move.getColumn()] != 0):
            raise TicTacToeException("Give Square not empty")        
        self._board[move.getRow()][move.getColumn()] = move.getPlayer()
    
    # Returns MAX_PLAYER, MIN_PLAYER if there is a result and based on winner.
    # Returns TIE if game is tied
    def checkGameOver(self):             
        return (self.checkRowMatch() or self.checkColumnMatch() or self.checkDiagonalMatch() or self.checkForTie())
    
    # Checks if there is winner by checking diagonals
    def checkDiagonalMatch(self):
        # Diagonal from 0,0 to BOARD_SIZE, BOARD_SIZE
        cur_val = -1
        index = 1
        for i in range(0, BOARD_SIZE):            
            if(cur_val == -1):
                cur_val = self._board[i][i]
            elif(cur_val == self._board[i][i] and self._board[i][i] > 0):
                    index += 1
                                        
        if(index == BOARD_SIZE):
            return cur_val
        
        # Diagonal from BOARD_SIZE,0 to 0,BOARD_SIZE
        cur_val = -1
        index = 1
        for j in range(0,BOARD_SIZE):
            i = BOARD_SIZE - 1 - j    
            if(cur_val == -1):
                cur_val = self._board[i][j]
            elif(cur_val == self._board[i][j] and self._board[i][j] > 0):
                    index += 1
                    
        if(index == BOARD_SIZE):
            return cur_val
        
        return False
     
    # Checks if there is winner by checking row
    def checkRowMatch(self):
        for i in range(0, BOARD_SIZE):
            cur_val = -1
            index = 1
            for j in range(0, BOARD_SIZE):                
                if(cur_val == -1):
                    cur_val = self._board[i][j]
                elif(cur_val == self._board[i][j] and self._board[i][j] > 0):
                    index += 1
                    continue
                else:
                    break
                
            if(index == BOARD_SIZE):
                return cur_val
        return False
    
    # Checks if there is winner by checking column     
    def checkColumnMatch(self):
        for j in range(0, BOARD_SIZE): 
            cur_val = -1
            index = 1
            for i in range(0, BOARD_SIZE):      
                if(cur_val == -1):
                    cur_val = self._board[i][j]
                elif(cur_val == self._board[i][j] and self._board[i][j] > 0):
                    index += 1
                    continue
                else:
                    break
                
            if(index == BOARD_SIZE):
                return cur_val
        return False
    
    # Returns TIE if game is already tied, else returns INPROGRESS
    def checkForTie(self):
        if(len(self.getPossibleMoves(MAX_PLAYER)) == 0):
            return TIE
        return INPROGRESS
    
    # Returns all possible moves of current board for the given player
    def getPossibleMoves(self,player_no):
        possibleMoves = Set()
        for i in range(0, BOARD_SIZE):
            for j in range(0, BOARD_SIZE):                
                if(self._board[i][j] == EMPTY_SQUARE):
                    possibleMoves.add(Move(i,j,player_no))
        return possibleMoves
    
    # Generates the best possible move for the agent and displays the updated move
    def playMove(self):
        if(len(self.getPossibleMoves(MAX_PLAYER)) == 0):
            return
        srch = MinMaxSearch()
        # First time takes almost 6 seconds reduce computation
        # using this special handling
        # works only for 3 X 3
        if(self._firsttime and self._board[1][1] == MIN_PLAYER):
            self.markSquare(Move(2,0,MAX_PLAYER))
        elif(self._firsttime):
            self.markSquare(Move(1,1,MAX_PLAYER))
        else:
            self.markSquare(srch.getBestMoveforAgent(self,DIFFICULTY))
        self._firsttime = False
        return True     