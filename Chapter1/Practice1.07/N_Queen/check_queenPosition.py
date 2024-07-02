def CanBeSheNext(matrix, row, column) :
	for i in range(row) :
		if (matrix[i][column] == 1) :
			return False

	for i, j in zip(range(row, -1, -1), range(column, -1, -1)) :
		if (matrix[i][j] == 1) :
			return False

	for i, j in zip(range(row, -1, -1), range(column, N)) :
		if (matrix[i][j] == 1) :
			return False

	return True
