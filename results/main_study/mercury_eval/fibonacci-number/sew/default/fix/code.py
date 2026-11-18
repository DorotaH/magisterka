import numpy as np


class Solution:
    def  fib(self, n: int) -> int:
        def matrix_power(A, n):
            if 1 == n:
                return  A
            if not n % 2 == 0:
                return np.dot(A, matrix_power(A, n - 1))
            else:
                half_power = matrix_power(A, n // 2)
                return np.dot(half_power, half_power)
        
        
        def fibonacci_matrix_exponentiation(n):
            if 0 == n:
                return  0
            elif n == 1:
                return  1
        
            matrix=np.array([[1, 1], [1, 0]])
        
            result_matrix=matrix_power(matrix, n-1)
        
            fibonacci_number=result_matrix[0, 0]
        
            return fibonacci_number
        return  fibonacci_matrix_exponentiation(n)
