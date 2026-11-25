def can_win(N, K, board):
    def check_win(char, row, col, dir):
        for i in range(1, K):
            r, c = row + dir[0] * i, col + i * dir[1]
            if 1 <= r <= N and 1 <= c <= N and board[r - 1][c - 1] == char:
                continue
            return False
        return True

    def check_win_in_row_col(char, x, y):
        return check_win(char, x, y, (0, 1)) or check_win(char, x, y, (1, 0))

    def check_win_in_diagonal(char, x, y):
        return check_win(char, x, y, (1, 1)) or check_win(char, x, y, (-1, 1))

    for i in range(1, N):
        for j in range(1, N):
            if board[i][j] == '.':
                board[i][j] = 'X'
                if check_win_in_row_col('O', i, j) or check_win_in_diagonal('O', i, j) or check_win_in_diagonal('O', N - i + 1, j) or check_win_in_row_col('O', N - i + 1, j):
                    return True
                board[i][j] = 'O'
                if check_win_in_row_col('X', i, j) or check_win_in_diagonal('X', i, j) or check_win_in_diagonal('X', N - i + 1, j) or check_win_in_row_col('X', N - i + 1, j):
                    return True
                board[i][j] = '.'

    return False


for _ in range(int(input())):
    N, K = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]
    if can_win(N, K, board):
        print('YES')
    else:
        print('NO')
