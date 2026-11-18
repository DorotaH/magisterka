class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        total = n**2
        count = 1
        startingrow = 0
        endingrow = n - 1
        startingcol = 0
        endingcol = n - 1

        ans = [[0 for _ in range(n)] for _ in range(n)]

        while count <= total:
            for i in range(startingcol, endingcol + 1):
                ans[startingrow][i] = count
                count += 1
            startingrow += 1

            for i in range(startingrow, endingrow + 1):
                ans[i][endingcol] = count
                count += 1
            endingcol -= 1

            for i in range(endingcol, startingcol - 1, -1):
                ans[endingrow][i] = count
                count += 1
            endingrow -= 1

            for i in range(endingrow, startingrow - 1, -1):
                ans[i][startingcol] = count
                count += 1
            startingcol += 1
        return ans
