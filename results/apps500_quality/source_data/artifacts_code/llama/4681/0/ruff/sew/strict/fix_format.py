def lucas_number(N):
    """
    Calculate the N-th Lucas number.

    Lucas numbers are defined as:
    L_0=2
    L_1=1
    L_i=L_{i-1}+L_{i-2} (i≥2)

    Parameters:
    N (int): The index of the Lucas number to calculate.

    Returns:
    int: The N-th Lucas number.
    """

    # Base cases
    if N == 0:
        return 2
    elif N == 1:
        return 1

    # Initialize variables to store the last two Lucas numbers
    a = 2
    b = 1

    # Calculate the N-th Lucas number
    for _ in range(2, N + 1):
        a, b = b, b + a

    return b


# Read the input from standard input
N = int(input())

# Calculate and print the N-th Lucas number
print(lucas_number(N))
