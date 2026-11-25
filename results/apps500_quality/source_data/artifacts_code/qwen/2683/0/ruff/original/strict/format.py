def can_win_in_one_move(N, K, board):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def check_winner(player):
        for i in range(N):
            for j in range(N):
                if board[i][j] == ".":
                    board[i] = board[i][:j] + player + board[i][j + 1 :]
                    for di, dj in directions:
                        count = 1
                        for k in range(1, K):
                            ni, nj = i + di * k, j + dj * k
                            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == player:
                                count += 1
                            else:
                                break
                        if count == K:
                            board[i] = board[i][:j] + "." + board[i][j + 1 :]
                            return True
                    board[i] = board[i][:j] + "." + board[i][j + 1 :]
        return False

    return "YES" if check_winner("X") else "NO"


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        board = []
        for i in range(N):
            board.append(data[index + 2 + i * N])
        index += 2 + N * N
        results.append(can_win_in_one_move(N, K, board))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
