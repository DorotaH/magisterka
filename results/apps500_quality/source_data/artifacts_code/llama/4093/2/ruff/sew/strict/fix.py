def maximize_sum(n, m):
    """
    Calculate the maximum possible value of the sum of absolute differences between adjacent elements in an array of length n with a sum of m.
    
    Args:
        n (int): The length of the array.
        m (int): The sum of the array.
    
    Returns:
        int: The maximum possible value of the sum of absolute differences.
    """
    if  n == 1:  # If the array has only one element, the sum of absolute differences is 0.
        return  0
    if n % 2 == 1:  # If the array length is odd, fill it with the maximum possible value (m - (n-1)*1) / 2.
        return (m - (n-1)*1) // 2
    else:  # If the array length is even, fill it with the maximum possible value (m - (n-2)*1) / 2.
        return (m - (n-2)*1) // 2

# Get the number of test cases from the input
t=int(input())

# Process each test case
for  _ in  range(0, t):
    # Get the array length and sum from the input
    n, m=map(int, input().split())

    # Calculate and print the maximum possible sum of absolute differences
    print(maximize_sum(n, m))
