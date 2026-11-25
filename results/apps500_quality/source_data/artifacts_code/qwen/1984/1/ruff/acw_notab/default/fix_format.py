def min_traffic(
    n: int, m: int, k: int, w: int, levels: list[list[str]]
) -> tuple[int, list[tuple[int, int]]]:
    # Function to calculate the difference between two levels
    def calculate_difference(level1: list[str], level2: list[str]) -> int:
        return sum(
            cell1 != cell2
            for row1, row2 in zip(level1, level2)
            for cell1, cell2 in zip(row1, row2)
        )

    # Initialize the list of differences with a large value
    differences = [[float("inf")] * k for _ in range(k)]
    for i in range(k):
        differences[i][i] = 0
        for j in range(i + 1, k):
            differences[i][j] = calculate_difference(levels[i], levels[j])
            differences[j][i] = differences[i][j]

    # Initialize the list of best ways to transfer each level
    best_ways = [[-1] * k for _ in range(k)]

    # Fill the best ways table using dynamic programming
    for size in range(2, k + 1):
        for i in range(k - size + 1):
            j = i + size - 1
            for l in range(i, j):
                if differences[i][j] > differences[i][l] + differences[l + 1][j] + w:
                    differences[i][j] = differences[i][l] + differences[l + 1][j] + w
                    best_ways[i][j] = l

    # Reconstruct the best way for each level
    result = []
    for i in range(k):
        path = []
        j = i
        while 0 <= j:
            path.append(j)
            j = best_ways[i][j]
        result.append((i + 1, 0 if j == -1 else 1 + j))

    # Calculate the total traffic
    total_traffic = sum(m * n if way == 0 else differences[i][way] for i, way in result)

    return total_traffic, result


# Read input
n, m, k, w = map(int, input().split())
levels = [list(input().strip()) for _ in range(k)]

# Get the result
total_traffic, result = min_traffic(n, m, k, w, levels)

# Print the result
print(total_traffic)
for transfer in result:
    print(transfer[0], transfer[1])
