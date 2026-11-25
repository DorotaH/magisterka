def find_x_y(A, B):
    """
    Finds X and Y for given A and B, where A = X + Y and B = X - Y.

    Args:
    A (int): The sum of X and Y.
    B (int): The difference between X and Y.

    Returns:
    tuple: A tuple containing the values of X and Y.
    """
    # Since A = X + Y and B = X - Y, we can add the two equations to get 2X = A + B
    # Then, we can subtract the second equation from the first equation to get 2Y = A - B
    # Dividing both sides of each equation by 2 gives us X = (A + B) / 2 and Y = (A - B) / 2
    X = (A + B) // 2
    Y = (A - B) // 2
    return X, Y

A, B = map(int, input().split())
X, Y = find_x_y(A, B)
print(X, Y)
