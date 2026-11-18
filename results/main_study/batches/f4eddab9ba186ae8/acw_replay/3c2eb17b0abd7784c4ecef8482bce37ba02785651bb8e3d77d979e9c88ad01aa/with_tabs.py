class Solution:
	def totalNQueens(self, n: int) -> int:


		def isSafe(row, col, board):

			for i in range(col):
				if board[row][i] == "Q":
					return False

			i, j = row, col

			while (i >= 0 and 0 <= j):

				if board[i][j] == "Q":
					return False
				i -= 1
				j -= 1

			i, j = row, col

			while (i < n and 0 <= j):
				if board[i][j] == "Q":
					return False

				i += 1
				j -= 1

			return True



		def rec(board, col):

			nonlocal ans

			if col == n:
				ans += 1
				return



			for row in range(n):

				if isSafe(row, col, board):
					board[row][col] = "Q"
					rec(board, 1 + col)
					board[row][col] = 0



		board = [[0] * n for i in range(n)]

		ans = 0

		rec(board, 0)

		return ans
