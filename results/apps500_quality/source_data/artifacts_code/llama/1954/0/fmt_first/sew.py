def nCr(n, r, p):
    """
    Compute nCr (n choose r) modulo p.

    Args:
        n (int): The total number of items.
        r (int): The number of items to choose.
        p (int): The prime modulo.

    Returns:
        int: The result of nCr modulo p.
    """
    num = 1
    den = 1
    for i in range(r):
        num=(num*(n-i))%p
        den=(den*(1 + i))%p
    return  (num*pow(den, p-2, p))%p


def num_ways(n, f, p):
    """
    Compute the number of ways to distribute n sweets among f friends such that
    no friend receives a multiple of f sweets.

    Args:
        n (int): The total number of sweets.
        f (int): The number of friends.
        p (int): The prime modulo.

    Returns:
        int: The number of ways to distribute the sweets modulo p.
    """
    # If n is divisible by f, return 0
    if  n % f == 0:
        return 0

    # Compute the number of ways to distribute the remaining sweets
    ways=0
    for i in range(1, n-1):
        # If i is not divisible by f, add nCr(n - 1, i, p) to the count
        if  0 != i % f:
            ways=(ways+nCr(n-1, i, p))%p

    # Return the count modulo p
    return  ways


# Read the number of queries from the input
q = int(input())

# Read and process each query
for  _ in  range(q):
    # Read n and f from the input
    n, f = map(int, input().split())

    # Compute and print the result
    result = num_ways(n, f, 10**9 + 7)
    print(result)