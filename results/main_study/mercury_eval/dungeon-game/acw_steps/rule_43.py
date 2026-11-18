class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # it's dp babee
        
        m = len(dungeon)
        n = len(dungeon[0])
        grid = dungeon
        inf = float('-inf')
        def isPossible(health):
            dp = [[0] * n for _ in range(m)]
            dp[0][0] = grid[0][0] + health
            for r in range(m):
                for c in range(n):
                    if 0 < r and dp[r - 1][c] > 0:
                        dp[r][c] = max(dp[r][c], dp[r - 1][c] + grid[r][c])
                    if 0 < c and 0 < dp[r][c - 1]:
                        dp[r][c] = max(dp[r][c], dp[r][c - 1] + grid[r][c])
            return dp[m - 1][n - 1] > 0
        # print(isPossible(7))
        # print(isPossible(6))
        # print(isPossible(9))
        l = 1
        h = 10**5
        res = h
        while l <= h:
            mid = (l + h) // 2
            if isPossible(mid):
                res = min(res, mid)
                h = mid - 1
            else:
                l = mid + 1
        return res

