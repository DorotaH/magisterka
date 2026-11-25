def calculate_emeralds(a, b):
    """
    Calculate the maximum number of emeralds Polycarp can earn.

    Parameters:
    a (int): The number of sticks.
    b (int): The number of diamonds.

    Returns:
    int: The maximum number of emeralds Polycarp can earn.
    """
    # Calculate the maximum number of swords that can be crafted with the given diamonds
    swords = min(b // 2, a // 1)

    # Calculate the remaining diamonds after crafting swords
    diamonds_remaining = b - 2 * swords

    # Calculate the maximum number of shovels that can be crafted with the remaining diamonds and the available sticks
    shovels = min(diamonds_remaining // 1, a - swords)

    # Return the total number of emeralds earned
    return shovels + swords


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the number of sticks and diamonds
    a, b = map(int, input().split())

    # Calculate and print the maximum number of emeralds
    print(calculate_emeralds(a, b))
