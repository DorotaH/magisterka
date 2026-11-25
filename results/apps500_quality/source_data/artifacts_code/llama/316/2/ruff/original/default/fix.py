def rhombus(n):
    """
    This function calculates the number of cells in a n-th order rhombus.
    
    Args:
    n (int): The order of the rhombus.
    
    Returns:
    int: The number of cells in the n-th order rhombus.
    """
    
    # Base case: A 1st order rhombus has 1 cell
    if n == 1:
        return 1
    
    # Recursive case: A n-th order rhombus is formed by adding cells to the (n-1)-th order rhombus
    else:
        # Calculate the number of cells in the (n-1)-th order rhombus
        prev_order = rhombus(n-1)
        
        # The number of new cells added to the (n-1)-th order rhombus to form the n-th order rhombus
        # is equal to 2*(n-1) + 2*(n-2) + ... + 2*1 = n*(n-1)
        new_cells = n*(n-1)
        
        # Return the total number of cells in the n-th order rhombus
        return prev_order + new_cells

# Read the input from standard input
n = int(input())

# Calculate and print the result
print(rhombus(n))
