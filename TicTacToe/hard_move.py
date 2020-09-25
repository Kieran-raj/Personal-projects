import random
import math
from check import *
from get import *

##### Have to look a terminal state

def possible_move(board):
	possibles = []
	for i in board:
		if board[i] == ' ':
			possibles.append(i)
	return possibles


def terminal_state(board):
	if not check_win(board):
		if check_diagonals(board):
			return True
		else:
			return False
			# check_draw(board) # essentially not a win
			# return False

def minimax():
	pass


def best_move():
	bestScore = -math.inf
	bestMove = None
	for move in possible_move(board):
		score = minimax(False, aiPlayer, board)


def get_aiplayer(char):
	return char


def hard_func(board, char):
	print(get_aiplayer(char))
	print(possible_move(board))
	terminal_state(board)
	 