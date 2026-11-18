class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = list()
        for o in range(min(m, n) // 2 + 1):
            left = o
            right = n - o - 1
            up = o
            down = m - o - 1
            print(left, right, up, down)
            if up > down or left > right:
                continue
            # if up == down and left == right:
            #    res.append(matrix[up][left])
            #    continue
            for j in range(left, right):
                res.append(matrix[up][j])
            if down == up:
                res.append(matrix[up][right])
                continue
            for i in range(up, down):
                res.append(matrix[i][right])
            if left == right:
                res.append(matrix[down][right])
                continue
            for j in range(right, left, -1):
                res.append(matrix[down][j])
            for i in range(down, up, -1):
                res.append(matrix[i][left])
        return res
