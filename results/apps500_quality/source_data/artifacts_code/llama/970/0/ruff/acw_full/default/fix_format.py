def min_moves(n, pieces):
    # Sort the pieces by their positions
    pieces.sort()

    # Calculate the median of the positions
    median = (pieces[len(pieces) // 2 - 1] + pieces[len(pieces) // 2]) // 2

    # Initialize the moves counter
    moves = 0

    # Count the number of pieces to the left of the median and the number to the right
    left = sum(bool(median > p) for p in pieces)
    right = len(pieces) - left

    # Move the pieces to the right of the median to the left and vice versa
    for p in pieces:
        moves += abs(p - median)
    # Return the total number of moves
    return moves


# Read the input
n = int(input())
pieces = list(map(int, input().split()))

# Print the result
print(min_moves(n, pieces))
