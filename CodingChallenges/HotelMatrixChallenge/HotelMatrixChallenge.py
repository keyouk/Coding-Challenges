def matrixElementsSum(matrix):
	total_sum = 0
	for x in range(len(matrix) - 1):
		for y in range(len(matrix[x])):
			if matrix[x][y] == 0:
				matrix[x + 1][y] = 0
			else:
				continue
	for x in matrix:
		total_sum += sum(x)

	print total_sum
	return total_sum