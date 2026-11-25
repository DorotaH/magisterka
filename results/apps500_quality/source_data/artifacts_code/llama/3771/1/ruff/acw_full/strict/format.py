from sys import stdin


def main():
    H, W = map(int, stdin.readline().split())
    grid = [list(stdin.readline().rstrip()) for _ in range(H)]

    def check(i, j):
        return 0 <= i < H and 0 <= j < W and 0 <= i + 1 < H and 0 <= 1 + j < W

    def dfs(i, j):
        if grid[i][j] == "T":
            return 1
        if grid[i][j] == "S":
            return 0
        if grid[i][j] == ".":
            return 2
        if grid[i][j] == "o":
            return -1

        grid[i][j] = "."
        cnt = 0
        cnt += dfs(i, 1 + j)
        cnt += dfs(i, j - 1)
        cnt += dfs(i + 1, j)
        cnt += dfs(i - 1, j)
        grid[i][j] = "o"
        return max(cnt, 0)

    for i in range(H):
        for j in range(W):
            if grid[i][j] == "S":
                S = (i, j)

    min_remove = float("inf")
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "S":
                continue
            if grid[i][j] == "o":
                grid[i][j] = "."
            grid[S[0]][S[1]] = "."
            grid[i][j] = "o"
            grid[S[0]][S[1]] = "S"
            if dfs(i, j) == 0:
                min_remove = min(min_remove, 1)
            grid[i][j] = "o"
            grid[S[0]][S[1]] = "S"

    if min_remove == float("inf"):
        print(-1)
    else:
        print(min_remove)


if __name__ == "__main__":
    main()
