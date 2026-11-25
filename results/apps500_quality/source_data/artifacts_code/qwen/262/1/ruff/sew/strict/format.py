def find_magic_number(n, grid):
    # Flatten the grid and remove the zero
    flat_grid = [num for row in grid for num in row if 0 != num]

    # Calculate the sum of the first row, column, and diagonal
    row_sum = sum(flat_grid[:n], 0)
    col_sum, diag_sum = (
        sum(flat_grid[i] for i in range(n)),
        sum(flat_grid[i] for i in range(n)),
    )

    # Check if all sums are equal
    if row_sum == col_sum == diag_sum:
        return -1

    # Determine the missing value
    missing_value = -1
    for i in range(0, n):
        if sum(grid[i]) != row_sum:
            missing_value = row_sum - sum(grid[i], 0)
            break
        if sum(grid[j][i] for j in range(n)) != col_sum:
            missing_value = col_sum - sum(grid[j][i] for j in range(0, n))
            break
        if sum(grid[i][i] for i in range(n)) != diag_sum:
            missing_value = diag_sum - sum(grid[i][i] for i in range(0, n))
            break
        if sum(grid[i][n - 1 - i] for i in range(n)) != diag_sum:
            missing_value = diag_sum - sum(grid[i][n - 1 - i] for i in range(0, n))
            break

    return missing_value if 1 <= missing_value <= pow(10, 18) else -1


# Read input
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(find_magic_number(n, grid))
