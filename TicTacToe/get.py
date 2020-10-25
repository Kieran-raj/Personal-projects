def get_rows(board):
	current = []
	rows = []
	for i in range(1, 4):
		for j in board:
			if j.startswith(f'{i}'):
				current.append(board[j])
	rows.append(current[::3])
	rows.append(current[1::3])
	rows.append(current[2::3])
	return rows


def get_columns(board):
	current = []
	columns =[]
	for i in range(1, 4):
		for j in board:
			if j.endswith(f'{i}'):
				current.append(board[j])
	columns.append(current[::3])
	columns.append(current[1::3])
	columns.append(current[2::3])
	return columns


def get_diagonals(board):
	diagonals = []
	diagonal1 = [board['1 3'], board['2 2'], board['3 1']]
	diagonal2 = [board['1 1'], board['2 2'], board['3 3']]
	diagonals.append(diagonal1)
	diagonals.append(diagonal2)
	return diagonals
