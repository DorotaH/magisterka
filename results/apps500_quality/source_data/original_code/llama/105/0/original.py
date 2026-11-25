from sys import stdin, stdout

def main():
    N = int(stdin.readline())
    A = [list(map(int, stdin.readline().split())) for _ in range(N)]
    m = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            m[i][j] = A[i][j] - 1

    moves = {
        'knight': [(2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)],
        'bishop': (-1, -1),
        'rook': (0, 0)
    }

    dp = [[[float('inf'), float('inf')] for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 0

    for i in range(N):
        for j in range(N):
            for k, piece in enumerate(moves):
                x, y = moves[piece]
                for dx, dy in [(x, y), (-x, -y)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        dp[i][j][0] = min(dp[i][j][0], dp[nx][ny][k] + 1)
                        dp[i][j][1] = min(dp[i][j][1], dp[nx][ny][k] + 1)

                for dx, dy in [(1, 0), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if (dx, dy) == (0, 0):
                            dp[i][j][k+1] = min(dp[i][j][k+1], dp[nx][ny][k] + 1)
                        else:
                            dp[i][j][k+1] = min(dp[i][j][k+1], dp[nx][ny][k] + 1)

    ans = min(dp[-1][-1])
    print(ans[0], ans[1])

if __name__ == '__main__':
    main()
