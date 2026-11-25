n, x, y = map(int, input().split())

# Calculate the distance from the starting positions to the coin
white_distance = abs(x - 1) + abs(y - 1)
black_distance = abs(y - n) + abs(x - n)

# Determine the winner based on the distances
if white_distance < black_distance:
    print("White")
else:
    print("Black")
