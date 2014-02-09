# Control part of MVC Architecture

import random

from Constants import PLAYER_WIN, TIE, AGENT_WIN, MIN_PLAYER, MAX_PLAYER, \
    INPUT_ERROR, INPROGRESS
from Model import Board, Move, TicTacToeException
from View import printBoard
import datetime as dt


# For a given board gets move from player 
# PLAYER_WIN or a  TIE , INPUT_ERROR
def getMoveFromPlayer(board):
    try:
        row = int(raw_input("Enter your move : Row No     (0-2)"))            
        col = int(raw_input("Enter your move : Column No  (0-2)"))
        board.markSquare(Move(row,col,MIN_PLAYER))
    except TicTacToeException as ttte:
        print(ttte)
        return INPUT_ERROR
    except :
        print("Invalid Entry Please try again")
        return INPUT_ERROR     
    
    print("Board after your move")
    printBoard(board)
    result = board.checkGameOver()
    if(MIN_PLAYER == result):        
        return PLAYER_WIN
    elif(TIE == result):        
        return TIE
    return INPROGRESS

# For a given boards get move from agent 
# AGENT_WIN or a  TIE
def getMoveFromAgent(board):
      
    n1=dt.datetime.now()
    board.playMove()
    n2=dt.datetime.now()
    print("Time for move:" + `((n2-n1).seconds)`)
        
    print("Board after Agent move")
    printBoard(board)
    
    result = board.checkGameOver()
    if(MAX_PLAYER == result):        
        return AGENT_WIN
    elif(TIE == result):       
        return TIE
    return INPROGRESS

# Takes the player who will start the game and return
# PLAYER_WIN , AGENT_WIN or a  TIE
def newGame(startplayer):
    board = Board()
    board.reset()
    printBoard(board)
    
    #If game is to be started by Agent    
    if(MAX_PLAYER == startplayer):
        result = getMoveFromAgent(board)
        if(MAX_PLAYER == result):        
            return AGENT_WIN
        elif(TIE == result):       
            return TIE        
    
    # Continues till the game is complete
    # Loops getting player input and agent input moves
    while(1):  
        result = getMoveFromPlayer(board)
        if(MIN_PLAYER == result):            
            return PLAYER_WIN
        elif(TIE == result):            
            return TIE
        elif(INPUT_ERROR == result):
            continue
        
        result = getMoveFromAgent(board)
        if(MAX_PLAYER == result):        
            return AGENT_WIN
        elif(TIE == result):       
            return TIE
        
# Main function 
# Loops until player quits(Multiple games allowed
# Chooses an Arbitrary start player and starts a game
# Maintains count of wins and Losses
def start():
    player = 0
    agent = 0
    tie = 0
    play = True   
    
    while(play):
        print("Player : " + `player` + "    " + "Agent:" + `agent` + "    " + "Tie:" + `tie`)
        startplayer = random.randrange(MIN_PLAYER,MAX_PLAYER+1)
        
        if (startplayer == MAX_PLAYER):
            print("Agent starts")
        else:
            print("Player starts")
           
        result = newGame(startplayer)
        if(result == PLAYER_WIN):
            print("Player Wins")
            player += 1
        elif (result == AGENT_WIN):
            print("Agent Wins")
            agent += 1
        elif(result == TIE):
            print("Tie")
            tie += 1
        play = input ("1 to play another game 0 to quit")
    print("Final Result")
    print("Player : " + `player` + "    " + "Agent:" + `agent` + "    " + "Tie:" + `tie`)
    
start()
    
        