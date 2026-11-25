def read_ints():
    return map(int, input().split())


def read_str():
    return input()


def read_list_ints():
    return list(map(int, input().split()))


def read_list_strs():
    return input().split()


def solve():
    n, m = read_ints()
    grid = [read_str() for _ in range(n)]
    costs = [read_list_ints() for _ in range(n)]

    dp = [[float("inf")] * 26 for _ in range(n)]
    memo = [[-1] * 26 for _ in range(n)]

    def dfs(i, c):
        if i == n:
            return 0
        if memo[i][c] != -1:
            return memo[i][c]

        result = float("inf")
        for j in range(26):
            if j == ord(grid[i] % 26) and costs[i][i // 26] != 0:
                continue
            result = min(
                result,
                dfs(1 + i, c) + (costs[i][i // 26] if j != ord(grid[i] % 26) else 0),
            )

        memo[i][c] = result
        return result

    result = 0
    for i in range(0, 26):
        result = min(result, dfs(0, i))

    print(result)


solve()
