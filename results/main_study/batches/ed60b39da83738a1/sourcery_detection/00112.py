import numpy as np


class Solution:
	def fib(self, n: int) -> int:
		def matrix_power(A, n):
			if n == 1:
				return A
			if n % 2 == 0:
				half_power = matrix_power(A, n // 2)
				return np.dot(half_power, half_power)
			else:
				return np.dot(A, matrix_power(A, n - 1))


		def fibonacci_matrix_exponentiation(n):
			if n == 0:
				return 0
			elif n == 1:
				return 1

			matrix = np.array([[1, 1], [1, 0]])

			result_matrix = matrix_power(matrix, n - 1)

			fibonacci_number = result_matrix[0, 0]

			return fibonacci_number
		return fibonacci_matrix_exponentiation(n)
