

def max_abs_diff(n, m):
    """
    This function calculates the maximum possible value of the sum of absolute differences between adjacent elements in the array
    of length n with the sum m.

    Args:
        n (int): The length of the array.
        m (int): The sum of the array.

    Returns:
        int: The maximum possible value of the sum of absolute differences.
    """
    # If n is 1, the only possible array is [m], so the answer is 0
    if n == 1:
        return 0

    # If m is 0, the only possible array is [0], so the answer is 0
    return 0 if m == 0 else m * (n - 1)


def main():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # Read the length and sum of the array
        print(max_abs_diff(n, m))  # Calculate and print the maximum possible value of the sum of absolute differences


if __name__ == "__main__":
    main()
