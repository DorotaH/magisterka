def count_includes_bonus(n: int) -> int:
    """
    Calculate the number of times a bonus is received for a given number of sales.

    Args:
        n (int): The number of sales.

    Returns:
        int: The number of times a bonus is received.
    """
    return sum(bool(all(i % j != 0 for j in range(2, 11)))
           for i in range(2, 1 + n))


# Read the input from standard input
n = int(input())

# Print the result to standard output
print(count_includes_bonus(n))
