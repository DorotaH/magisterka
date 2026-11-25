def min_moves_to_same_color(n, positions):
	black_positions = [i for i in range(1, 1 + n) if i % 2 == 1]
	white_positions = [i for i in range(1, 1 + n) if i % 2 == 0]
	
	black_moves = 0
	white_moves = 0
	
	for pos in positions:
		if pos in black_positions:
			black_moves += abs(black_positions.index(pos) - positions.index(pos))
		else:
			white_moves += abs(white_positions.index(pos) - positions.index(pos))
	
	return min(black_moves, white_moves)


# Read input
n = int(input())
positions = list(map(int, input().split()))

# Output the result
print(min_moves_to_same_color(n, positions))
