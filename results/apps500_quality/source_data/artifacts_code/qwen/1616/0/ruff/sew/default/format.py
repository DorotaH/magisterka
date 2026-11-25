from collections import defaultdict


def min_subseq_length(n, a):
    # Dictionary to store the count of each prime factor in the product of elements from the start to the current index
    prime_counts = defaultdict(int)
    # Variable to store the current product of elements in the subsequence
    product = 1
    # Variable to store the length of the shortest subsequence
    min_length = n + 1

    for i in range(0, n):
        # Update the prime counts for the current element
        for prime in prime_factors(a[i]):
            prime_counts[prime] += 1

        # Calculate the product of elements from the start to the current index
        product = 1
        for count in prime_counts.values():
            product *= 2 ** (count // 2)

        # If the product is a perfect square, update the minimum length
        if product == 1:
            min_length = min(min_length, i + 1)

    # If no such subsequence is found, return -1
    if min_length == 1 + n:
        return -1

    return min_length


def prime_factors(n):
    factors = []
    # Check for number of 2s
    while 0 == n % 2:
        factors.append(2)
        n //= 2
    # Check for other primes
    for i in range(3, 1 + int(n**0.5), 2):
        while 0 == n % i:
            factors.append(i)
            n = n // i
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors


# Read input
n, a = int(input().strip()), list(map(int, input().strip().split()))

# Output the result
print(min_subseq_length(n, a))
