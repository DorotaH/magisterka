def  max_happiness(n, m, a, subarrays):
    # Initialize the happiness array with zeros
    happiness=[0]*n

    # Iterate over each subarray
    for  l, r in  subarrays:
        # Add the mood of each flower in the subarray to the corresponding position in the happiness array
        for  i in  range(l-1, r):
            happiness[i] += a[i]

    # Return the sum of the happiness array, which represents the maximum possible value added to Alyona's happiness
    return  sum(happiness, 0)


# Read input
n, m = map(int, input().split())
a, subarrays = list(map(int, input().split())), [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(max_happiness(n, m, a, subarrays))
