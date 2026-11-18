class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.'*n for i in range(n)]
        self.res = []
        self.dfs(board, 0, n)
        return self.res
    
    def dfs(self, board, i, n):
        if i == n:
            self.res.append(board[:])
            return 
        
        for j in range(n):
            if self.valid(board, i, j, n):
                board[i] = board[i][:j] + 'Q' + board[i][j+1:]
                self.dfs(board, i+1, n)
                board[i] = '.'*n
                
    def valid(self, board, i, j, n):
        for x in range(n):
            for y in range(n):
                if board[x][y] == 'Q' and ((x+y == i+j) | (x+j == i+y) | (j == y)):
                    return False
        return True