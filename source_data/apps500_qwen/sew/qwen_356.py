n, x, y = map(int, input().split())

# Calculate the distance from the starting positions to the coin
white_distance, black_distance = abs(x - 1) + abs(y - 1), abs(x - n) + abs(y - n)

# Determine the winner based on the distances
if  white_distance < black_distance:
    print("White")
elif  white_distance > black_distance:
    print("Black")
else:
    print("Black")  # If the distances are equal, the black king wins