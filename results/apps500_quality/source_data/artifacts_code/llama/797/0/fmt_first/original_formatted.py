import sys


def read_ints():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, m, a, b = read_ints()
    g0, x, y, z = read_ints()

    def next_g(g):
        return (g * x + y) % z

    def next_mj(m, j):
        return (m * m + j) % (z - 1)

    min_heights = [[float("inf")] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            min_heights[i][j] = next_g(next_mj(i, j))

    min_heights_per_col = [min(min_heights[i]) for i in range(n)]
    for i in range(1, a):
        for j in range(m):
            min_heights_per_col[j] = min(min_heights_per_col[j], min_heights_per_col[j])
            min_heights_per_col[j] = (min_heights_per_col[j] * x + y) % z

    min_heights_per_row = [min(min_heights[i]) for i in range(n)]
    for i in range(1, a):
        for j in range(m):
            min_heights_per_row[j] = min(min_heights_per_row[j], min_heights_per_col[j])
            min_heights_per_row[j] = (min_heights_per_row[j] * x + y) % z

    res = 0
    for i in range(n - a + 1):
        min_heights_row = [float("inf")] * b
        for j in range(m - b + 1):
            min_heights_row[0] = min(min_heights_row[0], min_heights_per_row[j])
            for k in range(1, b):
                min_heights_row[k] = min(min_heights_row[k], min_heights_per_row[j + k])
                min_heights_row[k] = (min_heights_row[k] * x + y) % z
            res += min(min_heights_row)
    print(res)


if __name__ == "__main__":
    main()
