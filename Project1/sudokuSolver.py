import sudokuGenerator
#import pdb

expert = sudokuGenerator.grid


def next(sudoku, row, column, nodes):
	while row < 9:
		while column < 9:
			if sudoku[row][column] == 0:
				nodes.append((row, column))
				sudoku[row][column] += 1
				return row, column
			else:
				column += 1
		row += 1
		column = 0

	return None, None


def check(sudoku, row, column):
	#pdb.set_trace()
	for r in range(9):
		if sudoku[row][column] == sudoku[row][r] and r != column:
			return False

	for c in range(9):
		if sudoku[row][column] == sudoku[c][column] and c != row:
			return False

	for r in range(row//3, row//3 + 3):
		for c in range(column//3, column//3 + 3):
			if (r != row or c != column) and sudoku[row][column] == sudoku[r][c]:
				return False

	return True


def solve(sudoku):
	nodes = []
	i, j = next(sudoku, 0, 0, nodes)

	while True:
		if i == None:
			return sudoku
		if check(sudoku, i, j):
			i, j = next(sudoku, i, j, nodes)
		else:
			if sudoku[i][j] == 9:
				sudoku[i][j] = 0
				del nodes[-1]
				try:
					i, j = nodes[-1]
				except IndexError:
					return None
			else:
				sudoku[i][j] += 1

	print("What")


for t in range(9):
	print(solve(expert)[t])