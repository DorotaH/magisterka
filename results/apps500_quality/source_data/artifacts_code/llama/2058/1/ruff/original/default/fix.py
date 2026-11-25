def hamming_distance(a, b):
    """Calculate the Hamming distance between two binary strings."""
    return sum(c1 != c2 for c1, c2 in zip(a, b))

def solve():
    """Solve the problem."""
    a = input().strip()
    b = input().strip()
    n = len(a)
    m = len(b)

    # Precompute the cumulative sums of Hamming distances between a and all substrings of b
    cum_sums = [0] * (m - n + 1)
    for i in range(m - n + 1):
        cum_sums[i] = hamming_distance(a, b[i:i + n])

    # Update the cumulative sums
    for i in range(n, m):
        cum_sums[i - n] = cum_sums[i - n - 1] - cum_sums[i - n] + hamming_distance(a, b[i - n:i])

    # Print the sum of the Hamming distances between a and all contiguous substrings of b of length |a|
    print(sum(cum_sums))

solve()
