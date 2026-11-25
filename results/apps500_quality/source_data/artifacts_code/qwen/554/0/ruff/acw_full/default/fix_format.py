def max_happiness(n, m, a, subarrays):
    # Initialize a list to keep track of the contribution of each flower
    happiness = [0] * n

    # Iterate over each subarray and update the happiness contribution
    for l, r in subarrays:
        for i in range(l - 1, r):
            happiness[i] += a[i]

    # Return the sum of the maximum values of each flower's contribution
    return sum(max(0, x) for x in happiness)


# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
subarrays = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and print the maximum happiness
print(max_happiness(n, m, a, subarrays))
