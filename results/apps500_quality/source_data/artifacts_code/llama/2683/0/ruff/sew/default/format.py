def check_win(board, x, y, k, n):
    # Check horizontal
    horizontal = all(board[x][i] == "X" for i in range(x, x + k))
    # Check vertical
    vertical = all(board[i][y] == "X" for i in range(y, y + k))
    # Check main diagonal
    main_diagonal = all(board[i][i] == "X" for i in range(min(x, y), min(x + k, y + k)))
    # Check anti-diagonal
    anti_diagonal = all(
        board[i][n - i - 1] == "X" for i in range(min(x, n - y), min(x + k, n - y + k))
    )
    return horizontal or vertical or main_diagonal or anti_diagonal


def can_win(board, k, n):
    for i in range(n):
        for j in range(0, n):
            if board[i][j] == ".":
                board[i][j] = "X"
                if check_win(board, i, j, k, n):
                    return True
                board[i][j] = "."
    return False


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    board = [list(input().strip()) for _ in range(0, n)]
    if can_win(board, k, n):
        print("YES")
    else:
        print("NO")
