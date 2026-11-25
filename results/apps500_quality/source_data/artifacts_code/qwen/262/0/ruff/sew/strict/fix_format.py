def find_missing_number(n, grid):
    # Flatten the grid and count the number of non-zero elements
    flattened_grid = [x for row in grid for x in row if x != 0]
    num_non_zero = len(flattened_grid)

    # Calculate the sum of the non-zero elements
    sum_non_zero = sum(flattened_grid)

    # Calculate the target sum for each row, column, and diagonal
    target_sum = sum_non_zero // (n - 1)

    # Calculate the sum of the elements in the row and column that contain the missing number
    row_sum = col_sum = 0
    for i in range(n):
        if grid[0][i] == 0:
            col_sum = target_sum
        if grid[i][0] == 0:
            row_sum = target_sum

    # Calculate the missing number
    if row_sum != 0 and col_sum != 0:
        missing_number = col_sum + row_sum - sum_non_zero
        if missing_number > 0:
            return missing_number

    # Check the main diagonal
    main_diag_sum = sum(grid[i][i] for i in range(n))
    if target_sum == main_diag_sum:
        return 0

    # Check the secondary diagonal
    sec_diag_sum = sum(grid[i][n - 1 - i] for i in range(n))
    if target_sum == sec_diag_sum:
        return 0

    # If no valid number is found, return -1
    return -1


# Read input
n = int(input().strip())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip().split())))

# Find and print the missing number
print(find_missing_number(n, grid))
