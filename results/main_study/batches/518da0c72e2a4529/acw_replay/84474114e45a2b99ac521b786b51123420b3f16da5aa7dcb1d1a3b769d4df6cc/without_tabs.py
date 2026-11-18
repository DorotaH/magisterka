class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        m = len(Grid)
        n = len(Grid[0])
        prev = [0] * n
        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if Grid[i][j] == 1:
                    temp[j] = 0
                    continue
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                up = 0
                left = 0
                if i > 0:
                    up = prev[j]
                if 0 < j:
                    left = temp[j - 1]
                temp[j] = up + left
            prev = temp
        return prev[n - 1]
