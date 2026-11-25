def find_magic_number(n, grid):
    # Flatten the grid and remove the zero
    flat_grid = [num for row in grid for num in row if num != 0]
    
    # Calculate the sum of the first row, column, and diagonal
    row_sum = sum(flat_grid[:n])
    col_sum = sum(flat_grid[i] for i in range(n))
    diag_sum = sum(flat_grid[i] for i in range(n))
    
    # Check if all sums are equal
    if row_sum == col_sum == diag_sum:
        return -1
    
    # Determine the missing value
    missing_value = -1
    for i in range(n):
        if sum(grid[i]) != row_sum:
            missing_value = row_sum - sum(grid[i])
            break
        if sum(grid[j][i] for j in range(n)) != col_sum:
            missing_value = col_sum - sum(grid[j][i] for j in range(n))
            break
        if sum(grid[i][i] for i in range(n)) != diag_sum:
            missing_value = diag_sum - sum(grid[i][i] for i in range(n))
            break
        if sum(grid[i][n - 1 - i] for i in range(n)) != diag_sum:
            missing_value = diag_sum - sum(grid[i][n - 1 - i] for i in range(n))
            break
    
    return missing_value if 1 <= missing_value <= 10**18 else -1


# Read input
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(find_magic_number(n, grid))
