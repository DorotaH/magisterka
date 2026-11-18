class Solution:

    def traverse(self, x: int, y: int, xt: int, yt: int, dp: List[List[int]]) -> int:

        if x == xt and y == yt:
            return 1
        elif x > xt or y > yt:
            return 0
        elif dp[x][y] != -1:
            return dp[x][y]
        else:
            dp[x][y] = self.traverse(x+1, y, xt, yt, dp) + self.traverse(x, y+1, xt, yt, dp)
            return dp[x][y]


    def uniquePaths(self, m: int, n: int) -> int:
        rx = m-1
        ry = n-1
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        num = self.traverse(0, 0, rx, ry, dp)
        return num if m == 1 and n == 1 else dp[0][0]
        