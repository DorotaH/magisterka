class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def reachable(T):
            bfs = [(0, 0)]
            seen = set((0, 0))
            for x, y in bfs:
                if grid[x][y] <= T:
                    if x == y == size - 1: return True
                    for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        if 0 <= i + x < size and 0 <= y + j < size and (i + x, y + j) not in seen:
                            seen.add((i + x, y + j))
                            bfs.append((i + x, y + j))
            return False

        # def swimInTime(x, y, t_cap, history):
        #     if x==size-1 and y==size-1:
        #         return True
        #     history.append((x, y))
        #     for dx, dy in dirs:
        #         if 0<=x+dx<size and 0<=y+dy<size and grid[x+dx][y+dy]<=t_cap and (x+dx, y+dy) not in history:
        #             if swimInTime(x+dx, y+dy, t_cap, history[:]):
        #                 return True
        #     return False

        minT, maxT = grid[0][0], size**2 - 1
        while minT<=maxT:
            midT = (minT+maxT)//2
            res = reachable(midT)
            if res:
                maxT = midT-1
            else:
                minT = 1+midT
        return minT