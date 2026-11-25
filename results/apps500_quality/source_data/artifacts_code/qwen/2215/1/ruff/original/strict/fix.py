def maximize_beauty(n, m, queries):
    # Initialize the array with roses (0)
    flowers = [0] * n

    # Array to count the number of roses and lilies in each segment
    prefix_roses = [0] * (n + 1)
    prefix_lilies = [0] * (n + 1)

    # Process each query to update the prefix arrays
    for l, r in queries:
        prefix_roses[l] += 1
        prefix_roses[r + 1] -= 1
        prefix_lilies[l] += 1
        prefix_lilies[r + 1] -= 1

    # Convert prefix arrays to actual counts of roses and lilies
    roses = 0
    lilies = 0
    for i in range(n):
        roses += prefix_roses[i]
        lilies += prefix_lilies[i]
        # Determine the flower to place in this position
        if roses * lilies > 0:
            flowers[i] = 0 if roses >= lilies else 1
        elif roses > 0:
            flowers[i] = 0
        elif lilies > 0:
            flowers[i] = 1

    # Convert the array to a string and return
    return ''.join('01'[f] for f in flowers)

# Read input
n, m = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(maximize_beauty(n, m, queries))
