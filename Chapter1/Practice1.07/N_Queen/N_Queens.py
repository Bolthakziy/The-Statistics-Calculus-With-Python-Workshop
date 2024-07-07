def print_chessBoard(board, number) :
	for i in range(number) :
		for j in range(number) :
			print(board[i][j], end = ' ')
		print()


def canBe_QueenThere(board, row, column, number) :
	for i in range(row) :
		if (board[i][column] == 1) :
			return False

	for i, j in zip(range(row, -1, -1), range(column, -1, -1)) :
		if (board[i][j] == 1) :
			return False

	for i, j in zip(range(row, -1, -1), range(column, number, 1)) :
		if (board[i][j] == 1) :
			return False

	return True


def find_Solution(board, row, number) :
	if (row >= number) :
		return True

	for i in range(number) :
		if (canBe_QueenThere(board, row, i, number)) :
			board[row][i] = 1

			if (find_Solution(board, row + 1, number) == True) :
				return True

			board[row][i] = 0

	return False
