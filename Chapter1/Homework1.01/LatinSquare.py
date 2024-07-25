def print_LatinSquare(square) :
	for i in range(9) :
		for j in range(9) :
			print(square[i][j], end = ' ')
		print()


def canBe_there(square, row, column, number) :
	for y in range(9) :
		if (square[row][y] == number) :
			return False

	for x in range(9) :
		if (square[x][column] == number) :
			return False

	SomewhereInRow = row - (row % 3)
	SomewhereInColumn = column - (column % 3)

	for i in range(3) :
		for j in range(3) :
			if (square[SomewhereInRow + i][SomewhereInColumn + j] == number) :
				return False

	return True


def find_Solution(square, row, column) :
	if ((row == 8) and (column == 9)) :
		return True

	if (column == 9) :
		row += 1
		column = 0

	if (square[row][column] > 0) :
		return find_Solution(square, row, column + 1)

	for number in range(1, 10, 1) :
		if canBe_there(square, row, column, number) :
			square[row][column] = number

			if find_Solution(square, row, column + 1) :
				return True

		square[row][column] = 0

	return False
