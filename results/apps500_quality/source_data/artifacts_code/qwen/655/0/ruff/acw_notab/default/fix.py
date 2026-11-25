def determine_winner(n, x, y):
    # Calculate the Manhattan distance from the white king to the coin
    white_distance = abs(x - 1) + abs(y - 1)
    # Calculate the Manhattan distance from the black king to the coin
    black_distance = abs(y - n) + abs(x - n)
    # Determine the winner based on the distances
    return "White" if white_distance < black_distance else "Black"


# Read input
n = int(input())
x, y = map(int, input().split())

# Determine and print the winner
print(determine_winner(n, x, y))
