def find_initial_position(n, x):
    """
    Finds the initial position of the ball in the shell game.

    Args:
        n (int): The number of movements made by the operator.
        x (int): The index of the shell where the ball was found after n movements.

    Returns:
        int: The index of the shell where the ball was initially placed.
    """
    # If the number of movements is even, the initial position is the same as the final position.
    return x if n % 2 == 0 else (2 - x) % 3


n = int(input())
x = int(input())
print(find_initial_position(n, x))
