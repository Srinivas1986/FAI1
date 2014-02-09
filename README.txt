1.How to run Tic-Tac-Toe?
Running the Control.py will trigger the TicTacToe application.
Ensure all the files listed below are present
When all files are in current directory
eg: python Control.py

Board is printed in console with input also read from console
You need to enter row and column number when player is supposed to move.
The program will prompt for inputs.
All rows and column indexes start from 0.

File	 		Description
Constants.py 	All constants and error codes required for the TicTacToe are all defined here
View.py			Display logic for the TicTacToe board.(Uses DataModel from Model.py)
Model.py		Data Model of the TicTacToeboard, Move object used for representing moves
Control.py 		Starting point of execution, controls objects in both View.py and Model.py
Search.py		Core logic which uses MinMaxSearch for finding optimal move
