def can_win(n, k, board):
    def is_winning(board, player, x, y):
        # Check rows
        for i in range(n):
            count = 0
            for j in range(n):
                if board[i][j] == player:
                    count += 1
            if count == k:
                return True

        # Check columns
        for j in range(n):
            count = 0
            for i in range(n):
                if board[i][j] == player:
                    count += 1
            if count == k:
                return True

        # Check diagonals
        count = 0
        for i in range(n):
            if board[i][i] == player:
                count += 1
        if count == k:
            return True
        count = 0
        for i in range(n):
            if board[i][n - i - 1] == player:
                count += 1
        if count == k:
            return True

        return False

    # Try to place X in every empty cell
    for i in range(n):
        for j in range(n):
            if board[i][j] == ".":
                new_board = [row[:] for row in board]
                new_board[i][j] = "X"
                if is_winning(new_board, "X", 0, 0) or is_winning(new_board, "O", 0, 0):
                    return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    print(can_win(n, k, board))
