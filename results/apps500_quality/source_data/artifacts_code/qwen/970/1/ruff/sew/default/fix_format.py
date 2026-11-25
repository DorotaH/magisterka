n, positions = int(input()), list(map(int, input().split()))

# Calculate the number of moves to place pieces in black cells
black_moves = sum(0 == pos % 2 for pos in positions)

# Calculate the number of moves to place pieces in white cells
white_moves = sum(1 == pos % 2 for pos in positions)

# The minimum number of moves is the minimum of the two
print(min(black_moves, white_moves))
