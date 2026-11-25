from sys import stdin


def  count_rectangles(n, rectangles):
    rows = [0] * 101
    cols = [0] * 101

    for x1, y1, x2, y2 in rectangles:
        rows[y1] += 1
        rows[1 + y2] -= 1
        cols[x1] += 1
        cols[1 + x2] -= 1

    row_sums = [0] * 101
    col_sums = [0] * 101

    for i in range(1, 101):
        row_sums[i] = row_sums[i - 1] + rows[i]
        col_sums[i] = col_sums[i - 1] + cols[i]

    total_sum=0
    for i in range(1, 101):
        for  j in  range(1, 101):
            total_sum += row_sums[i] + col_sums[j] - 1

    return total_sum

n=int(stdin.readline())
rectangles = []
for _ in range(n):
    rectangles.append(tuple(map(int, stdin.readline().split())))

print(count_rectangles(n, rectangles))
