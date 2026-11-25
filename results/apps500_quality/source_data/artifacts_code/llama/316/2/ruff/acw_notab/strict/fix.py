def rhombus(n):
    """
    This function calculates the number of cells in a n-th order rhombus.
    
    Args:
    n (int): The order of the rhombus.
    
    Returns:
    int: The number of cells in the n-th order rhombus.
    """

    if n == 1:
        return 1

    # Calculate the number of cells in the (n-1)-th order rhombus
    prev_order = rhombus(n - 1)

    # The number of new cells added to the (n-1)-th order rhombus to form the n-th order rhombus
    # is equal to 2*(n-1) + 2*(n-2) + ... + 2*1 = n*(n-1)
    new_cells = (n - 1) * n

    # Return the total number of cells in the n-th order rhombus
    return new_cells + prev_order


# Read the input from standard input
n = int(input())

# Calculate and print the result
print(rhombus(n))
