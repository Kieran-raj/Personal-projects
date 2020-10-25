import random
from get import *


def medium_func(board, char):
	return if_can_win(board, char)



def if_can_win(board, char):
	y_rowposition = 0
	x_colposition = 0
	x_diposition = 0
	y_diposition = 0
	for i in get_rows(board):
		y_rowposition += 1
		if ' ' in i:
			if i.count(char) == 2:
				win = i.index(' ')
				x_position = win + 1
				i[win] = char
				if ''.join(i) == 3 * char:
					return f'{x_position} {y_rowposition}'
	for j in get_columns(board):
		x_colposition += 1
		if ' ' in j:
			if j.count(char) == 2:
				win = j.index(' ')
				y_position = win + 1
				j[win] = char
				if ''.join(j) == 3 * char:
					return f'{x_colposition} {y_position}'
	for k in get_diagonals(board):
		x_diposition += 1
		if ' ' in k:
			if k.count(char) == 2:
				win = k.index(' ')
				if x_diposition == 1 and win == 0:
					y_diposition = 3
				elif x_diposition == 1 and win == 2:
					x_diposition = 3
					y_diposition = 1
				elif x_diposition == 2 and win == 0:
					x_diposition = 1
					y_diposition = 1
				elif x_diposition == 2 and win == 2:
					x_diposition = 3
					y_diposition = 3
				return f'{x_diposition} {y_diposition}'

	return prevent_win(board)


def prevent_win(board):
	y_rowposition = 0
	x_colposition = 0
	x_diposition = 0
	for i in get_rows(board):
		y_rowposition += 1
		if ' ' in i:
			if i.count('X') == 2 or i.count('O') == 2:
				x_position = i.index(' ') + 1
				return f'{x_position} {y_rowposition}'
	for j in get_columns(board):
		x_colposition += 1
		if ' ' in j:
			if j.count('X') == 2 or j.count('O') == 2:
				y_position = j.index(' ') + 1
				return f'{x_colposition} {y_position}'
	for k in get_diagonals(board):
		x_diposition += 1
		if ' ' in k:
			if k.count('X') == 2 or k.count('O') == 2:
				y_diposition = k.index(' ') + 1
				if board['2 2'] == ' ':
					return f'{x_diposition} {y_diposition}'
				else:
					return f'{x_diposition + 1} {y_diposition}'
	while True:
		move = random.choice(list(board.keys()))
		if board[move] == ' ':
			return move
