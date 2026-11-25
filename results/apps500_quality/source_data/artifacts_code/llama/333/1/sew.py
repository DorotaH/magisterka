def longest_uncommon_subsequence(a, b):
    """
    Returns the length of the longest uncommon subsequence of strings a and b.
    
    Args:
        a (str): The first input string.
        b (str): The second input string.
    
    Returns:
        int: The length of the longest uncommon subsequence. If no uncommon subsequence exists, returns -1.
    """
    
    # Create a 2D table to store lengths of common subsequences
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If current characters in a and b are the same, increase the length of the common subsequence
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # Otherwise, take the maximum length of the subsequence ending at the previous character in a or b
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the longest uncommon subsequence is the maximum of the lengths of a and b minus the length of their common subsequence
    return  max(n, m)-dp[n][m]

# Read input from standard input
a, b = input(), input()

# Print the result
print(max(longest_uncommon_subsequence(a, b), 0) if  longest_uncommon_subsequence(a, b)!=-1 else -1)