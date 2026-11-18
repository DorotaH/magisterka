class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        total = n * n
        count = 1
        startingrow = 0
        endingrow = n - 1
        startingcol = 0
        endingcol = n - 1

        ans = []
        for _ in range(n):
            ans.append([0 for _ in range(n)])

        while count <= total:
            for i in range(startingcol, 1 + endingcol):
                ans[startingrow][i] = count
                count = count + 1
            startingrow = startingrow + 1

            for i in range(startingrow, 1 + endingrow):
                ans[i][endingcol] = count
                count = count + 1
            endingcol = endingcol - 1

            for i in range(endingcol, startingcol - 1, -1):
                ans[endingrow][i] = count
                count = count + 1
            endingrow = endingrow - 1

            for i in range(endingrow, startingrow - 1, -1):
                ans[i][startingcol] = count
                count = count + 1
            startingcol = startingcol + 1
        return ans
