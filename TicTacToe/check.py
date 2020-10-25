from get import *


def check_input_words(coords):
	words = 0
	for i in coords.split(' '):
		if i.isalpha():
			words += 1
	if words == 0:
		return False
	else:
		return True


def check_input(coords):
	greater_than = 0
	for i in coords.split(' '):
		if int(i) > 3:
			greater_than += 1
	if greater_than == 0:
		return True
	else:
		return False


def check_rows(board):
	correct = 0
	rows = get_rows(board)
	for k in rows:
		row = ''.join(k)
		if row == 'XXX':
			correct += 1
		elif row == 'OOO':
			correct += 1
	if correct == 1:
		return True
	else:
		return False


def check_columns(board):
	correct = 0
	columns = get_columns(board)
	for k in columns:
		column = ''.join(k)
		if column == 'XXX':
			correct += 1
		elif column == 'OOO':
			correct += 1
	if correct == 1:
		return True
	else:
		return False


def check_diagonals(board):
	diagonal1 = ''.join([board['1 3'], board['2 2'], board['3 1']])
	diagonal2 = ''.join([board['1 1'], board['2 2'], board['3 3']])
	if diagonal1 == 'XXX' or diagonal1 == 'OOO':
		return True
	else:
		if diagonal2 == 'XXX' or diagonal2 == 'OOO':
			return True
		else:
			return False


def check_draw(board):
	for i in board:
		if board[i] == ' ':
			return False
	return True


def check_win(board):
	if not check_rows(board):
		if not check_columns(board):
			return False
		else: 
			return True
	else:
		return True