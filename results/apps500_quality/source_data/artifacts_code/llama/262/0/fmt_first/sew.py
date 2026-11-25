def read_input():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # Find the position of the empty cell
    for i in range(n):
        for j in range(n):
            if  grid[i][j] == 0:
                pos = (i, j)
                break

    # Calculate the sum of each row and each column
    row_sums = [sum(grid[i]) for i in range(n)]
    col_sums = [sum(grid[i][j] for i in range(n)) for j in range(n)]

    # Calculate the sum of the main diagonal
    main_diagonal_sum = sum(grid[i][i] for  i in  range(n))

    # Calculate the sum of the secondary diagonal
    secondary_diagonal_sum = sum(grid[i][n - i - 1] for  i in  range(n))

    # Calculate the total sum of the grid
    total_sum = sum(row_sums)

    # Check if the grid can be completed to a magic square
    if  (
        len(set(row_sums))>1
        or  len(set(col_sums))>1
        or  secondary_diagonal_sum != main_diagonal_sum
        or  0 != total_sum % n
    ):
        return  -1

    # Calculate the sum of the empty cell
    cell_sum = (total_sum - grid[pos[0]][pos[1]]) // n

    # Return the result
    return cell_sum


print(read_input())