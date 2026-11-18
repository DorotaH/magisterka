class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        for o in range(0, 1 + min(m, n) // 2):
            left = o
            right = n - o - 1
            up = o
            down = m - o - 1
            print(left, right, up, down)
            if down < up or left > right:
                continue
            # if up == down and left == right:
            #    res.append(matrix[up][left])
            #    continue
            res.extend(matrix[up][j] for j in range(left, right))
            if up == down:
                res.append(matrix[up][right])
                continue
            res.extend(matrix[i][right] for i in range(up, down))
            if left == right:
                res.append(matrix[down][right])
                continue
            res.extend(matrix[down][j] for j in range(right, left, -1))
            res.extend(matrix[i][left] for i in range(down, up, -1))
        return res
