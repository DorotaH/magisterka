def count_rectangles(n, rectangles):
    table = []
    for _ in range(100):
        table.append([0] * 100)
    for x1, y1, x2, y2 in rectangles:
        for i in range(x1 - 1, x2):
            for j in range(y1 - 1, y2):
                table[i][j] += 1
    return sum(sum(row, 0) for row in table)


# Read input
n = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(count_rectangles(n, rectangles))
