class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = board[i]
            col = [t[i] for t in board]
            if not self.checkRep(col) or not self.checkRep(row):
                return False
        for i in range(3):
            sub1 = (
                board[0][0 + i * 3 : 3 + i * 3]
                + board[1][0 + i * 3 : 3 + i * 3]
                + board[2][0 + i * 3 : 3 + i * 3]
            )
            sub2 = (
                board[3][0 + i * 3 : 3 + i * 3]
                + board[4][0 + i * 3 : 3 + i * 3]
                + board[5][0 + i * 3 : 3 + i * 3]
            )
            sub3 = (
                board[6][i * 3 + 0 : i * 3 + 3]
                + board[7][i * 3 + 0 : i * 3 + 3]
                + board[8][i * 3 + 0 : i * 3 + 3]
            )
            if (
                not self.checkRep(sub1)
                or not self.checkRep(sub2)
                or not self.checkRep(sub3)
            ):
                return False
        return True

    def checkRep(self, arr: List[str]) -> bool:
        table = dict()
        for i in arr:
            if i == ".":
                continue
            if i in table:
                return False
            table[i] = 0
        return True
