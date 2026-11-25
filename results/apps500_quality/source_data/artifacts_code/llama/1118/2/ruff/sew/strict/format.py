def min_turns(n, c):
    """
    This function calculates the minimum number of turns needed to change the colors of all squares to a single color.

    Args:
        n (int): The number of squares.
        c (list): A list of integers representing the initial colors of the squares.

    Returns:
        int: The minimum number of turns needed.
    """
    last = [-1] * (
        1 + max(c)
    )  # Initialize a list to store the last index of each color
    cnt = [0] * (1 + max(c))  # Initialize a list to store the count of each color

    for i in range(n):
        # Update the last index of the current color and increment its count
        last[c[i]] = i
        cnt[c[i]] += 1

    ans = 0
    for i in range(1, max(c) + 1):
        # For each color, update the answer with the maximum of 0 and the count of the current color minus the count of the color that was present at the last index of the current color
        ans = max(ans, cnt[i] - (last[i] - last[c[i - 1]]))

    return ans


n, c = int(input()), list(map(int, input().split()))
print(min_turns(n, c))
