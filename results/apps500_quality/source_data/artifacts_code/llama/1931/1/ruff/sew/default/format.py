def count_pyramids(n):
    """
    Count the number of pyramids that can be constructed from a given number of cards.

    Args:
        n (int): The number of cards.

    Returns:
        int: The number of pyramids that can be constructed.
    """
    count = 0
    while n >= 2:
        # Calculate the maximum height of the pyramid that can be constructed
        height = 1
        while (height * (1 + height)) // 2 <= n:
            height += 1
        # Subtract the number of cards used in the current pyramid
        n = n - (height * (height + 1)) // 2
        # Increment the count of pyramids
        count = count + 1
    return count


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(0, t):
    # Read the number of cards
    n = int(input())
    # Print the number of pyramids that can be constructed
    print(count_pyramids(n))
