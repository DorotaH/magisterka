class  Solution:
     def uniquePathsWithObstacles(self, obstacleGrid):
         """
         :type obstacleGrid: List[List[int]]
         :rtype: int
         """
         m = len(obstacleGrid) #row
         n = len(obstacleGrid[0]) #col
         path = [[0 for  j in  range(n)] for  i in  range(m)]
         for  i in  range(m):
             if not obstacleGrid[i][0] == 0:
                 break
             else:
                 path[i][0] = 1
         for  i in  range(n):
             if not obstacleGrid[0][i] == 0:
                 break
             else:
                 path[0][i] = 1
         for  i in  range(1,m):
             for  j in  range(1,n):
                 if not obstacleGrid[i][j] != 1:
                     path[i][j] = 0
                 else:
                     path[i][j] = path[i-1][j] + path[i][j-1]
         return  path[m-1][n-1]
