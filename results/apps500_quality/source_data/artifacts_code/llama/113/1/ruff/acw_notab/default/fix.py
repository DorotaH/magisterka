

def k_rounding(n, k):
    """
    Calculate the k-rounding of a given number n.
    
    Parameters:
    n (int): The input number.
    k (int): The number of trailing zeros.
    
    Returns:
    int: The k-rounding of n.
    """
    
    # Calculate the power of 10 needed to get k trailing zeros
    power = 10 ** k

    return n * power


# Read input from standard input
n, k = map(int, input().split())

# Calculate and print the k-rounding
print(k_rounding(n, k))
