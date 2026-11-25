def max_sum(N):
    """Calculates the maximum possible value of M_1 + M_2 + ... + M_N.

    Args:
        N (int): An integer satisfying 1 <= N <= 10^9.

    Returns:
        int: The maximum possible value of M_1 + M_2 + ... + M_N.
    """
    return N if N % 2 == 1 else N - 1


N = int(input())
print(max_sum(N))
