def  find_initial_position(n, x):
    """
    Finds the initial position of the ball in the shell game.

    Args:
        n (int): The number of movements made by the operator.
        x (int): The index of the shell where the ball was found after n movements.

    Returns:
        int: The index of the shell where the ball was initially placed.
    """
    # If the number of movements is even, the initial position is the same as the final position.
    if not n % 2 == 0:
        return (2 - x) % 3

    # If the number of movements is odd, the initial position is the opposite of the final position.
    # Since Python's modulo operator gives a result in the range [0, n-1], we need to add 2 to the result.
    # However, if the result is 2, we need to subtract 2 to get 0.
    else:
        return x


n, x = int(input()), int(input())
print(find_initial_position(n, x))
