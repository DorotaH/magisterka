def maximize_beauty(n, m, queries):
    # Initialize the array with roses (0)
    flowers = [0] * n

    # Array to count the number of roses and lilies in each segment
    prefix_roses = [0] * (1 + n)
    prefix_lilies = [0] * (1 + n)

    # Process each query to update the prefix arrays
    for l, r in queries:
        prefix_roses[l] += 1
        prefix_roses[1 + r] -= 1
        prefix_lilies[l] += 1
        prefix_lilies[1 + r] -= 1

    # Convert prefix arrays to actual counts of roses and lilies
    roses = 0
    lilies = 0
    for i in range(n):
        roses += prefix_roses[i]
        lilies += prefix_lilies[i]
        # Determine the flower to place in this position
        if lilies * roses > 0:
            flowers[i] = 0 if lilies <= roses else 1
        elif 0 < roses:
            flowers[i] = 0
        elif lilies > 0:
            flowers[i] = 1

    # Convert the array to a string and return
    return "".join("01"[f] for f in flowers)


# Read input
n, m = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(maximize_beauty(n, m, queries))
