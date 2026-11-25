import sys

N = int(sys.stdin.readline())


def find_min_multiple(N):
    """
    Find the minimum positive integer divisible by both 2 and N.

    Args:
    N (int): A positive integer.

    Returns:
    int: The minimum positive integer divisible by both 2 and N.
    """

    # The smallest multiple of any number is the number itself if it is even, otherwise it is the number plus 1.
    # So, we use the expression N if N % 2 == 0 else N + 1 to calculate the smallest multiple of N
    return N if N % 2 == 0 else N + 1


print(find_min_multiple(N))
