def is_anti_sudoku(board):
    for i in range(9):
        if len(set(board[i])) == 1 or len(set(board[j][i] for j in range(9))) == 1:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if len(set(board[i + k][l + j] for k in range(3) for l in range(3))) == 1:
                return False
    return True


def make_anti_sudoku(board):
    for i in range(9):
        for j in range(9):
            if (
                len(set(board[i])) < 2
                or len(set(board[j][i] for j in range(9))) < 2
                or len(set(board[i + k][l + j] for k in range(3) for l in range(3))) < 2
            ):
                board[i][j] = str(1 + (int(board[i][j]) % 9))
    return board


def solve():
    t = int(input())
    results = []
    for _ in range(t):
        board = [list(input()) for _ in range(9)]
        anti_sudoku_board = make_anti_sudoku(board)
        results.append("\n".join("".join(row) for row in anti_sudoku_board))
    for result in results:
        print(result)


solve()
