def min_repaint(S):
    """
    Calculate the minimum number of tiles that need to be repainted to satisfy the condition.

    Args:
        S (str): A string of length N representing the initial color of each tile.

    Returns:
        int: The minimum number of tiles that need to be repainted.
    """
    # Initialize variables to keep track of the number of white and black tiles
    white = 0
    black = 0

    # Initialize a variable to store the minimum number of tiles that need to be repainted
    repaint = 0

    # Iterate over the string S
    for c in S:
        # If the current character is '1', increment the white counter
        if c == '1':
            white += 1
        # If the current character is '0', increment the black counter
        else:
            black += 1

        # If the number of white or black tiles is greater than 1, we need to repaint the current tile
        if max(white, black) > 1:
            repaint += 1

            # Reset the counters to 0
            white = 0
            black = 0

    # Return the minimum number of tiles that need to be repainted
    return repaint


# Read the input from standard input
S = input()

# Print the result
print(min_repaint(S))
