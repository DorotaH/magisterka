class  Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # it's dp babee
        
        m, n = len(dungeon), len(dungeon[0])
        grid, inf = dungeon, float('-inf')
        def isPossible(health):
            dp = []
            for _ in range(m):
                dp.append([0] * n)
            dp[0][0]=health+grid[0][0]
            for r in range(m):
                for c in range(n):
                    if r > 0 and dp[r - 1][c] > 0:
                        dp[r][c]=max(dp[r][c], dp[r-1][c]+grid[r][c])
                    if c > 0 and dp[r][c - 1] > 0:
                        dp[r][c]=max(dp[r][c], dp[r][c-1]+grid[r][c])
            return dp[m-1][n-1]>0
        # print(isPossible(7))
        # print(isPossible(6))
        # print(isPossible(9))
        l, h = 1, 10**5
        res = h
        while  l<=h:
            mid=(h+l)//2
            if not isPossible(mid):
                l=mid+1
            else:
                res = min(res,mid)
                h=mid-1
        return  res
            