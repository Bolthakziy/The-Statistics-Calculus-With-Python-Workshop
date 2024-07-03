def find_solution(matrix, row) :
	if (row == N) :
		return True

	for i in range(N) :
		if (CanBeSheNext(matrix, row, i) :
			matrix[row][i] = 1

		lastPhaseMatrix = find_solution(matrix, row + 1)

		if lastPhaseMatrix :
			return True

		matrix[row][i] = 0

	return False
