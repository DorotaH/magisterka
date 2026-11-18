class  Solution:
    def  rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotateCoord(c, n):
            x, y=c
            return (y, n - x - 1)

        n = len(matrix)

        for i in range(0, n // 2):
            for  j in  range(0, 3):
                for k in range(0, n - i * 2 - 1):
                    coord0 = (i, k + i)
                    coord1 = coord0
                    for l in range(0, j + 1):
                        coord1=rotateCoord(coord1, n)
                    x0, y0 = coord0
                    x1, y1 = coord1
                    matrix[x0][y0], matrix[x1][y1] = matrix[x1][y1], matrix[x0][y0]
                    print(matrix)
