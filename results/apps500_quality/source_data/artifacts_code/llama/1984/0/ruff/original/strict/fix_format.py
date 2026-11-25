import sys


def read_input():
    """Read input from standard input"""
    n, m, k, w = map(int, input().split())
    grid = []
    for _ in range(k):
        grid.append(list(input()))
    return n, m, k, w, grid


def compute_candy_map(grid):
    """Compute the candy map where each cell contains the number of candies in the corresponding cell"""
    n, m = len(grid), len(grid[0])
    candy_map = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            candy_map[i][j] = ord(grid[i][j]) if grid[i][j] != "." else 0
    return candy_map


def compute_difference(candy_map1, candy_map2):
    """Compute the difference between two candy maps"""
    n, m = len(candy_map1), len(candy_map1[0])
    diff = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            diff[i][j] = abs(candy_map1[i][j] - candy_map2[i][j])
    return diff


def compute_total_diff(grid, i, j, total_diff):
    """Compute the total difference between the grid and the corresponding cell in total_diff"""
    n, m = len(grid), len(grid[0])
    total_diff[i][j] = abs(ord(grid[i][j]) - ord(total_diff[i][j]))


def find_min_cost(grid):
    """Find the minimum cost to transfer all levels"""
    n, m, k, w, grid = read_input()
    candy_map = compute_candy_map(grid)
    dp = [[float("inf")] * (k + 1) for _ in range(k + 1)]
    parent = [[(-1, -1)] * (k + 1) for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(1, k):
        for j in range(i):
            diff = compute_difference(candy_map, compute_candy_map(grid[j]))
            for r in range(i):
                compute_total_diff(grid, r, 0, diff)
                compute_total_diff(grid, r, m - 1, diff)
            for r in range(m):
                compute_total_diff(grid, 0, r, diff)
                compute_total_diff(grid, n - 1, r, diff)
            total_diff = [[0] * m for _ in range(n)]
            for r in range(i):
                compute_total_diff(grid, r, 0, total_diff)
                compute_total_diff(grid, r, m - 1, total_diff)
                for c in range(m):
                    compute_total_diff(grid, 0, c, total_diff)
                    compute_total_diff(grid, n - 1, c, total_diff)
            for r in range(i):
                for c in range(m):
                    compute_total_diff(grid, r, c, total_diff)
            for r in range(n):
                compute_total_diff(grid, r, 0, total_diff)
                compute_total_diff(grid, r, m - 1, total_diff)
            for r in range(m):
                compute_total_diff(grid, 0, r, total_diff)
                compute_total_diff(grid, n - 1, r, total_diff)
            for r in range(i):
                compute_total_diff(grid, r, 0, total_diff)
                compute_total_diff(grid, r, m - 1, total_diff)
                for c in range(m):
                    compute_total_diff(grid, 0, c, total_diff)
                    compute_total_diff(grid, n - 1, c, total_diff)
            for r in range(i):
                for c in range(m):
                    compute_total_diff(grid, r, c, total_diff)
            for r in range(n):
                compute_total_diff(grid, r, 0, total_diff)
                compute_total_diff(grid, r, m - 1, total_diff)
            for r in range(m):
                compute_total_diff(grid, 0, r, total_diff)
                compute_total_diff(grid, n - 1, r, total_diff)
            dp[i + 1][0] = min(dp[i][0], dp[i][i] + w * (n * m))
            for j in range(i + 1):
                if dp[i][j] + w * (n * m) < dp[i + 1][j + 1]:
                    dp[i + 1][j + 1] = dp[i][j] + w * (n * m)
                    parent[i + 1][j + 1] = (i, j)
    return dp, parent


def find_min_cost_rec(grid, i, parent):
    """Find the minimum cost to transfer level i"""
    if i == 0:
        return 0
    j = parent[i][1]
    cost = dp[i][j] - dp[parent[i][0]][j] - w * (n * m)
    return cost


def print_result(grid, parent):
    """Print the result"""
    n, m, _, _, _ = read_input()
    k = len(grid)
    result = ""
    dp, parent = find_min_cost(grid)
    cost = dp[k][0]
    result += str(cost) + "\n"
    for i in range(1, k):
        cost = find_min_cost_rec(grid, i, parent)
        result += str(i + 1) + " " + str(parent[i][0] + 1) + "\n"
    sys.stdout.write(result)


n, m, k, w, grid = read_input()
print_result(grid, [[-1, -1]] * (k + 1))
