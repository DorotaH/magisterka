class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        
        for i in range(n):
            for j in range(0, m):
                matrix[i][j]=int(matrix[i][j])
        
        ans = 0
        for i in range(n):
            dp=list()
            for k in range(i, -1, -1):
                if not dp or dp[-1] == 1:
                    dp.append(matrix[k][0])
                    if dp[-1] == 1:
                        ans = max(ans, i-k+1)
                else:
                    dp.append(0)
            dp.reverse()
            for j in range(1, m):
                valid=True
                for  k in  range(i, -1, -1):
                    if 0 == matrix[k][j]:
                        valid=False
                        
                    if not valid:
                        dp[k] = 0
                    else:
                        ans = max(ans, (1 + dp[k]) * (i-k+1))
                        dp[k] = 1 + dp[k]
        return ans
                    
                
                
