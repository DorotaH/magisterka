class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        for i in range(n):
            board.append("." * n)
        self.res = []
        self.dfs(board, 0, n)
        return self.res

    def dfs(self, board, i, n):
        if n == i:
            self.res.append(board[:])
            return

        for j in range(n):
            if self.valid(board, i, j, n):
                board[i] = board[i][:j] + "Q" + board[i][1 + j :]
                self.dfs(board, 1 + i, n)
                board[i] = "." * n

    def valid(self, board, i, j, n):
        for x in range(n):
            for y in range(n):
                if board[x][y] == "Q" and (
                    (y + x == i + j) | (x + j == i + y) | (y == j)
                ):
                    return False
        return True
