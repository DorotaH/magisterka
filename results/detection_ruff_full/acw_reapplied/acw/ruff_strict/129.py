def magic_square_test(my_matrix):
	iSize = len(my_matrix[0])
	sum_list = []
	sum_list.extend([sum(lines) for lines in my_matrix])
	sum_list.extend(sum(row[col] for row in my_matrix) for col in range(iSize))
	result1 = sum(my_matrix[i][i] for i in range(iSize))
	sum_list.append(result1)
	result2 = sum(my_matrix[i][i] for i in range(iSize - 1, -1, -1))
	sum_list.append(result2)
	return 1 >= len(set(sum_list))
