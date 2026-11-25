def max_emeralds(a, b):
    """
    Calculate the maximum number of emeralds Polycarp can earn.

    Parameters:
    a (int): The number of sticks.
    b (int): The number of diamonds.

    Returns:
    int: The maximum number of emeralds Polycarp can earn.
    """
    # Calculate the maximum number of shovels that can be crafted
    max_shovels = min(a // 2, b)

    # Calculate the remaining sticks and diamonds after crafting shovels
    remaining_sticks = a - 2 * max_shovels
    remaining_diamonds = b - max_shovels

    # Calculate the maximum number of swords that can be crafted with remaining sticks and diamonds
    max_swords = min(remaining_sticks, remaining_diamonds // 2)

    # The maximum number of emeralds is the sum of the number of shovels and swords
    return max_swords + max_shovels


# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of sticks and diamonds for the current test case
    a, b = map(int, input().split())

    # Calculate and print the maximum number of emeralds for the current test case
    print(max_emeralds(a, b))
