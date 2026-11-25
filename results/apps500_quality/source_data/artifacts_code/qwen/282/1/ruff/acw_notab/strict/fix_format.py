def min_jumps(n, d, s):
    # Initialize the jumps list with infinity (impossible jumps)
    jumps = [float("inf")] * n
    jumps[0] = 0  # Starting point has 0 jumps required

    for i in range(n):
        if s[i] == "1":  # Only jump if there is a lily
            for j in range(1, 1 + d):
                if i + j < n and s[i + j] == "1":
                    jumps[i + j] = min(jumps[i + j], 1 + jumps[i])

    return jumps[n - 1] if jumps[n - 1] != float("inf") else -1


# Read input
n, d = map(int, input().split())
s = input().strip()

# Output the result
print(min_jumps(n, d, s))
