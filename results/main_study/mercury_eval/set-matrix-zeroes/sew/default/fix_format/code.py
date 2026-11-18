class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import numpy as np

        has_zero_row, has_zero_col = (
            np.full(len(matrix), False),
            np.full(len(matrix[0]), False),
        )
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    has_zero_col[j] = True
                    has_zero_row[i] = True
        for i in range(len(has_zero_row)):
            if has_zero_row[i]:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(len(has_zero_col)):
            if has_zero_col[j]:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
