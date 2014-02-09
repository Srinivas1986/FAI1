import copy

from Constants import NEUTRAL, MAX_PLAYER, WINNING, MIN_PLAYER, LOSING, \
    MIN_DEFAULT, MAX_DEFAULT

# Represents the Result Object of a MINMAX search
class Result(object):
    def __init__ (self,score,move):
        self._score = score
        self._move = move

    def setMove(self,move):        
        self._move = move
    
    def getMove(self):
        return self._move
    
    def getScore(self):
        return self._score

# Node class representing every node in MinMax Tree
class Node(object):
    def __init__(self,board,move,depth,playerToMove):
        if (playerToMove == MAX_PLAYER):
            self._score = LOSING
        else:
            self._score = WINNING
        self._move = copy.deepcopy(move)
        self.children = []
        self.initializeScoreAndChildren(playerToMove,board,depth)
    
    # Handle childern and generate score of every node
    def initializeScoreAndChildren(self,playerToMove,board,depth):
        # If one player has already won no need to find children
        # any more. We can directly update score based on that
        winner = board.checkGameOver()
        if(winner == MAX_PLAYER):
            # Adding depth ensures that Agent will pick a faster win
            self._score = WINNING + depth
            return
        elif(winner == MIN_PLAYER):
            # Subtracting depth ensures that Agent will pick a slow death
            self._score = LOSING - depth
            return
        
        # only find moves till given depth for reducing time
        moves = board.getPossibleMoves(playerToMove)
        if(depth == 0 or len(moves) == 0):
            self._score = NEUTRAL 
            return
        
        # Create a child node for all possible moves  
        for m in moves:            
            newBoard = copy.deepcopy(board)            
            newBoard.markSquare(m)
            playerToMoveNxt = MIN_PLAYER if (playerToMove == MAX_PLAYER) else MAX_PLAYER
            child = Node(newBoard,m,depth-1,playerToMoveNxt)            
            self.addChild(child)
        
    # Add child node to current node
    def addChild(self,child):
        self.children.append(child)
    
    # Returns current board in the current node  
    def getBoard(self):
        return self._board
    
    # Returns the score calculated for the given Node
    def getScore(self):
        return self._score      

# Implements the min max search algorithm  
class MinMaxSearch(object):
    # Returns best move for agent for any given board
    def getBestMoveforAgent(self,board,depth):
        moves = []        
        node = Node(board,moves,depth,MAX_PLAYER)
        result = self.findBestMove(node, True)
        return result.getMove()
    
    # Returns best possible move for the given player at any instant
    def findBestMove(self,node,maxPlayer):          
        if(maxPlayer):        
            bestVal = MIN_DEFAULT
            final_result = Result(node.getScore(),node._move)          
            # Max value of child will be this nodes score
            for child in node.children:
                
                result = self.findBestMove(child,False)
                if(result.getScore() > bestVal):
                    bestVal = result.getScore()
                    final_result._score = bestVal
                    final_result.setMove(child._move)
            return final_result
        else:
            bestVal = MAX_DEFAULT
            final_result = Result(node.getScore(),node._move)
            # Min value of child will be this nodes score            
            for child in node.children:
                result = self.findBestMove(child,True)
                if(result.getScore() < bestVal):
                    bestVal = result.getScore()
                    final_result._score = bestVal
                    final_result.setMove(child._move)
            return final_result
            
             
        
        
