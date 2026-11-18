class  Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        m = len(Grid)
        n = len(Grid[0])
        prev=[0]*n
        for  i in  range(m):
            temp=[0]*n
            for  j in  range(n):
                if  1==Grid[i][j]:
                    temp[j]=0
                    continue
                if  0==i and  0==j:
                    temp[j]=1
                    continue
                up = left = 0
                if  i > 0:
                    up=prev[j]
                if  j > 0:
                    left=temp[j-1]
                temp[j]= left+up
            prev=temp
        return prev[n - 1]