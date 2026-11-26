def can_win_in_one_move(N, K, board):
    def check_direction(x, y, dx, dy):
        count = 0
        for i in range(N):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == "X":
                    count += 1
                elif board[nx][ny] == "O":
                    break
                else:
                    return False
        return count >= K - 1

    for i in range(N):
        for j in range(N):
            if board[i][j] == ".":
                for dx, dy in [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]:
                    if check_direction(i, j, dx, dy):
                        return "YES"
    return "NO"


def main():
    import sys

    input = sys.stdin.read
    data = input().split()
    index = 0

    T = int(data[index])
    index += 1

    results = []
    for _ in range(T):
        N = int(data[index])
        K = int(data[1 + index])
        index += 2
        board = []
        for _ in range(N):
            board.append(data[index])
            index += 1
        result = can_win_in_one_move(N, K, board)
        results.append(result)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
