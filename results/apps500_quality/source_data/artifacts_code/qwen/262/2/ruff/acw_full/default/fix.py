import sys


def find_magic_number(n, grid):
	# Flatten the grid to find the empty cell and calculate the sum of non-zero elements
	flat_grid = [x for row in grid for x in row if x != 0]
	total_sum = sum(flat_grid)
	
	# Calculate the target sum for each row, column, and diagonal
	target_sum = total_sum + n
	
	# Check if the target sum can be achieved by adding a single number to the grid
	for i in range(n):
		for j in range(n):
			if grid[i][j] == 0:
				# Calculate the number that would make the sum of the row, column, and diagonals equal to the target sum
				row_sum = sum(grid[i])
				col_sum = sum(grid[k][j] for k in range(n))
				diag_sum = sum(grid[k][k] for k in range(n))
				anti_diag_sum = sum(grid[k][n - k - 1] for k in range(n))
				
				# Check if the empty cell is on a row, column, or diagonal
				if row_sum == target_sum:
					return target_sum - row_sum + grid[i][j]
				if col_sum == target_sum:
					return target_sum - col_sum + grid[i][j]
				if diag_sum == target_sum:
					return target_sum - diag_sum + grid[i][j]
				if anti_diag_sum == target_sum:
					return target_sum - anti_diag_sum + grid[i][j]
	
	# If no valid number is found, return -1
	return -1


# Read input
input = sys.stdin.read
data = input().split()

n = int(data[0])
grid = []
index = 1
for _ in range(n):
	row = list(map(int, data[index:index + n]))
	grid.append(row)
	index += n

# Find and print the magic number
print(find_magic_number(n, grid))
