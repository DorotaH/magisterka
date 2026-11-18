class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def rotateCoord(c, n):
            x, y = c
            return (y, n - x - 1)

        n = len(matrix)

        for i in range(n // 2):
            for j in range(3):
                for k in range(n - i * 2 - 1):
                    coord0 = (i, i + k)
                    coord1 = coord0
                    for l in range(j + 1):
                        coord1 = rotateCoord(coord1, n)
                    x0, y0 = coord0
                    x1, y1 = coord1
                    matrix[x0][y0], matrix[x1][y1] = matrix[x1][y1], matrix[x0][y0]
                    print(matrix)