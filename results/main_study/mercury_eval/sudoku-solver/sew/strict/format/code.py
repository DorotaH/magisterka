class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def convertToSub(i, j):
            return i // 3 * 3 + j // 3

        rowDct = collections.defaultdict(set)
        colDct = collections.defaultdict(set)
        subDct = collections.defaultdict(set)

        toFill = list()
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    toFill.append((i, j))
                else:
                    rowDct[i].add(board[i][j])
                    colDct[j].add(board[i][j])
                    subDct[convertToSub(i, j)].add(board[i][j])

        def fill(index):
            if index == len(toFill):
                return True
            i, j = toFill[index]
            for num in range(1, 10):
                fillItem = str(num)
                if any(
                    [
                        fillItem in rowDct[i],
                        fillItem in colDct[j],
                        fillItem in subDct[convertToSub(i, j)],
                    ]
                ):
                    continue
                board[i][j] = fillItem
                rowDct[i].add(board[i][j])
                colDct[j].add(board[i][j])
                subDct[convertToSub(i, j)].add(board[i][j])
                res = fill(1 + index)
                if res:
                    return True
                rowDct[i].remove(board[i][j])
                colDct[j].remove(board[i][j])
                subDct[convertToSub(i, j)].remove(board[i][j])
                board[i][j] = "."

        fill(0)
