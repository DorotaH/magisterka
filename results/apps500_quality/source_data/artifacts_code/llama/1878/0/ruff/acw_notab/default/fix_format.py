from sys import stdin


def count_rectangles(n, rectangles):
    rows = [0] * 101
    cols = [0] * 101

    for x1, y1, x2, y2 in rectangles:
        rows[y1] += 1
        rows[y2 + 1] -= 1
        cols[x1] += 1
        cols[x2 + 1] -= 1

    row_sums = [0] * 101
    col_sums = [0] * 101

    for i in range(1, 101):
        row_sums[i] = rows[i] + row_sums[i - 1]
        col_sums[i] = cols[i] + col_sums[i - 1]

    total_sum = 0
    for i in range(1, 101):
        for j in range(1, 101):
            total_sum += col_sums[j] + row_sums[i] - 1

    return total_sum


n = int(stdin.readline())
rectangles = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
print(count_rectangles(n, rectangles))
