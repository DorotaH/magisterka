class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def search(i, j, word):
            if not word:
                return True
            if i < 0 or j < 0 or m <= i or n <= j:
                return False
            if board[i][j] != word[0]:
                return False
            board[i][j] = "*"
            res = (
                search(1 + i, j, word[1:])
                or search(i - 1, j, word[1:])
                or search(i, 1 + j, word[1:])
                or search(i, j - 1, word[1:])
            )
            board[i][j] = word[0]
            return res

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    if search(i, j, word):
                        return True

        return False
