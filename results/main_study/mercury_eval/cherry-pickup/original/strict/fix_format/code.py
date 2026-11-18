class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        @lru_cache(None)
        def dfs(x1, y1, x2, y2, n):
            if not (0 <= x1 < n and 0 <= y1 < n and 0 <= x2 < n and 0 <= y2 < n):
                return -50000000
            if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                return -50000000
            if x1 == y1 == x2 == y2 == 0:
                return grid[0][0]
            c1 = dfs(x1 - 1, y1, x2 - 1, y2, n)
            c2 = dfs(x1, y1 - 1, x2, y2 - 1, n)
            c3 = dfs(x1 - 1, y1, x2, y2 - 1, n)
            c4 = dfs(x1, y1 - 1, x2 - 1, y2, n)
            return (
                max(c1, c2, c3, c4) + grid[x1][y1] + (grid[x2][y2] if x1 != x2 else 0)
            )

        n = len(grid)
        r = dfs(n - 1, n - 1, n - 1, n - 1, n)
        return r if r > 0 else 0

        n = len(grid)
        forward = [(0, 1), (1, 0)]
        downward = [(-1, 0), (0, -1)]
        if grid[0][0] == -1 or grid[n - 1][n - 1] == -1:
            return 0
        arr = {}

        def dfs(i, j):
            nonlocal arr
            if i == n - 1 and j == n - 1:
                # arr.append((i,j))
                # print(i,j)
                return 0
            maxi = float("-inf")
            p, q = -1, -1
            for x, y in forward:
                if (
                    i + x >= 0
                    and j + y >= 0
                    and i + x < n
                    and j + y < n
                    and grid[i + x][j + y] != -1
                ):
                    temp = grid[i + x][j + y]
                    # grid[i+x][j+y] = 0
                    if dfs(i + x, j + y) + grid[i + x][j + y] > maxi:
                        p, q = i + x, j + y
                    maxi = max(dfs(i + x, j + y) + grid[i + x][j + y], maxi)
                    # grid[i+x][j+y] = temp
            # print(i,j, maxi)

            arr[(i, j)] = max(arr.get((i, j), 0), maxi)
            return maxi

        tt = max(0, dfs(0, 0))
        print(arr)
        return tt

        # Q = deque()
        # Q.append((0,0, grid[0][0]))
        # grid[0][0] = 0

        # maxi = 0
        # # print(type(Q))
        # while Q:
        #     i,j,count = Q.popleft()

        #     if i==n-1 and j == n-1:
        #         maxi = max(maxi, count)
        #     for x,y in forward:
        #         if i+x >= 0 and j+y >=0 and i+x < n and j+y < n and grid[i+x][j+y] != -1:
        #             Q.append((i+x, j+y, count+grid[i+x][j+y]))
        #             grid[i+x][j+y] = 0

        # Q = deque()
        # Q.append((0,0, grid[n-1][n-1]))
        # grid[n-1][n-1] = 0

        # maxj = 0
        # # print(type(Q))
        # while Q:
        #     i,j,count = Q.popleft()

        #     if i==0 and j == 0:
        #         maxj = max(maxj, count)
        #     for x,y in downward:
        #         if i+x >= 0 and j+y >=0 and i+x < n and j+y < n and grid[i+x][j+y] != -1:
        #             Q.append((i+x, j+y, count+grid[i+x][j+y]))
        #             grid[i+x][j+y] = 0

        # return maxi + maxj
