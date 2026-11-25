def min_max_heights(n, m, heights):
    answers = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # Get the height at the intersection
            intersection_height = heights[i][j]

            # Get the heights in the current row and column
            row_heights = heights[i]
            col_heights = [heights[k][j] for k in range(n)]

            # Determine the minimum possible x
            x = max(intersection_height, max(row_heights), max(col_heights))

            # Assign the heights
            for k in range(n):
                for l in range(m):
                    if k == i or l == j:
                        answers[k][l] = x

    return answers


# Read input
n, m = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(n)]

# Compute answers
answers = min_max_heights(n, m, heights)

# Print answers
for row in answers:
    print(' '.join(map(str, row)))
